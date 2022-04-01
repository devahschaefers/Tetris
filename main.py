import pygame
from colors import Colors
import random
import os
import pathlib
import copy
import time


PATH = pathlib.Path().absolute()


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
    print("Printing Board:\n")
    width = len(board[0])
    for j in range(-1, -width - 1, -1):
        for i in board:
            print(i[j].color.value, end=" ")
        print("")

class Block:
  def __init__(self, color, location = "s"):
    self.color = color
    self.value = color.value
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
      #create copy of the board which will replace the actual board if the fuction doesnt encounter errors
      board = copy.deepcopy(self.board)
#assumes tetormino is a shape object
      if Tetromino == None:
        Tetromino = self.currentTetrominoFalling[0]
      y_lengthOfTetromino = len(Tetromino.shape[Tetromino.currentRotation])
      x_lengthOfTetromino = len(Tetromino.shape[Tetromino.currentRotation][0])
      j = 0 #x
      i = 0 #y
     
      for y in range(location[1], location[1] - y_lengthOfTetromino, -1):
        for x in range(location[0], location[0]+ x_lengthOfTetromino):
          ignoreCurrentBlock = False
          if self.board[x][y].color != Colors.NO_COLOR:
            return -1
          if Tetromino.shape[Tetromino.currentRotation][j][i].value == 0:
            ignoreCurrentBlock = True
          if ignoreCurrentBlock == False:
            board[x][y] = Tetromino.shape[Tetromino.currentRotation][j][i]
          i += 1
        j += 1
        i = 0
      self.board = board
    
    def draw(self):
        pass
    
    def spawnTetromino(self, Tetromino=random.choice(shapes)):
      self.numberOfTetrominosSpawned += 1
      Tetromino.id = self.numberOfTetrominosSpawned
      self.currentTetrominoFalling = [Tetromino, Tetromino.id]
      self.drawDrawShapeAtLocation([3, 39], Tetromino)
      return Tetromino.name
      

game = Game()


  
if game.currentTetrominoFalling == None:
    spawmedTetromino = game.spawnTetromino()
    print("Spawned Tetromino:", spawmedTetromino)
print(game.currentTetrominoFalling[0].name)
printBoard(game.board)
time.sleep(0.5)
# os.system("clear")