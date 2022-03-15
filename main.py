import pygame
from colors import Colors


def printBoard(board):
    width = len(board[0])
    for j in range(-1, -width - 1, -1):
        for i in board:
            print(i[j], end=" ")
        print("")


class Shape():
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def rotate(self, direction):
        pass


rawShapes = {
    "oBlock": [
               [[0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [0, 1, 1, 0], 
                [0, 1, 1, 0]],
      
               [[0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [0, 1, 1, 0], 
                [0, 1, 1, 0]],
      
               [[0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [0, 1, 1, 0], 
                [0, 1, 1, 0]],
      
               [[0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [0, 1, 1, 0], 
                [0, 1, 1, 0]]
              ],
    "iBlock": [
               [[0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [1, 1, 1, 1], 
                [0, 0, 0, 0]],
      
               [[0, 0, 1, 0], 
                [0, 0, 1, 0], 
                [0, 0, 1, 0], 
                [0, 0, 1, 0]],
      
               [[0, 0, 0, 0], 
                [0, 0, 0, 0], 
                [1, 1, 1, 1], 
                [0, 0, 0, 0]],
      
               [[0, 1, 0, 0], 
                [0, 1, 0, 0], 
                [0, 1, 0, 0], 
                [0, 1, 0, 0]]
              ],
    "jBlock": [
                [[0, 0, 0, 0], 
                 [0, 0, 0, 0], 
                 [1, 0, 0, 0], 
                 [1, 1, 1, 0]],
      
                [[0, 0, 0, 0],
                 [0, 0, 1, 1], 
                 [0, 0, 1, 0], 
                 [0, 0, 1, 0]],
      
                [[0, 0, 0, 0], 
                 [0, 0, 0, 0], 
                 [0, 1, 1, 1], 
                 [0, 0, 0, 1]],
      
                [[0, 0, 0, 0],
                 [0, 1, 0, 0], 
                 [0, 1, 0, 0], 
                 [1, 1, 0, 0]],
              ],
    "lBlock": [
                 [[0, 0, 0, 0], 
                  [0, 0, 0, 0],
                  [0, 0, 0, 1],
                  [0, 1, 1, 1]],
      
                 [[0, 0, 0, 0],
                  [0, 0, 1, 0], 
                  [0, 0, 1, 0], 
                  [0, 0, 1, 1]],
      
                 [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [1, 1, 1, 0], 
                  [1, 0, 0, 0]],
      
                 [[0, 0, 0, 0],
                  [1, 1, 0, 0], 
                  [0, 1, 0, 0], 
                  [0, 1, 0, 0]]
              ],
    "sBlock": [
                 [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 1, 1, 0],
                  [1, 1, 0, 0]],
      
                 [[0, 0, 0, 0], 
                  [0, 1, 0, 0], 
                  [0, 1, 1, 0], 
                  [0, 0, 1, 0]],
      
                 [[0, 0, 0, 0], 
                  [0, 0, 0, 0], 
                  [0, 1, 1, 0], 
                  [1, 1, 0, 0]],
      
                 [[0, 0, 0, 0],
                  [1, 0, 0, 0], 
                  [1, 1, 0, 0],
                  [0, 1, 0, 0]]
              ],
    "zBlock": [
                [
                  [0, 0, 0, 0], 
                  [0, 0, 0, 0],
                  [0, 1, 1, 0], 
                  [1, 1, 0, 0]
                ],
                [
                  [0, 0, 0, 0], 
                  [0, 1, 0, 0],
                  [0, 1, 1, 0], 
                  [0, 0, 1, 0]
                ],
                [
                  [0, 0, 0, 0], 
                  [0, 0, 0, 0],
                  [0, 1, 1, 0], 
                  [1, 1, 0, 0]
                ],
                [
                  [0, 0, 0, 0], 
                  [1, 0, 0, 0],
                  [1, 1, 0, 0], 
                  [0, 1, 0, 0]
                ],
              ],
    "tBlock": [
                  [0, 0, 0, 0], 
                  [0, 0, 0, 0], 
                  [0, 0, 1, 0], 
                  [0, 1, 1, 1]
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

    def drawDrawShapeAtLocation(self):
        #-----set up board -------------
        row = []
        num = 0
        for i in range(self.width):
            for j in range(self.height):
                row.append(num)
            self.board.append(row.copy())
            row.clear()

    #---------------------------------

    def setupgame(self):
        pass

    def draw(self):
        pass


game = Game(10, 40)
printBoard(game.board)
