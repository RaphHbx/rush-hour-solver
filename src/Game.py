import matplotlib.pyplot as plt
import numpy as np
import Car
from matplotlib.colors import ListedColormap

class Game():
    def __init__(self,file=None):
      if file == None:
        self.size = 0
        self.nbrCar = 0
        self.cars = []
        self.grid = np.array([])
      else:
        file = open(file,"r")

        self.size = int(file.readline())
        self.nbrCar = int(file.readline())

        #On enregistre chaque voiture
        self.cars = []
        carInfos = file.readlines()
        for carInfo in carInfos:
          infos = carInfo.split(" ")
          self.cars.append(Car.Car(int(infos[0]),infos[1],int(infos[2]),int(infos[3])-1,int(infos[4])-1))

        #On construit la grille voiture par voiture, en vérifiant que tout va bien
        if self.updateGrid() == False:
          raise ValueError("problème de compatibilité")
        file.close()
        self.move = None
    def __str__(self):
      return f'size : {self.size}, nbrCar : {self.nbrCar}, cars : {self.cars}'

    def __repr__(self):
      return f'size : {self.size}, nbrCar : {self.nbrCar}, cars : {self.cars}'

    def __eq__(self, other):
      return self.size == other.size and self.nbrCar == other.nbrCar and self.cars == other.cars

    def __lt__(self,other):
      return self.size < other.size #On met n'importe quoi juste pour que la comparaison existe

    def __hash__(self) -> int:
      #On ne "retient" que les voitures, car le reste ne peut pas changer.
      t = [car.toTuple() for car in self.cars]
      t = tuple(t)
      return hash(t)

    def show(self):
      # Génération d'une colormap avec "nbrCar" couleurs uniques
      base_cmap = plt.get_cmap("twilight", self.nbrCar)
      colors = base_cmap(np.arange(self.nbrCar))  # Génération de couleurs

      # Remplace 0 par blanc et 1 par rouge, tout le reste garde une couleur unique
      colors[0] = [1, 1, 1, 1]  # Blanc pour 0
      colors[1] = [1, 0, 0, 1]  # Rouge pour 1

      # Création de la colormap personnalisée
      cmap = ListedColormap(colors)


      plt.imshow(self.grid.T,cmap=cmap)
      for car in self.cars:
        plt.text(car.x,car.y,car.id)

    def updateGrid(self):
      self.grid = np.array([[0 for i in range(self.size)] for j in range(self.size)])
      for car in self.cars:
        if car.pos == 'h':
          for i in range(car.l):
            if self.grid[car.x+i][car.y] != 0:
              return False
            self.grid[car.x+i][car.y] = car.id
        elif car.pos == 'v':
            for i in range(car.l):
              if self.grid[car.x][car.y+i] != 0:
                return False
              self.grid[car.x][car.y+i] = car.id
      return True

    def free(self):
      return np.transpose(np.where(self.grid==0))

    def freeLine(self,ord):
      return self.free()[self.free()[:,1] == ord,:]

    def freeColumn(self, abs):
      return self.free()[self.free()[:,0] == abs,:]

    def isFinished(self): #Permet de vérifier si la voiture rouge est arrivée à la sortie ou non
      return ((self.cars[0].pos == 'h'
               and self.cars[0].x+self.cars[0].l == self.size)
            or (self.cars[0].pos == 'v'
               and self.cars[0].y+self.cars[0].l == self.size))


    def copy(self,movedCar):
      new_game = Game()
      new_game.size = self.size
      new_game.nbrCar = self.nbrCar
      new_game.cars = []
      for car in self.cars:
        if car.id != movedCar.id:
          new_game.cars.append(Car.Car(car.id,car.pos,car.l,car.x,car.y))
        else:
          new_game.move = (self,movedCar)
          new_game.cars.append(movedCar)
      new_game.updateGrid()
      return new_game

