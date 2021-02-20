"""
Cours : Tutoriel Python - créer un exécutable
Lien : https://www.youtube.com/watch?v=Jji2ik_AQOg

Dans ce programme on a recours à auto-py-to-exe pour convertir un fichier .py en un fichier .exe pour tout utilisateur
qui n'aurait pas python dans son ordinateur.

La manipulation est très simple, mais il ressort un tas de fichier avec un exécutable en Mo (et non en Ko), ce qui
ralentit considérablement les ordinateurs peu performants.

. Dans le répertoire où se trouve le fichier .py à exécuter, aller dans le répertoire venv->Scripts : copier le chemin
. Aller dans l'invite de commandes cmd puis saisir 'cd' et coller le chemin copier pour accéder directement au
répertoire Scripts
. Aller sur le lien : https://pypi.org/project/auto-py-to-exe/ et copier l'instruction d'installation de auto-py-to-exe
. Coller l'instruction d'installation auto-py-to-exe dans l'invite de commande dans le répertoire Scripts
. Aller dans le répertoire Scripts puis exécuter le fichier 'auto-py-to-exe'
. Dans la partie Console Window, si l'application est une interface graphique sélectionner 'Window Based (hide the
console)
. Dans la partie Icon, récupérer éventuellement l'icône qui s'affichera du fichier exécutable
. Dans la partie Additionnal Files, ajouter les fichiers telles que les bases de données
. Dans la partie Settings -> Output Directory (= répertoire de sortie) : sélectionner le bureau pour que le répertoire
avec le fichier exécutable puisse s'afficher directement sur le bureau
. Puis appuyer sur le bouton 'CONVERT .PY TO .EXE'

Éditeur : Laurent REYNAUD
Date : 20-02-2021
"""