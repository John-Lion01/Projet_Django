# <img src="./django-logo-png_seeklogo-394570.png" width="30px" height="30px"/> Projet Django

Un projet simple réalisé avec **Django**, permettant de :

- créer une base de données à partir de modèles Django  
- soumettre un **formulaire** basé sur ces modèles  
- gérer les données via une **interface d’administration** intuitive  

Ce projet constitue une excellente introduction au framework Django.

---

## 🚀 Fonctionnalités

- Modèles Django définissant la structure de la base de données  
- Formulaire de questionnaire généré automatiquement  
- Enregistrement des données dans la base  
- Interface admin pour consulter, modifier et supprimer les entrées  
- Architecture Django standard (views, templates, urls)

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/John-Lion01/Projet_Django.git
cd Projet_Django
```

### 2. Créer un environnement virtuel

```bash
python -m venv env
source env/bin/activate  # Linux / macOS
env\Scripts\activate     # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur

```bash
python manage.py runserver
```

Accès au site :  
👉 http://127.0.0.1:8000/

Accès à l’admin :  
👉 http://127.0.0.1:8000/admin/

---
