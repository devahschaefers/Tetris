import pygame
from colors import Colors
import os

def printBoard(board):

    width = len(board[0])
    for j in range(-1, -width - 1, -1):
        for i in board:
            print(i[j].color, end=" ")
        print("")

class Block:
  def __init__(self, color):
    self.color = color
    
class Shape(Block):
    def __init__(self, shape, color):
        Block.__init__(self, color)
        self.shape = shape

    def rotate(self, direction):
        pass


rawShapes = {
    "oBlock": [
               [[Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(0)], 
                [Block(0), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(0)]],
      
               [[Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(0)], 
                [Block(0), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(0)]],
      
               [[Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(0)], 
                [Block(0), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(0)]],
      
               [[Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(0)], 
                [Block(0), Block(Colors.YELLOW), Block(Colors.YELLOW), Block(0)]]
              ],
    "iBlock": [
               [[Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(0), Block(0), Block(0)], 
                [Block(Colors.RED), Block(Colors.RED), Block(Colors.RED), Block(Colors.RED)], 
                [Block(0), Block(0), Block(0), Block(0)]],
      
               [[Block(0), Block(0), Block(Colors.RED), Block(0)], 
                [Block(0), Block(0), Block(Colors.RED), Block(0)], 
                [Block(0), Block(0), Block(Colors.RED), Block(0)], 
                [Block(0), Block(0), Block(Colors.RED), Block(0)]],
      
               [[Block(0), Block(0), Block(0), Block(0)], 
                [Block(0), Block(0), Block(0), Block(0)], 
                [Block(Colors.RED), Block(Colors.RED), Block(Colors.RED), Block(Colors.RED)], 
                [Block(0), Block(0), Block(0), Block(0)]],
      
               [[Block(0), Block(Colors.RED), Block(0), Block(0)], 
                [Block(0), Block(Colors.RED), Block(0), Block(0)], 
                [Block(0), Block(Colors.RED), Block(0), Block(0)], 
                [Block(0), Block(Colors.RED), Block(0), Block(0)]]
              ],
    "jBlock": [
                [[Block(0), Block(0), Block(0), Block(0)], 
                 [Block(0), Block(0), Block(0), Block(0)], 
                 [Block(Colors.ORANGE), Block(0), Block(0), Block(0)], 
                 [Block(Colors.ORANGE), Block(Colors.ORANGE), Block(Colors.ORANGE), Block(0)]],
      
                [[Block(0), Block(0), Block(0), Block(0)],
                 [Block(0), Block(0), Block(Colors.ORANGE), Block(Colors.ORANGE)], 
                 [Block(0), Block(0), Block(Colors.ORANGE), Block(0)], 
                 [Block(0), Block(0), Block(Colors.ORANGE), Block(0)]],
      
                [[Block(0), Block(0), Block(0), Block(0)], 
                 [Block(0), Block(0), Block(0), Block(0)], 
                 [Block(0), Block(Colors.ORANGE), Block(Colors.ORANGE), Block(Colors.ORANGE)], 
                 [Block(0), Block(0), Block(0), Block(Colors.ORANGE)]],
      
                [[Block(0), Block(0), Block(0), Block(0)],
                 [Block(0), Block(Colors.ORANGE), Block(0), Block(0)], 
                 [Block(0), Block(Colors.ORANGE), Block(0), Block(0)], 
                 [Block(Colors.ORANGE), Block(Colors.ORANGE), Block(0), Block(0)]],
              ],
    "lBlock": [
                 [[Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(0), Block(0), Block(0)],
                  [Block(0), Block(0), Block(0), Block(Colors.BLUE)],
                  [Block(0), Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.BLUE)]],
      
                 [[Block(0), Block(0), Block(0), Block(0)],
                  [Block(0), Block(0), Block(Colors.BLUE), Block(0)], 
                  [Block(0), Block(0), Block(Colors.BLUE), Block(0)], 
                  [Block(0), Block(0), Block(Colors.BLUE), Block(Colors.BLUE)]],
      
                 [[Block(0), Block(0), Block(0), Block(0)],
                  [Block(0), Block(0), Block(0), Block(0)],
                  [Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.BLUE), Block(0)], 
                  [Block(Colors.BLUE), Block(0), Block(0), Block(0)]],
      
                 [[Block(0), Block(0), Block(0), Block(0)],
                  [Block(Colors.BLUE), Block(Colors.BLUE), Block(0), Block(0)], 
                  [Block(0), Block(Colors.BLUE), Block(0), Block(0)], 
                  [Block(0), Block(Colors.BLUE), Block(0), Block(0)]]
              ],
    "sBlock": [
                 [[Block(0), Block(0), Block(0), Block(0)],
                  [Block(0), Block(0), Block(0), Block(0)],
                  [Block(0), Block(Colors.PURPLE), Block(Colors.PURPLE), Block(0)],
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), Block(0), Block(0)]],
      
                 [[Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(Colors.PURPLE), Block(0), Block(0)], 
                  [Block(0), Block(Colors.PURPLE), Block(Colors.PURPLE), Block(0)], 
                  [Block(0), Block(0), Block(Colors.PURPLE), Block(0)]],
      
                 [[Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(Colors.PURPLE), Block(Colors.PURPLE), Block(0)], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), Block(0), Block(0)]],
      
                 [[Block(0), Block(0), Block(0), Block(0)],
                  [Block(Colors.PURPLE), Block(0), Block(0), Block(0)], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), Block(0), Block(0)],
                  [Block(0), Block(Colors.PURPLE), Block(0), Block(0)]]
              ],
    "zBlock": [
                [
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(0), Block(0), Block(0)],
                  [Block(0), Block(Colors.GREEN), Block(Colors.GREEN), Block(0)], 
                  [Block(Colors.GREEN), Block(Colors.GREEN), Block(0), Block(0)]
                ],
                [
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(Colors.GREEN), Block(0), Block(0)],
                  [Block(0), Block(Colors.GREEN), Block(Colors.GREEN), Block(0)], 
                  [Block(0), Block(0), Block(Colors.GREEN), Block(0)]
                ],
                [
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(0), Block(0), Block(0)],
                  [Block(0), Block(Colors.GREEN), Block(Colors.GREEN), Block(0)], 
                  [Block(Colors.GREEN), Block(Colors.GREEN), Block(0), Block(0)]
                ],
                [
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(Colors.GREEN), Block(0), Block(0), Block(0)],
                  [Block(Colors.GREEN), Block(Colors.GREEN), Block(0), Block(0)], 
                  [Block(0), Block(Colors.GREEN), Block(0), Block(0)]
                ],
              ],
    "tBlock": [
                [
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(Colors.CYAN), Block(0), Block(0)], 
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.CYAN), Block(0)]
                ],
                [
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(Colors.CYAN), Block(0), Block(0)], 
                  [Block(0), Block(Colors.CYAN), Block(Colors.CYAN), Block(0)], 
                  [Block(0), Block(Colors.CYAN), Block(0), Block(0)]
                ],
                [
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.CYAN), Block(0)], 
                  [Block(0), Block(Colors.CYAN), Block(0), Block(0)]
                ],
                [
                  [Block(0), Block(0), Block(0), Block(0)], 
                  [Block(0), Block(Colors.CYAN), Block(0), Block(0)], 
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(0), Block(0)], 
                  [Block(0), Block(Colors.CYAN), Block(0), Block(0)]
                ]
              ]
}
shapes = [
    Shape(rawShapes["oBlock"], Colors.YELLOW),
    Shape(rawShapes["iBlock"], Colors.CYAN),
    Shape(rawShapes["jBlock"], Colors.BLUE),
    Shape(rawShapes["lBlock"], Colors.ORANGE),
    Shape(rawShapes["sBlock"], Colors.GREEN),
    Shape(rawShapes["zBlock"], Colors.RED),
    Shape(rawShapes['tBlock'], Colors.PURPLE)
]


class Game():
    def __init__(self, width, height):
        self.board = []
        self.width = width
        self.height = height
    #-----set up board -------------
        row = []
        for i in range(self.width):
            for j in range(self.height):
                row.append(Block(0))
            self.board.append(row.copy())
            row.clear()

    #---------------------------------
    
    def drawDrawShapeAtLocation(self):
      pass
    

    def setupgame(self):
        pass

    def draw(self):
        pass


game = Game(10, 40)
printBoard(game.board)