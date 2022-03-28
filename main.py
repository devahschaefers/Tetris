import pygame
from colors import Colors
import random
import copy


def printShape(shape):
  length_x = len(shape.shape[shape.currentRotation][0])
  length_y = len(shape.shape[shape.currentRotation])
  print("\nPrinting:", shape.name)
  
  for y in range(0, length_y):
    for x in range(0, length_x):
      print(shape.shape[shape.currentRotation][y][x].color.value, end = ' ')      
    print('')
  print('\n')
  
def printBoard(board):
    width = len(board[0])
    for j in range(-1, -width - 1, -1):
        for i in board:
            print(i[j].color.value, end=" ")
        print("")

class Block:
  def __init__(self, color, location = "s"):
    self.color = color
    self.location = location
    
class Shape(Block):
    def __init__(self, shape, color, name):
      Block.__init__(self, color)
      self.shape = shape
      self.id = 0 # will be assigned when it is spawned
      self.name = name
      self.currentRotation = 0
      
      if (color.value != 0):
        self.isEmpty = False
      else:
        self.isEmpty = True

    def rotate(self, direction):
        pass


rawShapes = {
    "oBlock": [
               [ 
                [Block(Colors.NO_COLOR), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(Colors.NO_COLOR)], 
                [Block(Colors.NO_COLOR), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(Colors.NO_COLOR)]],
      
               [ 
                [Block(Colors.NO_COLOR), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(Colors.NO_COLOR)], 
                [Block(Colors.NO_COLOR), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(Colors.NO_COLOR)]],
      
               [ 
                [Block(Colors.NO_COLOR), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(Colors.NO_COLOR)], 
                [Block(Colors.NO_COLOR), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(Colors.NO_COLOR)]],
      
               [ 
                [Block(Colors.NO_COLOR), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(Colors.NO_COLOR)], 
                [Block(Colors.NO_COLOR), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(Colors.NO_COLOR)]]
              ],
    "iBlock": [ 
                [
                  [Block(Colors.RED), Block(Colors.RED), Block(Colors.RED), Block(Colors.RED)]
                ],
      
               [
                [Block(Colors.RED)], 
                [Block(Colors.RED)], 
                [Block(Colors.RED)], 
                [Block(Colors.RED)]
               ],
      
              [
                [Block(Colors.NO_COLOR),Block(Colors.NO_COLOR),Block(Colors.NO_COLOR),Block(Colors.NO_COLOR)]
              ],
              [
                [Block(Colors.RED), Block(Colors.RED), Block(Colors.RED), Block(Colors.RED)]
              ],
      
              [
                [Block(Colors.NO_COLOR), Block(Colors.RED)], 
                [Block(Colors.NO_COLOR), Block(Colors.RED)], 
                [Block(Colors.NO_COLOR), Block(Colors.RED)], 
                [Block(Colors.NO_COLOR), Block(Colors.RED)]
              ]
            ],
    "jBlock": [
                [
                 [Block(Colors.ORANGE), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)], 
                 [Block(Colors.ORANGE), Block(Colors.ORANGE), Block(Colors.ORANGE)]
                ],
      
                [
                 [Block(Colors.NO_COLOR), Block(Colors.ORANGE), Block(Colors.ORANGE)], 
                 [Block(Colors.NO_COLOR), Block(Colors.ORANGE), Block(Colors.NO_COLOR)], 
                 [Block(Colors.NO_COLOR), Block(Colors.ORANGE), Block(Colors.NO_COLOR)]
                ],
      
                [  
                 [Block(Colors.ORANGE),   Block(Colors.ORANGE),   Block(Colors.ORANGE)], 
                 [Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.ORANGE)]
                ],
                [
                 [Block(Colors.NO_COLOR), Block(Colors.ORANGE), Block(Colors.NO_COLOR)], 
                 [Block(Colors.NO_COLOR), Block(Colors.ORANGE), Block(Colors.NO_COLOR)], 
                 [Block(Colors.ORANGE), Block(Colors.ORANGE), Block(Colors.NO_COLOR)]
                ]
              ],
    "lBlock": [
                 [
                  [Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.BLUE)],
                  [Block(Colors.NO_COLOR), Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.BLUE)]
                 ],
      
                 [
                  [Block(Colors.NO_COLOR), Block(Colors.BLUE), Block(Colors.NO_COLOR)], 
                  [Block(Colors.NO_COLOR), Block(Colors.BLUE), Block(Colors.NO_COLOR)], 
                  [Block(Colors.NO_COLOR), Block(Colors.BLUE), Block(Colors.BLUE)]
                 ],
      
                 [
                  [Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.NO_COLOR)], 
                  [Block(Colors.BLUE), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)]
                 ],
      
                 [
                  [Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.NO_COLOR)],  
                  [Block(Colors.NO_COLOR), Block(Colors.BLUE), Block(Colors.NO_COLOR)],  
                  [Block(Colors.NO_COLOR), Block(Colors.BLUE), Block(Colors.NO_COLOR)]   
                  
                ]
              ],
    "sBlock": [
                 [
                  [Block(Colors.NO_COLOR), Block(Colors.PURPLE), Block(Colors.PURPLE)],
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), Block(Colors.NO_COLOR)]
                 ],
      
                 [ 
                  [Block(Colors.NO_COLOR), Block(Colors.PURPLE), Block(Colors.NO_COLOR)], 
                  [Block(Colors.NO_COLOR), Block(Colors.PURPLE), Block(Colors.PURPLE)], 
                  [Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.PURPLE)]
                 ],
      
                 [ 
                  [Block(Colors.NO_COLOR), Block(Colors.PURPLE), Block(Colors.PURPLE)], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), Block(Colors.NO_COLOR)]
                 ],
      
                 [
                  [Block(Colors.PURPLE), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR) ], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), Block(Colors.NO_COLOR) ],
                  [Block(Colors.NO_COLOR), Block(Colors.PURPLE), Block(Colors.NO_COLOR)]
                ],
              ],
    "zBlock": [
                [
                  [Block(Colors.NO_COLOR), Block(Colors.GREEN), Block(Colors.GREEN)], 
                  [Block(Colors.GREEN), Block(Colors.GREEN), Block(Colors.NO_COLOR)]
                ],
                [ 
                  [Block(Colors.GREEN), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)],
                  [Block(Colors.GREEN), Block(Colors.GREEN), Block(Colors.NO_COLOR)], 
                  [Block(Colors.NO_COLOR), Block(Colors.GREEN), Block(Colors.NO_COLOR)]
                ],
                [ 
                  [Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)],
                  [Block(Colors.NO_COLOR), Block(Colors.GREEN), Block(Colors.GREEN)], 
                  [Block(Colors.GREEN), Block(Colors.GREEN), Block(Colors.NO_COLOR)]
                ],
                [ 
                  [Block(Colors.GREEN), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)],
                  [Block(Colors.GREEN), Block(Colors.GREEN), Block(Colors.NO_COLOR)],
                  [Block(Colors.NO_COLOR), Block(Colors.GREEN), Block(Colors.NO_COLOR)]
                ]
              ],
    "tBlock": [
                [ 
                  [Block(Colors.NO_COLOR), Block(Colors.CYAN), Block(Colors.NO_COLOR)], 
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.CYAN)]
                ],
                [
                  [ Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)], 
                  [ Block(Colors.CYAN), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)], 
                  [ Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.NO_COLOR)], 
                  [ Block(Colors.CYAN), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)]
                ],
                [
                  [Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)], 
                  [Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)], 
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.NO_COLOR)], 
                  [Block(Colors.NO_COLOR), Block(Colors.CYAN), Block(Colors.NO_COLOR), Block(Colors.NO_COLOR)]
                ],
                [
                  [Block(Colors.NO_COLOR), Block(Colors.CYAN), Block(Colors.NO_COLOR)],
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.NO_COLOR)],
                  [Block(Colors.NO_COLOR), Block(Colors.CYAN), Block(Colors.NO_COLOR)]
                ]
              ]
}
shapes = [
    Shape(rawShapes["oBlock"], Colors.YELLOW, "oBlock"),
    Shape(rawShapes["iBlock"], Colors.CYAN, "iBlock"),
    Shape(rawShapes["jBlock"], Colors.BLUE, "jBlock"),
    Shape(rawShapes["lBlock"], Colors.ORANGE, "lBlock"),
    Shape(rawShapes["sBlock"], Colors.GREEN, "sBlock"),
    Shape(rawShapes["zBlock"], Colors.RED, "zBlock"),
    Shape(rawShapes['tBlock'], Colors.PURPLE, "tBlock")
]


class Game():

    def p_findtopRightofShape(shape):
      pass
    def __init__(self, width=10, height=40):
        self.board = []
        self.width = width
        self.height = height
        self.numberOfTetrominosSpawned = 0
        self.currentTetrominoFalling = None
    #-----set up board -------------
        row = []
        for i in range(self.width):
            for j in range(self.height):
                row.append(Block(Colors.NO_COLOR, [i, j]))
            self.board.append(row.copy())
            row.clear()

    #---------------------------------
    
    def drawDrawShapeAtLocation(self, location, Tetromino = None):
      if Tetromino == None:
        Tetromino = self.currentTetrominoFalling[0]
      printShape(Tetromino)
      y_lengthOfTetromino = len(Tetromino.shape[Tetromino.currentRotation]) - 1
      x_lengthOfTetromino = len(Tetromino.shape[Tetromino.currentRotation])
      print("y length:", y_lengthOfTetromino)
      j = 0 #x
      i = 0 #y
      for y in range(location[1], location[1]+len(Tetromino.shape[Tetromino.currentRotation])):
        for x in range(location[0], location[0]+len(Tetromino.shape[Tetromino.currentRotation][0])):
          print(i, j)
          self.board[x][y] = Tetromino.shape[Tetromino.currentRotation][i][j]
          i += 1
          
        print('');
        j += 1
        i = 0
    
    def setupgame(self):
        pass

    def draw(self):
        pass
    def drawTetrominoAt(location=[5,40], Tetrino = copy.deepcopy(random.choice(shapes))):
      pass
    
    def spawnTetromino(self, Tetromino=random.choice(shapes)):
      self.numberOfTetrominosSpawned += 1
      Tetromino.id = self.numberOfTetrominosSpawned
      self.currentTetrominoFalling = [Tetromino, Tetromino.id]
      

game = Game()

game.spawnTetromino()
game.drawDrawShapeAtLocation([3, 33], shapes[2])
print(game.board[3][36])
printBoard(game.board)