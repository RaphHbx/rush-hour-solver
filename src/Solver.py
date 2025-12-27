import Car
from collections import deque
import Game
import heapq

def possibleMove(currentState):
  """
  Renvoie tous les déplacements possibles à partir de l'état actuel
  """
  moves = []
  for car in currentState.cars:
    if car.pos == 'h':
      fixe = car.y
      movable = car.x
      for i in range(movable+car.l,currentState.size):
        if currentState.grid[i,fixe] == 0:
          moves.append(currentState.copy(Car.Car(car.id,car.pos,car.l,i-car.l+1,fixe)))
        else:
          break
      for i in range(movable-1,-1,-1):
        if currentState.grid[i,fixe] == 0:
          moves.append(currentState.copy(Car.Car(car.id,car.pos,car.l,i,fixe)))
        else:
          break
    else:
      fixe = car.x
      movable = car.y
      for j in range(movable+car.l,currentState.size):
        if currentState.grid[fixe,j] == 0:
          moves.append(currentState.copy(Car.Car(car.id,car.pos,car.l,fixe,j-car.l+1)))
        else:
          break
      for j in range(movable-1,-1,-1):
        if currentState.grid[fixe,j] == 0:
          moves.append(currentState.copy(Car.Car(car.id,car.pos,car.l,fixe,j)))
        else:
          break

  return moves

def bestSolution(file):
  """
  Renvoie la solution atteignable en le moins de déplacements possibles (BFS)
  """
  currentState = Game.Game(file)
  visited = set()
  toVisit = deque()
  toVisit.append((currentState,0))

  while toVisit:

    currentState,prof = toVisit.popleft()
    if currentState.isFinished():
      return currentState,prof
    for move in possibleMove(currentState):
      if move not in visited:
        visited.add(move)
        toVisit.append((move,prof+1))
  return

def bestSolution_w_count(file):
  """
  Renvoie la même solution que bestSolution() mais avec un compteur du nombres d'étapes effectuées pour l'atteindre.
  """
  currentState = Game.Game(file)
  visited = set()
  toVisit = deque()
  toVisit.append((currentState,0))
  count = 0
  while toVisit:
    count += 1
    currentState,prof = toVisit.popleft()
    if currentState.isFinished():
      return currentState,prof,count
    for move in possibleMove(currentState):
      if move not in visited:
        visited.add(move)
        toVisit.append((move,prof+1))
  return

def giveSolution(solution):
  """
  Renvoie l'ensemble des déplacements nécessaires pour atteindre la solution.
  """
  currentState = solution
  moves = [solution]
  while currentState.move != None:
    moves.append(currentState.move[0])
    currentState = currentState.move[0]
  return moves[::-1]

def bestSolution_H(file, h):
    """
    Renvoie une la solution atteignable en le moins de déplacements possibles tout en utilisant une heuristique consistante.
    Renvoie également le nombre d'étapes nécessaires pour atteindre cette solution.
    """
    currentState = Game.Game(file)
    visited = {}  # Dictionnaire pour stocker le meilleur coût connu pour chaque état
    toVisit = []
    heapq.heappush(toVisit, (h(currentState), 0, currentState))  # (f(n), g(n), état)
    counter = 0

    while toVisit:

        _, prof, currentState = heapq.heappop(toVisit)

        if currentState.isFinished():
            return currentState, prof, counter

        # Si l'état a déjà été visité avec un coût inférieur, on l'ignore
        if currentState in visited and visited[currentState] <= prof:
            continue

        # On marque l'état comme visité avec le coût actuel
        visited[currentState] = prof
        counter += 1

        for move in possibleMove(currentState):
            g_move = prof + 1  # Coût (profondeur)
            f_move = g_move + h(move)  

            # Si le mouvement n'a pas été visité ou si on a trouvé un meilleur chemin
            if move not in visited or visited[move] > g_move:
                heapq.heappush(toVisit, (f_move, g_move, move))

    return None