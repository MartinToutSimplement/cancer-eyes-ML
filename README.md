# cancer-eyes-project

## Ceci est le code de la version non compressé du projet. Voici le lien du site déployé sur Azure : https://appeyess.azurewebsites.net/

### Prédiction du Cancer de l'Œil avec Vuejs par Martin LUCAS & Ahyl PRADHAN dans le cadre du projet DATACAMP

Ce projet est une application Vue.js conçue pour prédire la présence de cancer de l'œil grâce à un modèle de machine learning entraîné.

### Prérequis
Node.js: Assurez-vous d'avoir Node.js installé sur votre machine. Si ce n'est pas le cas, téléchargez-le et installez-le depuis nodejs.org. Grâce au requirements.txt, vous devez aussi installer les dépendances grace à npm install.


### Téléchargement du Modèle:

Rendez-vous sur le lien Google Drive fourni pour télécharger le modèle de machine learning: https://drive.google.com/drive/folders/1tiMhAXSwyVOUVeWwbEUdpDbD6vGMeXna?usp=drive_link

Une fois téléchargé, créez un dossier nommé "models" à la racine du dossier du projet.
Glissez-y le fichier du modèle eyes_model.h5 que vous venez de télécharger. Assurez-vous de ne pas renommer ce fichier.

### Lancement du Serveur de Développement:
Allez dans le dossier "web-eyes grâce aux commandes cd web-eyes puis npm run serve"
Faites aussi python app.py pour lancer le serveur Flask.

L'application devrait maintenant s'exécuter sur http://localhost:8080/ ou un autre port si le 8080 est déjà utilisé. Naviguez vers cette URL dans votre navigateur pour commencer à utiliser l'application.

### Comment Ça Marche?
Une fois sur le site, l'utilisateur peut télécharger une image de l'œil dans le bas de la page (œil fourni par le dataset). Le modèle de machine learning traitera cette image et fournira une prédiction quant à la présence ou non de cancer de l'œil.

### Comment le Modèle a-t-il été entraîné?
Le modèle a été entraîné sur un dataset de 1000 images d'œils. Le modèle a été entraîné sur 20 epochs de CNN. Le fichier model_creation.py nous a permis de créer le model en question. Les autres fichiers python sont des fichiers de tests pour comparer d'autres algorithmes de machine learning.

Merci d'avoir lu ce README.md et bonne utilisation de l'application!