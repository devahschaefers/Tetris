from colors import Colors

class Block:
  def __init__(self, color= Colors.NO_COLOR, shapeID = 0, location = "NOT ON THE BOARD"):
    self.color = color
    self.value = color.value
    self.location = location
    self.shapeID = shapeID #0 means empty class Shape(Block):


class Shape(Block):
    def __init__(self, shape, color, name, id = "NOT ON THE BOARD"):
      Block.__init__(self, color, shapeID = id)
      self.shape = shape
      self.id = id # will be assigned when it is spawned
      self.name = name
      self.currentRotation = 0

      if (color.value != 0):
        self.isEmpty = False
      else:
        self.isEmpty = True

    def rotate(self, direction):
        pass