# 🚗 Rush Hour Solver

> Un solveur algorithmique en Python pour le jeu de logique Rush Hour, comparant des approches de recherche non informée (BFS) et informée (Heuristiques/A*).

## 📌 Description
Ce projet a été réalisé dans le cadre du cursus ingénieur à l'École Polytechnique. Il modélise le jeu Rush Hour sous forme de graphe d'états et implémente plusieurs stratégies de résolution pour trouver le chemin optimal (nombre minimal de mouvements) pour sortir le véhicule rouge.

Le projet met l'accent sur l'analyse comparative des performances :
*   **BFS (Breadth-First Search)** : Garantit la solution optimale mais explore un grand nombre d'états.
*   **Heuristiques** : Utilisation de fonctions de coût pour guider la recherche et réduire l'espace d'états visité (optimisation du temps de calcul).

## 🚀 Fonctionnalités
- **Résolution pas à pas** : Visualisation de l'état initial, des mouvements et de la solution finale.
- **Analyse d'états** : Calcul et affichage des déplacements possibles à chaque étape.
- **Benchmarking** : Comparaison directe entre BFS et différentes heuristiques (temps, nœuds visités).
- **Batch Processing** : Capable de traiter une banque de 40 problèmes de difficulté variable.

## 🛠 Installation

Assurez-vous d'avoir Python installé. Installez les dépendances nécessaires via :

```bash
pip install -r requirements.txt
```

## 💻 Utilisation

### Lancer le Solveur
Le script principal permet de résoudre une grille spécifique parmi les 40 disponibles.

Depuis la racine du projet (`rush_hour/`) :
```bash
python bin/main.py
```
*Une invite de commande vous demandera ensuite de saisir le nom du fichier à traiter (ex: `GameP01.txt`).*

**Sortie du programme :**
1.  Affichage de la grille initiale.
2.  Liste des mouvements valides.
3.  Séquence de résolution optimale.
4.  Métriques de performance (nombre de coups, états explorés).
5.  Comparaison avec les heuristiques implémentées.

### Générer les Statistiques (Benchmark)
Pour lancer l'analyse comparative globale et générer les données de performance situées dans le dossier `results` :

```bash
python bin/Results.py
```

## 📊 Résultats et Analyse
Le dossier `results/` contient les scripts d'analyse et les données brutes comparant l'efficacité des algorithmes.
*   **Métrique clé** : Réduction de l'espace de recherche (nœuds visités) grâce aux heuristiques par rapport au BFS standard.

---
*Projet réalisé par Keyvan Attarian et Raphaël Herbeaux - École Polytechnique - Parcours Mathématiques Appliquées*
