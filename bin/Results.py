#Code permettant d'obtenir les images et les statistiques qui sont dans le folder "results"
import sys
sys.path.append('C:/Users/rapha/rush_hour/src')
import matplotlib.pyplot as plt
import Solver
import numpy as np
import Heuristics

profs = []
counters = []
cases_blanches = []
voitures = []

sum1 = 0
sum2 = 0

for i in range (1,41):
  filename = f"GameP{i:02}.txt"
  solution, prof, counter = Solver.bestSolution_w_count(filename)
  _, _, counter1 = Solver.bestSolution_H(filename,Heuristics.h)
  _, _, counter2 = Solver.bestSolution_H(filename,Heuristics.h_with_added_penalty)
  sum1 = sum1 + (counter-counter1)/counter
  sum2 = sum2 + (counter-counter2)/counter
  profs.append(prof)
  counters.append(counter)
  cases_blanches.append(len(solution.free()))
  voitures.append(solution.nbrCar)
  print(f'{filename} : {solution.size} cases de côté, {len(solution.free())} cases libres, {solution.nbrCar} voitures, {prof} mouvements, {counter} étapes')

print(f"Avec l'heuristique comptant le nombre de voitures entre la rouge et la sortie, la diminution du nombre d'étapes est de {round(sum1*(100/40),3)}%")
print(f"Avec l'heuristique comptant le nombre de voitures entre la rouge et la sortie en ajoutant une pénalité selon la situation, la diminution du nombre d'étapes est de {round(sum2*(100/40),3)}%")

# Graphe décrivant le nombre d'étapes en fonction du nombres de voitures, en exécutant l'algorithme de résolution sans heuristique.
plt.figure(figsize=(8, 6))
plt.scatter(voitures, profs, marker='o', linestyle='-')
plt.xlabel("Nombre de voitures")
plt.ylabel("Nombre d'étapes")
plt.title("Nombre d'étapes en fonction du nombre de voitures")
plt.show()

#Histogramme du nombre d'étapes nécessaires dans les 40 fichiers donnés.
plt.figure(figsize=(8, 6))
plt.hist(profs, bins=10, edgecolor='black')  # Adjust the number of bins as needed
plt.xlabel("Nombre d'étapes")
plt.ylabel("Fréquence")
plt.title("Histogramme du nombre d'étapes")
plt.grid(True)
plt.show()



# Graphe décrivant le nombre d'étapes en fonction de cases occupées, en exécutant l'algorithme de résolution sans heuristique.
plt.figure(figsize=(8, 6))
plt.scatter(solution.size**2 - np.array(cases_blanches), profs, marker='o', linestyle='-')
plt.xlabel("Nombre de cases occupées")
plt.ylabel("Nombre d'étapes")
plt.title("Nombre d'étapes en fonction du nombre de cases occupées")
plt.show()
