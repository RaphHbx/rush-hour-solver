import matplotlib.pyplot as plt

def h_0(state):
  """
  Heuristique nulle.
  """
  return 0

def h(state): 
  """
  Heuristique qui compte le nombre de voitures entre la voiture rouge et la sortie.
  """
  red_car = state.cars[0]
  count = 0
  for x in range(red_car.x+red_car.l,state.size):
    if state.grid[x,red_car.y] != 0:
      count += 1
  return count

def h_with_added_penalty(state):    
    """
    Heuristique qui est calculée à partir du nombre de voitures entre la voiture rouge et la sortie
    tout en vérifiant si ces voitures sont directement bloquées, dans ce cas on ajoute une pénalité.
    Cette pénalité est calculée de sorte à ce que l'heuristique reste consistante.
    """
    red_car = state.cars[0]
    count = 0

    # On observe quelles voitures bloque le chemin de la voiture rouge.
    for x in range(red_car.x + red_car.l, state.size):
        if state.grid[x, red_car.y] != 0:
            blocking_car_id = state.grid[x, red_car.y]
            blocking_car = next((car for car in state.cars if car.id == blocking_car_id), None)

            if blocking_car and blocking_car.pos == 'v':
                count += 1  # On ajoute 1 pour chacune de ces voitures.

                blocked_above = False
                blocked_below = False

                # On observe si la voiture est bloquée par une autre voiture juste au dessus d'elle.
                if state.grid[blocking_car.x, max(0,blocking_car.y-1)] != 0: #Permet de gérer le mur du haut
                    blocked_above = True
                    if blocking_car.y-1>-1: #Si c'est effectivement une autre voiture qui bloque la voiture verticale, on récupère son identifiant.
                      blocking_car_above_id = state.grid[blocking_car.x, blocking_car.y-1]
                      blocking_car_above = next((car for car in state.cars if car.id == blocking_car_above_id), None)
                      break  

                # On observe si la voiture est bloquée par une autre voiture juste au dessous d'elle.
                if state.grid[blocking_car.x, min(state.size-1, blocking_car.y + blocking_car.l)] != 0: #Permet de gérer le mur du bas 
                    blocked_below = True
                    if blocking_car.y + blocking_car.l<state.size: #Si c'est effectivement une autre voiture qui bloque la voiture verticale, on récupère son identifiant.
                      blocking_car_below_id = state.grid[blocking_car.x, blocking_car.y + blocking_car.l]
                      blocking_car_below = next((car for car in state.cars if car.id == blocking_car_below_id), None)
                      break  

                # Si la voiture est directement bloquée par le haut et le bas, on ajoute une pénalité.
                if blocked_above and blocked_below:
                    #Pénalité qui est calculée de la sorte à ce que l'heuristique soit consistante.
                    #Lorsque l'on déplace la plus longue voiture de longueur L qui bloque la voiture verticale, on libère au plus L autres voitures?
                    #Ainsi, l'heuristique varie au plus de 1 par mouvement. 
                    penalty_divisor = max(blocking_car_above.l if blocking_car_above else 0,
                                         blocking_car_below.l if blocking_car_below else 0)
                    if penalty_divisor > 0:
                         count += 1 / penalty_divisor

    return count

def h_non_consistent(state):
    """
  Heuristique qui n'est pas consistante.
  Heuristique qui est calculée à partir du nombre de voitures entre la voiture rouge et la sortie
  tout en vérifiant si ces voitures peuvent se déplacer vers le haut ou le bas d'une case.
  Si elles ne peuvent pas, on ajoute une pénalité de 1.
    """
    red_car = state.cars[0]
    count = 0

    # On observe quelles voitures bloquent le chemin de la voiture rouge.
    for x in range(red_car.x + red_car.l, state.size):
        if state.grid[x, red_car.y] != 0:
            count += 1  # On compte la voiture bloquante
            blocking_car_id = state.grid[x, red_car.y]
            blocking_car = next((car for car in state.cars if car.id == blocking_car_id), None)

            if blocking_car and blocking_car.pos == 'v':  # Si la voiture est verticale
                can_move = False

                # Vérification si la voiture verticale peut bouger
                for dy in [-1, 1]:  
                    new_y = blocking_car.y + dy
                    if 0 <= new_y < state.size - blocking_car.l + 1:  # Vérification des limites
                        # Vérification de la faisabilité du déplacement
                        path_clear = all(
                            state.grid[blocking_car.x, new_y + i] in {0, blocking_car_id} 
                            for i in range(blocking_car.l)
                        )
                        if path_clear:
                            can_move = True
                            break  

                # Ajout de la pénalité en fonction de la mobilité
                count += 1 if can_move else 2  

    return count

   