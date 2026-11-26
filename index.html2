<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MAILLOT A KIN — Maillots, crampons et accessoires à Kinshasa</title>
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: Arial, sans-serif;
    color: #12124a;
    background: linear-gradient(180deg, #ffffff 0%, #e8ebff 45%, #c9d0ff 100%);
    background-attachment: fixed;
    padding-bottom: 90px;
  }

  .haut {
    position: sticky;
    top: 0;
    z-index: 30;
    background: #1a1a8c;
    box-shadow: 0 3px 12px rgba(0,0,0,.18);
  }

  .barre {
    display: flex;
    gap: 10px;
    padding: 10px 15px 6px;
    align-items: center;
  }

  .recherche {
    flex: 1;
    min-width: 0;
    padding: 13px;
    border-radius: 12px;
    border: none;
    font-size: 16px;
  }

  .panierbtn {
    background: transparent;
    border: 0;
    position: relative;
    padding: 8px;
    cursor: pointer;
  }

  .panierbtn svg {
    width: 30px;
    height: 30px;
    fill: white;
    display: block;
  }

  #nb {
    position: absolute;
    top: 0;
    right: 0;
    background: #ffd400;
    color: #12124a;
    border-radius: 50%;
    min-width: 20px;
    height: 20px;
    font-size: 12px;
    line-height: 20px;
    text-align: center;
    font-weight: bold;
  }

  .chips {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    padding: 4px 15px 12px;
  }

  .chips a {
    flex: 0 0 auto;
    background: rgba(255,255,255,.18);
    color: white;
    text-decoration: none;
    border-radius: 20px;
    padding: 9px 15px;
    font-size: 14px;
    font-weight: bold;
    white-space: nowrap;
  }

  header {
    text-align: center;
    padding: 16px 15px 6px;
  }

  header img {
    width: 110px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(26,26,140,.25);
  }

  header h1 {
    margin: 10px 0 4px;
    font-size: 24px;
    color: #1a1a8c;
  }

  header p {
    letter-spacing: 2px;
    font-size: 12px;
    opacity: .8;
    margin: 0;
  }

  section {
    max-width: 640px;
    margin: auto;
    padding: 15px;
  }

  .aide {
    text-align: center;
    opacity: .8;
    font-size: 14px;
    margin: 0 0 14px;
  }

  #vide {
    text-align: center;
    display: none;
    background: #fff3cd;
    color: #7a5b00;
    padding: 12px;
    border-radius: 12px;
    font-weight: bold;
  }

  .bannieres {
    display: flex;
    gap: 10px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    margin: 0 -15px;
    padding: 0 15px 8px;
  }

  .slide {
    flex: 0 0 88%;
    scroll-snap-align: center;
    display: flex;
    align-items: stretch;
    min-height: 160px;
    border-radius: 18px;
    overflow: hidden;
    background: linear-gradient(135deg, #1a1a8c, #3a3ad8);
    color: white;
    text-decoration: none;
  }

  .st {
    flex: 1;
    padding: 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .st small {
    opacity: .8;
    font-size: 11px;
    letter-spacing: 1px;
  }

  .st h3 {
    margin: 5px 0;
    font-size: 21px;
  }

  .st p {
    margin: 0 0 8px;
    font-size: 17px;
    font-weight: bold;
  }

  .st span {
    font-size: 14px;
    text-decoration: underline;
  }

  .slide img {
    width: 42%;
    object-fit: cover;
    display: block;
  }

  .rang, #accessoires {
    scroll-margin-top: 120px;
  }

  .rang h2 {
    margin: 22px 0 10px;
    font-size: 21px;
    color: #1a1a8c;
  }

  .defil {
    display: flex;
    gap: 12px;
    overflow-x: auto;
    scroll-snap-type: x proximity;
    margin: 0 -15px;
    padding: 4px 15px 14px;
  }

  .mini {
    flex: 0 0 160px;
    scroll-snap-align: start;
    background: #ffffff;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(26,26,140,.14);
    cursor: pointer;
  }

  .mini img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    display: block;
  }

  .mini h4 {
    font-size: 13px;
    margin: 9px 10px 4px;
    height: 36px;
    overflow: hidden;
  }

  .mini .prix {
    font-size: 16px;
    margin: 0 10px 12px;
    font-weight: bold;
    color: #1a1a8c;
  }

  .box {
    background: #ffffff;
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 18px;
    box-shadow: 0 4px 14px rgba(26,26,140,.12);
  }

  .box h3 {
    margin: 0 0 8px;
    color: #1a1a8c;
  }

  .box p {
    margin: 5px 0;
    font-size: 15px;
  }

  .acc {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }

  .acc a {
    background: #ffffff;
    border-radius: 16px;
    padding: 18px 8px;
    text-align: center;
    color: #12124a;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0 4px 14px rgba(26,26,140,.12);
  }

  .acc span {
    display: block;
    font-size: 38px;
    margin-bottom: 6px;
  }

  footer {
    text-align: center;
    padding: 22px 20px 30px;
    font-size: 13px;
    opacity: .75;
  }

  .barre-bas {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 40;
    background: #ffffff;
    padding: 10px 15px;
    box-shadow: 0 -4px 16px rgba(0,0,0,.12);
    display: flex;
    gap: 10px;
    align-items: center;
  }

  .btn-panier {
    flex: 1;
    background: #2f2fc8;
    color: white;
    border: 0;
    border-radius: 12px;
    padding: 14px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
  }

  .btn-wa {
    background: #25d366;
    color: white;
    border: 0;
    border-radius: 12px;
    padding: 14px 16px;
    font-size: 16px;
    font-weight: bold;
    text-decoration: none;
    white-space: nowrap;
  }

  .ov {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,.55);
    z-index: 60;
    display: none;
    align-items: flex-end;
    justify-content: center;
  }

  .feuille {
    background: #ffffff;
    color: #12124a;
    width: 100%;
    max-width: 640px;
    max-height: 88vh;
    overflow: auto;
    border-radius: 20px 20px 0 0;
    padding: 16px;
  }

  .feuille h3 {
    margin: 0 0 10px;
    color: #1a1a8c;
  }

  #f-img {
    width: 100%;
    max-height: 270px;
    object-fit: contain;
    background: #f6f7ff;
    border-radius: 14px;
    margin-bottom: 10px;
  }

  .prix {
    font-size: 22px;
    font-weight: bold;
    color: #1a1a8c;
  }

  .perso {
    font-size: 14px;
    opacity: .8;
    margin: 5px 0 10px;
  }

  .opt {
    width: 100%;
    padding: 13px;
    border-radius: 10px;
    border: 1px solid #c9d0ff;
    background: #f6f7ff;
    color: #12124a;
    margin-top: 10px;
    font-size: 16px;
  }

  .err {
    display: none;
    color: #d00000;
    font-size: 14px;
    margin-top: 8px;
    font-weight: bold;
  }

  .btn {
    display: block;
    width: 100%;
    background: #2f2fc8;
    color: white;
    text-align: center;
    padding: 14px;
    border: 0;
    border-radius: 12px;
    font-size: 16px;
    font-weight: bold;
    margin-top: 14px;
    cursor: pointer;
  }

  .lien {
    background: none;
    border: 0;
    color: #1a1a8c;
    opacity: .8;
    text-decoration: underline;
    font-size: 15px;
    margin: 12px 0 0;
    padding: 0;
    cursor: pointer;
  }

  .ligne {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding: 12px 0;
    border-bottom: 1px solid #dde1ff;
  }

  .qte {
    white-space: nowrap;
  }

  .qte button {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    border: 0;
    font-size: 18px;
    background: #e8ebff;
    color: #1a1a8c;
    cursor: pointer;
  }

  .total {
    font-size: 20px;
    font-weight: bold;
    margin: 16px 0;
    color: #1a1a8c;
  }

  #cartcom {
    margin-top: 10px;
    font-weight: bold;
  }

  @keyframes pop {
    0% { transform: scale(1); }
    50% { transform: scale(1.5); }
    100% { transform: scale(1); }
  }

  .pop { animation: pop .4s ease; }
</style>
</head>
<body>

<div class="haut">
  <div class="barre">
    <input class="recherche" id="recherche" type="search" placeholder="🔍 Rechercher : nike, adidas, psg...">
    <button class="panierbtn" id="ouvrir" aria-label="Ouvrir le panier">
      <svg viewBox="0 0 24 24"><path d="M7 18a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm10 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zM1 2v2h2l3.6 7.6-1.4 2.4A2 2 0 0 0 7 17h12v-2H7.4l1.1-2h7.5a2 2 0 0 0 1.7-1l3.6-6.5A1 1 0 0 0 20.4 4H5.2l-.9-2H1z"/></svg>
      <span id="nb">0</span>
    </button>
  </div>

  <div class="chips">
    <a href="#maillots">Maillots</a>
    <a href="#crampons">Crampons</a>
    <a href="#gants">Gants</a>
    <a href="#accessoires">Accessoires</a>
  </div>
</div>

<header>
  <img src="Kinshasa%20Teamwear%20Logo.PNG" alt="MAILLOT A KIN">
  <h1>MAILLOT A KIN</h1>
  <p>MAILLOTS & SPORTSWEAR · KINSHASA</p>
</header>

<section>
  <p class="aide">Tape une marque ou un club : nike, adidas, puma, psg, real madrid...</p>
  <p id="vide">Aucun résultat. Écris-nous sur WhatsApp, nous pouvons peut-être le trouver !</p>

  <div class="bannieres" id="bannieres"></div>

  <div class="rang" id="maillots">
    <h2>Maillots</h2>
    <div class="defil" id="liste-maillots"></div>
  </div>

  <div class="rang" id="crampons">
    <h2>Crampons</h2>
    <div class="defil" id="liste-crampons"></div>
  </div>

  <div class="rang" id="gants">
    <h2>Gants de gardien</h2>
    <div class="defil" id="liste-gants"></div>
  </div>

  <div class="box">
    <h3>🚚 Livraison à Kinshasa</h3>
    <p>Gombe, Pompage, UPN, Ngaliema et autres communes.</p>
  </div>

  <div class="box">
    <h3>💳 Modes de paiement</h3>
    <p>Orange Money et M-Pesa acceptés.</p>
    <p>Maillot sans personnalisation : paiement avant la livraison.</p>
    <p>Maillot personnalisé : 50 % à la commande, le reste à la livraison.</p>
  </div>

  <div id="accessoires">
    <h2>Accessoires sportifs</h2>
    <div class="acc">
      <a href="https://wa.me/243824814041?text=Bonjour%2C%20je%20veux%20des%20crampons%20de%20foot"><span>👟</span>Crampons</a>
      <a href="https://wa.me/243824814041?text=Bonjour%2C%20je%20veux%20des%20chaussettes"><span>🧦</span>Chaussettes</a>
      <a href="https://wa.me/243824814041?text=Bonjour%2C%20je%20veux%20des%20gants%20de%20gardien"><span>🧤</span>Gants de gardien</a>
      <a href="https://wa.me/243824814041?text=Bonjour%2C%20je%20veux%20un%20ballon%20de%20foot"><span>⚽</span>Ballons</a>
      <a href="https://wa.me/243824814041?text=Bonjour%2C%20je%20veux%20une%20m%C3%A9daille%20d%27or"><span>🥇</span>Médaille d'or</a>
      <a href="https://wa.me/243824814041?text=Bonjour%2C%20je%20veux%20une%20m%C3%A9daille%20d%27argent"><span>🥈</span>Médaille d'argent</a>
      <a href="https://wa.me/243824814041?text=Bonjour%2C%20je%20veux%20une%20m%C3%A9daille%20de%20bronze"><span>🥉</span>Médaille de bronze</a>
    </div>
  </div>
</section>

<footer>© MAILLOT A KIN · Kinshasa, RDC</footer>

<div class="barre-bas">
  <button class="btn-panier" id="ouvrir-bas">🛒 Voir mon panier</button>
  <a class="btn-wa" href="https://wa.me/243824814041?text=Bonjour%2C%20j%27ai%20une%20question">WhatsApp</a>
</div>

<div class="ov" id="fiche">
  <div class="feuille">
    <img id="f-img" src="" alt="">
    <h3 id="f-nom"></h3>
    <div class="prix" id="f-prix"></div>
    <div class="perso" id="f-perso"></div>
    <div id="f-opts"></div>
    <div class="err" id="f-err">📍 Choisis ta commune de livraison</div>
    <button class="btn" id="ajouter">🛒 Ajouter au panier</button>
    <button class="lien" id="f-fermer">Fermer</button>
  </div>
</div>

<div class="ov" id="overlay">
  <div class="feuille">
    <h3>🛒 Mon panier</h3>
    <div id="lignes"></div>
    <div id="cartcom"></div>
    <div class="total" id="total"></div>
    <button class="btn" id="commander">Commander sur WhatsApp</button>
    <button class="lien" id="vider">Vider le panier</button>
    <button class="lien" id="fermer">Continuer mes achats</button>
  </div>
</div>

<script>
const PRIX_MAILLOT = 20;
const PRIX_PERSO = 25;
const PRIX_CRAMPONS = 65;
const PRIX_GANTS = 40;

const COMMUNES = [
  'Gombe',
  'Pompage',
  'UPN',
  'Ngaliema',
  'Autre commune (je précise sur WhatsApp)'
];

const M = (nom, img, mots) => ({
  cat: 'maillots',
  nom,
  img,
  mots,
  prix: PRIX_MAILLOT,
  perso: PRIX_PERSO,
  ph: ''
});

const C = (nom, img, mots) => ({
  cat: 'crampons',
  nom,
  img,
  mots: mots + ' crampons chaussures',
  prix: PRIX_CRAMPONS,
  perso: 0,
  ph: 'Pointure (ex : 42)'
});

const G = (nom, img, mots) => ({
  cat: 'gants',
  nom,
  img,
  mots: mots + ' gants gardien',
  prix: PRIX_GANTS,
  perso: 0,
  ph: 'Taille (ex : 9)'
});

const articles = [
  M('FC Barcelone, noir et violet', '07405881-2946-435f-a05e-c10e0ca87309.JPG', 'nike barca barcelone'),
  M('Real Madrid, third vert', 'ff87788c-62cd-4f66-bd3d-046ad0ee55e3.JPG', 'adidas real madrid'),
  M('Manchester City, noir et or', 'cde8250d-b5b9-43a5-bb2e-5a59765e94e1.JPG', 'puma manchester city'),
  M('PSG, extérieur blanc', '1ae86674-5456-4d04-96c8-dcbc060b2389.JPG', 'nike psg paris'),
  M('Aston Villa, bordeaux', '16917675-76cb-45f6-869d-85ebc5b59c14.JPG', 'adidas aston villa'),
  M('Tottenham, domicile blanc', 'b05e7a1e-63ac-4721-9abc-262098045efc.JPG', 'nike tottenham spurs'),
  M('Juventus, noir et or', '449b4459-d5f9-4188-922b-68559e5ff58e.JPG', 'adidas juventus juve'),
  M('Bayern Munich, violet et rouge', '125a189e-3495-4102-8b9c-f4ea48b53205.JPG', 'adidas bayern munich'),

  C('Nike Air Zoom, bleu et rose', '7aaff630-c239-432c-a1bd-2ad28a2cb444.JPG', 'nike'),
  C('Nike Air Zoom, rose et orange', 'b266a7cb-26b9-486f-9b8b-25c889e8fdba.JPG', 'nike'),
  C('Nike Vapor, rose et blanc', 'ee5d6d6a-eb42-48de-a84b-402e6dcabadb.JPG', 'nike'),
  C('Nike Air Zoom, noir et rose', '1c90db5c-9ebc-45f0-b98c-35855bd63d21.JPG', 'nike'),
  C('Nike Vapor, rouge et or', '70e65ccd-ed21-42b4-9a46-06465b12f9f5.JPG', 'nike'),
  C('adidas Y-3, dragon et tigre', '5bbc3053-d6da-4e77-9f07-25e413aa0607.JPG', 'adidas y3'),
  C('adidas, noir et multicolore', '145fc687-c764-4e55-abd8-5464a9a7d6de.JPG', 'adidas'),

  G('adidas Predator, gris et rouge', '854776b3-56ef-4c09-9507-dbdd18169a3f.JPG', 'adidas predator'),
  G('adidas, vert et rose', '70dd41ac-845b-4b91-b0d7-39f7498fde4e.JPG', 'adidas'),
  G('adidas Predator, bleu et rose', '470afc52-ed9a-43dd-aa3c-75e290baf0bf.JPG', 'adidas predator'),
  G('Puma, rose et bleu', '685abd68-8a4d-43b6-88a7-578fe05be573.JPG', 'puma')
];

function esc(texte) {
  return String(texte).replace(/[&<>"']/g, caractere => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  }[caractere]));
}

const TITRES = {
  maillots: 'MAILLOTS DE CLUBS',
  crampons: 'CRAMPONS',
  gants: 'GANTS DE GARDIEN'
};

const PRIX = {
  maillots: PRIX_MAILLOT,
  crampons: PRIX_CRAMPONS,
  gants: PRIX_GANTS
};

let bannieres = '';

['maillots', 'crampons', 'gants'].forEach(categorie => {
  const article = articles.find(article => article.cat === categorie);

  bannieres += `
    <a class="slide" href="#${categorie}">
      <div class="st">
        <small>NOUVEAUTÉS</small>
        <h3>${TITRES[categorie]}</h3>
        <p>dès ${PRIX[categorie]} $</p>
        <span>Voir →</span>
      </div>
      <img src="${article.img}" alt="${esc(article.nom)}">
    </a>
  `;
});

document.getElementById('bannieres').innerHTML = bannieres;

articles.forEach((article, index) => {
  document.getElementById('liste-' + article.cat).innerHTML += `
    <div class="mini" data-voir="${index}" data-mots="${esc(article.mots)}">
      <img src="${article.img}" alt="${esc(article.nom)}" loading="lazy">
      <h4>${esc(article.nom)}</h4>
      <div class="prix">${article.prix} $</div>
    </div>
  `;
});

let panier = [];

try {
  panier = JSON.parse(localStorage.getItem('panier')) || [];
} catch (erreur) {
  panier = [];
}

let commune = '';

try {
  commune = localStorage.getItem('commune') || '';
} catch (erreur) {
  commune = '';
}

function sauver() {
  try {
    localStorage.setItem('panier', JSON.stringify(panier));
    localStorage.setItem('commune', commune);
  } catch (erreur) {}
}

let courant = 0;

function ouvrirFiche(index) {
  courant = index;
  const article = articles[index];

  document.getElementById('f-img').src = article.img;
  document.getElementById('f-nom').textContent = article.nom;
  document.getElementById('f-prix').textContent = article.prix + ' $';
  document.getElementById('f-perso').textContent = article.perso
    ? article.perso + ' $ avec personnalisation (nom + numéro)'
    : '';

  document.getElementById('f-err').style.display = 'none';

  const choixCommune = `
    <select class="opt commune">
      <option value="">📍 Choisir la commune de livraison</option>
      ${COMMUNES.map(commune => `<option>${commune}</option>`).join('')}
    </select>
  `;

  const taille = article.cat === 'maillots'
    ? `
      <select class="opt taille">
        <option>S</option>
        <option>M</option>
        <option>L</option>
        <option>XL</option>
      </select>
    `
    : `<input class="opt taille" placeholder="${article.ph}">`;

  const personnalisation = article.cat === 'maillots'
    ? `<input class="opt nomnum" placeholder="Nom + numéro (+${article.perso - article.prix} $, optionnel)">`
    : '';

  document.getElementById('f-opts').innerHTML = taille + choixCommune + personnalisation;
  document.querySelector('#f-opts .commune').value = commune;
  document.getElementById('fiche').style.display = 'flex';
}

function ajouter() {
  if (!commune) {
    document.getElementById('f-err').style.display = 'block';
    return;
  }

  const article = articles[courant];
  const fiche = document.getElementById('fiche');
  const taille = fiche.querySelector('.taille').value.trim();
  const champPerso = fiche.querySelector('.nomnum');
  const personnalisation = champPerso ? champPerso.value.trim() : '';
  const prix = personnalisation && article.perso ? article.perso : article.prix;

  const existant = panier.find(article =>
    article.nom === articles[courant].nom &&
    article.taille === taille &&
    article.perso === personnalisation
  );

  if (existant) {
    existant.qte++;
  } else {
    panier.push({
      nom: article.nom,
      taille,
      perso: personnalisation,
      prix,
      qte: 1
    });
  }

  sauver();
  majPanier();

  const compteur = document.getElementById('nb');
  compteur.classList.remove('pop');
  void compteur.offsetWidth;
  compteur.classList.add('pop');

  const bouton = document.getElementById('ajouter');
  bouton.textContent = '✅ Ajouté';

  setTimeout(() => {
    bouton.textContent = '🛒 Ajouter au panier';
    fiche.style.display = 'none';
  }, 700);
}

function majPanier() {
  const nombre = panier.reduce((total, article) => total + article.qte, 0);
  document.getElementById('nb').textContent = nombre;

  const liste = document.getElementById('lignes');
  const total = document.getElementById('total');

  document.getElementById('cartcom').textContent = commune
    ? '📍 Livraison : ' + commune
    : '';

  if (!panier.length) {
    liste.innerHTML = '<p>Votre panier est vide.</p>';
    total.textContent = '';
    return;
  }

  liste.innerHTML = panier.map((article, index) => `
    <div class="ligne">
      <div>
        <b>${esc(article.nom)}</b><br>
        <small>
          ${article.taille ? 'Taille : ' + esc(article.taille) : ''}
          ${article.perso ? ' · ' + esc(article.perso) : ''}
        </small><br>
        ${article.prix} $
      </div>
      <div class="qte">
        <button data-moins="${index}">−</button>
        ${article.qte}
        <button data-plus="${index}">+</button>
      </div>
    </div>
  `).join('');

  const montantTotal = panier.reduce((somme, article) => somme + article.prix * article.qte, 0);
  total.textContent = 'Total : ' + montantTotal + ' $';
}

function commander() {
  if (!panier.length) return;

  let message = 'Bonjour, je veux commander :\n';
  let montantTotal = 0;

  panier.forEach((article, index) => {
    message += `${index + 1}. ${article.nom}`;
    message += article.taille ? ` (taille ${article.taille})` : '';
    message += article.perso ? ` [personnalisation : ${article.perso}]` : '';
    message += ` x${article.qte} = ${article.prix * article.qte} $\\n`;

    montantTotal += article.prix * article.qte;
  });

  message += `Total : ${montantTotal} $\\n`;
  message += `Commune de livraison : ${commune}`;

  window.location.href = 'https://wa.me/243824814041?text=' + encodeURIComponent(message);
}

document.addEventListener('change', evenement => {
  if (evenement.target.classList.contains('commune')) {
    commune = evenement.target.value;
    sauver();
    majPanier();
    document.getElementById('f-err').style.display = 'none';
  }
});

document.addEventListener('click', evenement => {
  const cible = evenement.target;
  const produit = cible.closest('[data-voir]');

  if (produit) {
    ouvrirFiche(Number(produit.dataset.voir));
    return;
  }

  if (cible.dataset.plus !== undefined) {
    panier[Number(cible.dataset.plus)].qte++;
    sauver();
    majPanier();
  }

  if (cible.dataset.moins !== undefined) {
    const index = Number(cible.dataset.moins);
    panier[index].qte--;

    if (panier[index].qte <= 0) {
      panier.splice(index, 1);
    }

    sauver();
    majPanier();
  }

  if (cible.classList.contains('ov')) {
    cible.style.display = 'none';
  }
});

document.getElementById('ouvrir').addEventListener('click', () => {
  document.getElementById('overlay').style.display = 'flex';
});

document.getElementById('ouvrir-bas').addEventListener('click', () => {
  document.getElementById('overlay').style.display = 'flex';
});

document.getElementById('fermer').addEventListener('click', () => {
  document.getElementById('overlay').style.display = 'none';
});

document.getElementById('f-fermer').addEventListener('click', () => {
  document.getElementById('fiche').style.display = 'none';
});

document.getElementById('vider').addEventListener('click', () => {
  panier = [];
  sauver();
  majPanier();
});

document.getElementById('commander').addEventListener('click', commander);
document.getElementById('ajouter').addEventListener('click', ajouter);

majPanier();

const champRecherche = document.getElementById('recherche');

function filtrer() {
  const recherche = champRecherche.value.toLowerCase().trim();
  let resultats = 0;

  document.querySelectorAll('.mini, .acc a').forEach(element => {
    const titre = element.querySelector('h4');
    const texte = (element.dataset.mots || '') + ' ' + (titre ? titre.textContent : element.textContent);
    const visible = recherche === '' || texte.toLowerCase().includes(recherche);

    element.style.display = visible ? '' : 'none';

    if (visible) {
      resultats++;
    }
  });

  document.querySelectorAll('.rang').forEach(rang => {
    const visible = Array.from(rang.querySelectorAll('.mini')).some(mini => mini.style.display !== 'none');
    rang.style.display = visible ? '' : 'none';
  });

  document.getElementById('bannieres').style.display = recherche === '' ? '' : 'none';
  document.getElementById('vide').style.display = recherche !== '' && !resultats ? 'block' : 'none';
}

champRecherche.addEventListener('input', filtrer);
filtrer();
</script>
</body>
</html>
