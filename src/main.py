import Game
import Solver
import Heuristics
import matplotlib.pyplot as plt

if __name__== "__main__":
  game = input("Sur quelle exemple voulez vous tester le programme? Choisir un GamePX.txt où X varie entre 01 et 40. ")

  currentState = Game.Game(game)
  currentState.show()
  plt.title(f"{game}")
  plt.show()
  
 
  moves = Solver.possibleMove(currentState)
  n = len(moves)
  cols = 3  # Nombre de colonnes
  rows = (n + cols - 1) // cols  # Nombre de lignes pour bien les répartir

  fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows))

  # Si 1 seule ligne, Matplotlib retourne un array 1D -> on force un tableau 2D
  if rows == 1:
      axes = axes.reshape(1, -1)

  for i, move in enumerate(moves):
      ax = axes[i // cols, i % cols]  # Récupérer le subplot correspondant
      plt.sca(ax)  # Sélectionner ce subplot
      move.show()  # Afficher dans ce subplot
      ax.set_title(f"Move {i+1}")  # Ajouter un titre
      ax.set_xticks([])  # Optionnel : enlever les axes si pas nécessaires
      ax.set_yticks([])

  # Cacher les subplots vides (si le nombre de moves < rows * cols)
  for j in range(i + 1, rows * cols):
      fig.delaxes(axes[j // cols, j % cols])

  plt.tight_layout()  # Ajuster les espacements
  plt.show()

  solution, prof = Solver.bestSolution(game)
  solution.show()
  plt.title(f'Solution obtenue en {prof} mouvements')
  plt.show()

  movesSol = Solver.giveSolution(solution)

  n = len(movesSol)
  cols = 3  # Nombre de colonnes
  rows = (n + cols - 1) // cols  # Nombre de lignes pour bien répartir

  fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows))

  # S'assurer que axes est un tableau 2D même si rows == 1
  if rows == 1:
      axes = axes.reshape(1, -1)

  for i, move in enumerate(movesSol):
      ax = axes[i // cols, i % cols]  # Récupérer le subplot correspondant
      plt.sca(ax)  # Sélectionner ce subplot pour que move.show() l'affiche dessus
      move.show()  # Afficher le mouvement
      ax.set_title(f"étape {i}" if i != 0 else "Situation initiale")
      ax.set_xticks([])
      ax.set_yticks([])

  # Cacher les subplots vides (si le nombre de moves < rows * cols)
  for j in range(n, rows * cols):
      fig.delaxes(axes[j // cols, j % cols])

  plt.tight_layout()  # Ajuster les espacements
  plt.show()

  
  for move in movesSol:
    plt.figure(figsize=(4,4))
    if move.move != None:
      plt.title(move.move[1])
    else:
      plt.title("Situation initiale")
    move.show()
    plt.show()

  solution, prof, counter = Solver.bestSolution_w_count(game)
  solution.show()
  plt.title(f'Sans heuristique: Solution pour {game} obtenue en {prof} mouvements, calculée en {counter} étapes')
  plt.show()

  solution, prof, counter = Solver.bestSolution_H(game,Heuristics.h)
  solution.show()
  plt.title(f'Heuristique h: Solution pour {game} obtenue en {prof} mouvements, calculée en {counter} étapes')
  plt.show()

  solution, prof, counter = Solver.bestSolution_H(game,Heuristics.h_with_added_penalty)
  solution.show()
  plt.title(f'Heuristique h avec pénalité: Solution pour {game} obtenue en {prof} mouvements, calculée en {counter} étapes')
  plt.show()
  
  