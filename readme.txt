Ce projet implémente un solveur du jeu Rush Hour en utilisant d'abord un algorithme BFS puis en utilisant des heuristiques. 
Il permet de visualiser les étapes de résolution et de comparer l'efficacité de plusieurs algorithmes de résolution.

Avant d'exécuter il est recommandé d'installer les modules nécessaire en effectuant dans le terminal la commande :
pip install -r "requirements.txt"

Le fichier "main.py" situé dans le dossier "bin" permet d'exécuter toutes les fonctions de base
sur un des 40 fichiers choisi.
Apparaitront successivement:
-la situation initiale
-les déplacements réalisables à partir de cette situation
-la solution atteinte et le nombre de déplacements nécessaires, ainsi que le nombre d'états visités
-les déplacements intermédiaires réalisés pour atteindre la solution
-la solution atteinte avec les deux heuristiques implémentés ainsi que le nombre d'états visités dans chacun des cas

Pour l'exécuter il suffit de saisir dans le terminal, depuis le dossier "rush_hour":
python bin\main.py
Puis écrire le nom du fichier que l'on souhaite traiter.

Le dossier "results" contient des résultats et des statistiques à propos de ces différents algorithmes. Le code 
ayant permis de les obtenir est situé dans le même dossier.

Pour l'exécuter il suffit de saisir dans le terminal, depuis le dossier "rush_hour":
python bin\Results.py
