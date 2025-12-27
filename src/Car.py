class Car():
    def __init__(self,id,pos,l,x,y):
      self.id = id
      self.x = x
      self.y = y
      self.l = l
      self.pos = pos

    def toTuple(self):
      return (self.id,self.pos,self.l,self.x,self.y)

    def __hash__(self) -> int:
      return hash(self.toTuple())

    def __str__(self):
      return f'[id : {self.id}, x : {self.x}, y : {self.y}, l: {self.l}, pos : {self.pos}]'

    def __repr__(self):
      return f'[id : {self.id}, x : {self.x}, y : {self.y}, l: {self.l}, pos : {self.pos}]'

    def __eq__(self, other):
      return self.id == other.id and self.x == other.x and self.y == other.y and self.l == other.l and self.pos == other.pos