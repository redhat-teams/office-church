# Church Platform — Backend Django

Backend complet (Django 5 + Django REST Framework + SimpleJWT) connecté au frontend React.

---

## 📦 Contenu implémenté

| App                  | Rôle                                                         |
|-----------------------|--------------------------------------------------------------|
| `authentication`      | Connexion JWT (`/api/auth/token/`), stats du tableau de bord admin |
| `users`                | Gestion des utilisateurs (CRUD, rôles : member / staff / admin) |
| `events`               | Événements (CRUD + upload d'image)                           |
| `teachings`            | Enseignements / prédications (CRUD + miniature)              |
| `donations`            | Dons (création publique, gestion admin, changement de statut)|
| `prayerwinner`         | Demandes de prière (création publique + gestion admin)       |
| `contacts`             | Formulaire de contact                                        |
| `newsletter`           | Inscription newsletter                                       |
| `ccm`                  | Contenu de la page Ministère / CCM                            |
| `ministries`           | Liste des ministères                                          |
| `evangelisation`       | Inscriptions au programme d'évangélisation                    |
| `settings_app`         | Paramètres généraux de l'église (singleton)                   |
| `cinepay`               | Paiement CinetPay / PayPal pour les dons                      |

Toutes les routes en lecture (`GET`) sont publiques. Les routes de création/modification/suppression
sont protégées par JWT et réservées aux rôles **staff** ou **admin**, sauf les formulaires publics
(contact, newsletter, dons, prière, évangélisation) qui restent ouverts à tous.

---

## 🚀 Installation locale (Windows / macOS / Linux)

### 1. Se placer dans le dossier du projet

```bash
cd office-church
```

### 2. Créer et activer l'environnement virtuel

**Windows (PowerShell) :**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Le fichier `.env` est déjà présent à la racine avec des valeurs par défaut pour le développement.
Modifiez-le si vous voulez activer CinetPay / PayPal :

```env
CINETPAY_API_KEY=votre_clé
CINETPAY_SITE_ID=votre_site_id
PAYPAL_CLIENT_ID=votre_client_id
PAYPAL_SECRET=votre_secret
FRONTEND_URL=http://localhost:5173
BACKEND_URL=http://localhost:8000
```

### 5. Appliquer les migrations

```bash
python manage.py migrate
```

### 6. Créer un compte administrateur (pour te connecter sur /admin du frontend)

```bash
python manage.py createsuperuser
```

Renseigne un nom d'utilisateur, un email et un mot de passe.
⚠️ Pense ensuite à mettre son `role` sur `admin` (voir section suivante).

### 7. Définir le rôle admin sur ton compte (important !)

Le compte créé par `createsuperuser` a `is_superuser=True` mais son champ `role` reste
`member` par défaut. Pour qu'il s'affiche correctement côté frontend (badge "Administrateur"),
ouvre l'admin Django après avoir lancé le serveur (étape suivante) :

```
http://localhost:8000/admin/
```

Connecte-toi avec ton superuser, va dans **Users**, ouvre ton compte, et change le champ
**role** sur `admin`.

### 8. Lancer le serveur de développement

```bash
python manage.py runserver 0.0.0.0:8000
```

Le backend est maintenant disponible sur `http://localhost:8000`
(ou `http://<ton-ip-locale>:8000` si tu testes depuis un autre appareil sur le même réseau).

---

## 🔗 Connexion avec le frontend React

Le frontend (Vite) est déjà configuré pour proxy `/api` vers le backend dans `vite.config.js` :

```js
server: {
  proxy: {
    "/api": {
      target: "http://192.168.1.97:8000",  // ⚠️ remplace par l'IP de TA machine backend
      changeOrigin: true,
    },
  },
},
```

**Si tu lances le frontend et le backend sur la même machine**, remplace cette ligne par :
```js
target: "http://localhost:8000",
```

Puis démarre le frontend normalement :
```bash
cd ../view-church
npm install
npm run dev
```

Connecte-toi ensuite sur `http://localhost:5173/login` avec le compte admin créé à l'étape 7.

---

## 🔑 Endpoints d'authentification

| Méthode | URL                          | Description                          |
|---------|-------------------------------|---------------------------------------|
| POST    | `/api/auth/token/`            | Connexion → retourne `{access, refresh}` |
| POST    | `/api/auth/token/refresh/`    | Rafraîchit le token d'accès           |
| GET     | `/api/auth/health/`           | Health check                          |
| GET     | `/api/auth/stats/`            | Statistiques admin (staff/admin uniquement) |
| GET     | `/api/users/me/`               | Profil de l'utilisateur connecté      |

Body attendu pour `/api/auth/token/` :
```json
{ "username": "admin", "password": "motdepasse" }
```

---

## 🗂️ Endpoints principaux (CRUD)

Chaque ressource suit le même schéma REST standard :

```
GET    /api/events/            → liste (public, paginée, ?search=)
POST   /api/events/            → créer (staff/admin)
GET    /api/events/<id>/       → détail (public)
PATCH  /api/events/<id>/       → modifier (staff/admin)
DELETE /api/events/<id>/       → supprimer (staff/admin)
```

Identique pour `/api/teachings/`, `/api/donations/`, `/api/ministries/`, `/api/ccm/`.

Cas particuliers :
- `/api/donations/create/` → création publique d'un don
- `/api/users/` → liste/gestion des utilisateurs (staff/admin uniquement, pas de création — gérée via Django admin ou `createsuperuser`)
- `/api/prayer-requests/` → création publique ; `/api/prayer-requests/list/` → liste admin
- `/api/evangelisation/` → inscription publique ; `/api/evangelisation/list/` → liste admin

---

## 🖼️ Fichiers médias (images)

Les images uploadées (événements, enseignements, avatars...) sont servies depuis `/media/`
en développement automatiquement. En production, configure un service de stockage
(S3, Cloudinary, etc.) ou sers `/media/` via Nginx/Whitenoise selon ton hébergeur.

---

## 🌍 Déploiement en production

1. Définir les variables d'environnement de production dans `.env` ou directement sur ton hébergeur :
   ```env
   SECRET_KEY=...
   ALLOWED_HOSTS=tondomaine.com
   CORS_ALLOWED_ORIGINS=https://tondomaine.com
   DB_NAME=church
   DB_USER=postgres
   DB_PASSWORD=...
   DB_HOST=...
   DB_PORT=5432
   ```

2. Le script `build.sh` est prêt pour les hébergeurs type Render/Railway :
   ```bash
   bash build.sh
   ```
   Il installe les dépendances, exécute les migrations, collecte les fichiers statiques
   et crée un superuser `admin` par défaut si aucun n'existe.

3. Lancer avec Gunicorn :
   ```bash
   gunicorn core.wsgi:application
   ```

---

## ✅ Récapitulatif des commandes (résumé rapide)

```bash
# 1. Environnement virtuel
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux

# 2. Dépendances
pip install -r requirements.txt

# 3. Base de données
python manage.py migrate

# 4. Compte admin
python manage.py createsuperuser
# → puis mettre role=admin via /admin/

# 5. Lancer le serveur
python manage.py runserver 0.0.0.0:8000
```
