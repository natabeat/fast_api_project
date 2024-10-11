# API de recommandation avec FastAPI

### Installation

1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt

2. API url : http://127.0.0.1:8000
3. Accès pour la recommendation du user 1 : http://127.0.0.1:8000/recommend/1
### Utilisation de l'API

Vous pouvez lancer l'API avec cette commande depuis la racine du projet :
   ```bash 
   uvicorn app.main:app --reload
```

### Avancement
set API + reco on liked book (via tags)