# Hackathon-IA-CONFORMiT
- Fichier arrow.py pour détecter et supprimer les liaisons des schémas électriques (flèches)
- Fichier text.py pour détecter, supprimer et stocker les informations (caractères et positions sur l'image) textuelles des schémas électriques



References :
https://www.mdpi.com/2076-3417/10/11/4005

## Histogramme des gradients ##
Dans le cadre de la detection et classificaiton de symbol dans un fichier P&ID.
La technique HOG a pour role de créer un descripteur solide :
- Invariant par rotation
- Robuste et unique représentant la variation d'une image selon 8 directions

La detection d'un symbol suit ces étapes :
- Parcours de l'image et création du hog de la fenetre en cours
- Comparaison des histogrammes (fonction de cout)
- Sauvegarde et suppression du symbol détecté en question
