"""
Cours : [OLD] Tutoriel Python - créer exécutable (cx_Freeze)
Lien : https://www.youtube.com/watch?v=essSa78iv-A

Ci-dessous les instructions à opérer pour convertir le fichier .py souhaité en fichier .exe:
    • aller sur le fichier .py que l'on souhaite convertir
    • aller dans le menu File -> Settings…
    • sélectionner à gauche de la fenêtre 'Project Interpreter'
    • cliquer sur l'icône '+' situé en haut à droite de la fenêtre (Install)
    • dans la barre de recherche taper cx-Freeze puis cliquer sur ‘Install Package’

Création d’un fichier.py :
    • enregistrer le fichier dans PYCHARM sous NomFichier.py

Création d'un fichier setup.py :
• pour le répertoire 'Tutos' aller sur C:\Users\LRCOM\PycharmProjects\Tutos\venv\Scripts
• Puis cliquer sur le fichier exécutable 'cxfreeze-quickstart' (qui a été créé en installant le package cx-Freeze en
répondant aux questions suivantes :
    -> Project name : nom du projet
    -> Version : version du projet (la première version commence par principe par 1.0)
    -> Description : description du projet
    -> Python file to make executable from : NomDuFichier.py à convertir
    -> Executable file name : NomDuFichier en .exe (par principe même nom que le fichier.py
    -> (C)onsole application, (G)UI application, or (S)ervice : saisir G (évite l’affichage de la console)
    -> Save setup script to [setup.py]: saisir setup.py
    -> Run this now [n]? : saisir 'n'
• Si un ou plusieurs modules ont été importés dans le fichier.py, aller dans le fichier setup.py puis saisir dans
l’instruction suivante :
build_options = {‘includes’ : [‘NomModule1’, ‘NomModule2’…], ‘packages’:[], ‘excludes’:[]}
• Si un ou plusieurs fichiers sont à importer :
build_options = {include_files : [‘NomFichier1.extension’, ‘NomFichier2.extension’,…],...}


Un fichier setup.py a été créé au même endroit que le fichier exécutable 'cxfreeze-quickstar', en l'ouvrant on a les
instructions ci-dessous à titre d’exemple :

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [],
                 'include_files': ['CharlesSebastian.ttf', 'LogoBis.jpg'],
                 'includes':['tkinter', 'locale', 'pygame', 'datetime']}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('Tva.py', base=base, targetName = 'CalculetteTva', icon='Logo.ico')
]

setup(name='Calculette TVA',
      version = '2.1',
      description = 'Resultat a partir du montant HT ou de la TVA ou du montant TTC selon le taux choisi',
      options = {'build_exe': build_options},
      executables = executables)


Attention : l’icône n’est que celui présent dans l’exécutable, l’affichage d’icône dans la fenêtre tkinter n’est pas
mise (donc l’instruction root.iconbitmap(…) n’est pas mise dans le programme)

Convertir le fichier .py en fichier .exe :
    • Copier le fichier à convertir dans le répertoire où se trouve le fichier setup.py générer (ici le chemin est le
    suivant : C:\Users\LRCOM\PycharmProjects\Tutos\venv\Scripts) ainsi que les fichiers annexes ;
    • Aller dans la ligne de commande (LDC) de Windows ‘cmd’ puis aller au répertoire où se trouve le fichier setup.py
    généré ainsi que le fichier .py à convertir copié dans le même répertoire que setup.py ;
    • puis saisir dans la LDC : python setup.py build
Si le message suivant apparaît : « no module named cx_Freeze »
    • saisir dans la LDC : pip install --upgrade cx_Freeze (pour une mise à jour du module)
    • puis re-saisir dans la LDC : python setup.py build


Lancement du fichier .exe :
    • Quitter la LDC ;
    • Aller dans le nouveau sous-répertoire créé situé dans le répertoire où se trouve le fichier .py à convertir et le
    fichier setup.py ;
    • Dans ce sous-répertoire au nom de ‘exe.win32-3.8’  se trouve le fichier .exe → copier ce répertoire pour recourir
    à Inno Setup Compiler : https://www.youtube.com/watch?v=ormsdIk_Uhw

Attention : classer les fichiers et les répertoires du dossier installé de la même manière que le dossier d’origine
avant de lancer Inno Setup Compiler.

Éditeur : Laurent REYNAUD
Date : 20-02-2021
"""