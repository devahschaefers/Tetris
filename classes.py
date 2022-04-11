from enum import Enum
class Colors(Enum):
  CYAN = 1
  BLUE = 2
  ORANGE = 3
  YELLOW = 4
  RED = 5
  PURPLE = 6
  GREEN = 7
  NO_COLOR = 0
class Block:
  def __init__(self, color= Colors.NO_COLOR, shapeID = 0, location = "NOT ON THE BOARD"):
    self.color = color
    self.value = color.value
    self.location = location
    self.shapeID = shapeID #0 means empty class
    
class Shape(Block):
    def __init__(self, shape = [], color = Colors.NO_COLOR, name = "Not Initialized", id = "NOT ON THE BOARD"):
      Block.__init__(self, color, shapeID = id)
      self.shape : list = shape
      self.id : int = id # will be assigned when it is spawned
      self.name : str= name
      self.currentRotation : int = 0
      self.lastPositionDrawn : list = [-100, -100]

      if (color.value != 0):
        self.isEmpty = False
      else:
        self.isEmpty = True

    def yLength(self) -> int: return len(self.shape[self.currentRotation])
    def xLength(self) -> int: return len(self.shape[self.currentRotation][0])
    
    def rotate(self):
        if self.currentRotation < 3:
          self.currentRotation += 1
        else:
          self.currentRotation = 0
