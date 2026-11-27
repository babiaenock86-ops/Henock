from datetime import date, datetime
from database import connecter, creer_tables


def saisir_date(message):
    while True:
        texte = input(message + " (AAAA-MM-JJ, vide si aucune) : ").strip()
        if texte == "":
            return None
        try:
            datetime.strptime(texte, "%Y-%m-%d")
            return texte
        except ValueError:
            print("Format invalide. Exemple : 2026-11-27")


def initialiser_vaccins():
    conn = connecter()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM vaccins")
    if cur.fetchone()[0] == 0:
        vaccins = [
            ("BCG", "Protège contre la tuberculose"),
            ("Polio", "Protège contre la poliomyélite"),
            ("Rougeole", "Protège contre la rougeole"),
            ("Pentavalent", "Diphtérie, tétanos, coqueluche, hépatite B, Hib"),
        ]
        cur.executemany(
            "INSERT INTO vaccins (nom_vaccin, description) VALUES (?, ?)",
            vaccins,
        )
        conn.commit()
    conn.close()


def enregistrer_enfant():
    print("\n--- Parent / tuteur ---")
    nom_parent = input("Nom du parent : ").strip()
    telephone = input("Téléphone : ").strip()
    adresse = input("Adresse : ").strip()

    print("\n--- Enfant ---")
    nom_enfant = input("Nom de l'enfant : ").strip()
    sexe = input("Sexe (M/F) : ").strip().upper()
    date_naissance = saisir_date("Date de naissance")

    if nom_parent == "" or nom_enfant == "":
        print("Le nom du parent et de l'enfant est obligatoire.")
        return

    conn = connecter()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO parents (nom, telephone, adresse) VALUES (?, ?, ?)",
        (nom_parent, telephone, adresse),
    )
    parent_id = cur.lastrowid
    cur.execute(
        "INSERT INTO enfants (nom, sexe, date_naissance, parent_id) "
        "VALUES (?, ?, ?, ?)",
        (nom_enfant, sexe, date_naissance, parent_id),
    )
    conn.commit()
    conn.close()
    print("Enfant enregistré.")


def lister_enfants():
    conn = connecter()
    cur = conn.cursor()
    cur.execute(
        "SELECT e.id, e.nom, p.nom, p.telephone "
        "FROM enfants e LEFT JOIN parents p ON e.parent_id = p.id"
    )
    lignes = cur.fetchall()
    conn.close()
    if not lignes:
        print("Aucun enfant enregistré.")
    for id_, nom, parent, tel in lignes:
        print(f"[{id_}] {nom} - parent : {parent} ({tel})")
    return lignes


def enregistrer_vaccin():
    nom = input("Nom du vaccin : ").strip()
    description = input("Description : ").strip()
    if nom == "":
        print("Le nom est obligatoire.")
        return
    conn = connecter()
    conn.execute(
        "INSERT INTO vaccins (nom_vaccin, description) VALUES (?, ?)",
        (nom, description),
    )
    conn.commit()
    conn.close()
    print("Vaccin enregistré.")


def lister_vaccins():
    conn = connecter()
    cur = conn.cursor()
    cur.execute("SELECT id, nom_vaccin FROM vaccins")
    lignes = cur.fetchall()
    conn.close()
    for id_, nom in lignes:
        print(f"[{id_}] {nom}")
    return lignes


def enregistrer_vaccination():
    if not lister_enfants():
        return
    enfant_id = input("ID de l'enfant : ").strip()
    print()
    lister_vaccins()
    vaccin_id = input("ID du vaccin : ").strip()
    date_admin = saisir_date("Date de vaccination")
    dose = input("Dose (ex : 1ère dose) : ").strip()
    date_prochaine = saisir_date("Date du prochain rappel")

    try:
        conn = connecter()
        conn.execute(
            "INSERT INTO vaccinations "
            "(enfant_id, vaccin_id, date_administration, dose, date_prochaine) "
            "VALUES (?, ?, ?, ?, ?)",
            (enfant_id, vaccin_id, date_admin, dose, date_prochaine),
        )
        conn.commit()
        conn.close()
        print("Vaccination enregistrée.")
    except Exception:
        print("Erreur : vérifie l'ID de l'enfant et du vaccin.")


def historique():
    if not lister_enfants():
        return
    enfant_id = input("ID de l'enfant : ").strip()
    conn = connecter()
    cur = conn.cursor()
    cur.execute(
        "SELECT v.nom_vaccin, vac.dose, vac.date_administration, "
        "vac.date_prochaine "
        "FROM vaccinations vac JOIN vaccins v ON vac.vaccin_id = v.id "
        "WHERE vac.enfant_id = ? ORDER BY vac.date_administration",
        (enfant_id,),
    )
    lignes = cur.fetchall()
    conn.close()
    if not lignes:
        print("Aucune vaccination pour cet enfant.")
    for vaccin, dose, date_admin, prochaine in lignes:
        print(f"{date_admin} - {vaccin} ({dose}) - prochain : {prochaine}")


def prochains_rappels():
    aujourdhui = date.today().isoformat()
    conn = connecter()
    cur = conn.cursor()
    cur.execute(
        "SELECT e.nom, v.nom_vaccin, vac.date_prochaine "
        "FROM vaccinations vac "
        "JOIN enfants e ON vac.enfant_id = e.id "
        "JOIN vaccins v ON vac.vaccin_id = v.id "
        "WHERE vac.date_prochaine >= ? ORDER BY vac.date_prochaine",
        (aujourdhui,),
    )
    lignes = cur.fetchall()
    conn.close()
    if not lignes:
        print("Aucun rappel prévu.")
    for enfant, vaccin, prochaine in lignes:
        print(f"{prochaine} - {enfant} : {vaccin}")


def enfants_en_retard():
    aujourdhui = date.today().isoformat()
    conn = connecter()
    cur = conn.cursor()

    print("\nRappels dépassés :")
    cur.execute(
        "SELECT e.nom, v.nom_vaccin, vac.date_prochaine "
        "FROM vaccinations vac "
        "JOIN enfants e ON vac.enfant_id = e.id "
        "JOIN vaccins v ON vac.vaccin_id = v.id "
        "WHERE vac.date_prochaine < ? ORDER BY vac.date_prochaine",
        (aujourdhui,),
    )
    retards = cur.fetchall()
    if not retards:
        print("Aucun.")
    for enfant, vaccin, prochaine in retards:
        print(f"{enfant} : {vaccin} (prévu le {prochaine})")

    print("\nEnfants jamais vaccinés :")
    cur.execute(
        "SELECT nom FROM enfants "
        "WHERE id NOT IN (SELECT enfant_id FROM vaccinations)"
    )
    jamais = cur.fetchall()
    if not jamais:
        print("Aucun.")
    for (nom,) in jamais:
        print(nom)
    conn.close()


def menu():
    creer_tables()
    initialiser_vaccins()
    actions = {
        "1": enregistrer_enfant,
        "2": enregistrer_vaccin,
        "3": enregistrer_vaccination,
        "4": historique,
        "5": prochains_rappels,
        "6": enfants_en_retard,
    }
    while True:
        print("\n=== Vaccinations des enfants ===")
        print("1. Enregistrer un enfant et son parent")
        print("2. Enregistrer un vaccin")
        print("3. Enregistrer une vaccination")
        print("4. Historique vaccinal d'un enfant")
        print("5. Prochaines dates prévues")
        print("6. Enfants nécessitant un suivi")
        print("0. Quitter")
        choix = input("Votre choix : ").strip()
        if choix == "0":
            print("Au revoir.")
            break
        elif choix in actions:
            actions[choix]()
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
