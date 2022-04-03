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
    self.shapeID = shapeID #0 means empty class Shape(Block): from block import Block
    
class Shape(Block):
    def __init__(self, shape, color, name, id = "NOT ON THE BOARD"):
      Block.__init__(self, color, shapeID = id)
      self.shape = shape
      self.id = id # will be assigned when it is spawned
      self.name = name
      self.currentRotation = 0
      self.yLength = len(self.shape[self.currentRotation])
      self.xLength = len(self.shape[self.currentRotation][0])

      if (color.value != 0):
        self.isEmpty = False
      else:
        self.isEmpty = True

    def rotate(self, direction):
        pass