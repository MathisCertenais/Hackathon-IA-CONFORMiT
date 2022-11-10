
# Histogramme des gradients #
Dans le cadre de la detection et classificaiton de symbol dans un fichier P&ID.
La technique HOG a pour role de créer un descripteur solide :
- Invariant par rotation
- Robuste et unique représentant la variation d'une image selon 8 directions

### Explication de la detection ###
La detection d'un symbol suit ces étapes :
- Parcours de l'image et création du hog de la fenetre en cours
- Comparaison des histogrammes (fonction de cout)
- Sauvegarde et suppression du symbol détecté en question

## Exemple dectection #


https://user-images.githubusercontent.com/98732552/201126597-3819de00-17bf-4839-ba31-47b168eb7477.mp4


### Lancement ###
- Ouvrir 'test2.py'
- S'assurer d'etre dns le bon dossier 'HOG'
- Lancement du .py



# Hackathon-IA-CONFORMiT
- Fichier arrow.py pour détecter et supprimer les liaisons des schémas électriques (flèches)
- Fichier text.py pour détecter, supprimer et stocker les informations (caractères et positions sur l'image) textuelles des schémas électriques



References :
https://www.mdpi.com/2076-3417/10/11/4005

