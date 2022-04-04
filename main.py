'''
ERRORS

-200 = IndexError
-100 = Hit an object

'''

from turtle import shape
import pygame
import random
import copy, time, os
from classes import Colors, Shape, Block
import mShapes
from mShapes import shapes

pygame.init()
pygame.display.set_caption('Tetris')


#--------------------------CONSTANTS--------------------------
SPRITE_SIZE = 32
#colors
GRAY = (128, 128, 128)
#sprites
img_Blue = pygame.transform.scale(pygame.image.load("Sprites/Blue.png"), [32, 32])
img_Cyan = pygame.transform.scale(pygame.image.load("Sprites/Cyan.png"), [32, 32])
img_Green = pygame.transform.scale(pygame.image.load("Sprites/Green.png"), [32, 32])
img_Orange = pygame.transform.scale(pygame.image.load("Sprites/Orange.png"), [32, 32])
img_Purple = pygame.transform.scale(pygame.image.load("Sprites/Purple.png"), [32, 32])
img_Red = pygame.transform.scale(pygame.image.load("Sprites/Red.png"), [32, 32])
img_White = pygame.transform.scale(pygame.image.load("Sprites/White.png"), [32, 32])
img_Yellow = pygame.transform.scale(pygame.image.load("Sprites/Yellow.png"), [32, 32])
#events
SECONDPASSED = pygame.USEREVENT + 1

#other
PRINT_PERMANENT = ""

def coordinates_to_pixel_loc(postion: list):  # maybe think of a better name
    postion = list(postion)
    postion[0] = postion[0] * SPRITE_SIZE
    postion[1] = postion[1] * SPRITE_SIZE
    return (postion[0], postion[1])

def printShape(shape: Shape) -> None:
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
    for j in range(0, width - 1): #walks throught the board from right to left 
        for i in board: #walks through the each row in the board
            print(i[j].color.value, end=" ")
        print("")

    print("")
class Game():

  def __init__(self, width=10, height=20):
      self.board = []
      self.width = width
      self.height = height
      self.numberOfTetrominosSpawned = 0
      self.currentTetrominoFalling = {"shape": Shape(0, 0, 0, 0), "id": -1}
      self.size = (width * SPRITE_SIZE + 2, height * SPRITE_SIZE)
      self.screen = pygame.display.set_mode(self.size)
      self.allShapesCreated = [] #list of all Shape Objects
      pygame.time.set_timer(SECONDPASSED, 1000)
  #-----set up board -------------
      row = []
      for i in range(self.width):
          for j in range(self.height):
              row.append(Block(Colors.NO_COLOR, location = [i, j]))
          self.board.append(row.copy())
          row.clear()
  #---------------------------------
  def _removeID(self, ID):
    for colum in self.board:
      for mBlock in colum:
        if mBlock.shapeID == ID: self.board[mBlock.location[0]][mBlock.location[1]] = Block()
  
  def drawShapeAtLocation(self, location: list, blockID: int) -> int:
    #create copy of the board which will replace the actual board if the function doesnt encounter errors
    board = copy.deepcopy(self.board)
    Tetromino: Shape = self.currentTetrominoFalling["shape"]

    j = 0 #x
    i = 0 #y
    
    for y in range(location[1], location[1] + Tetromino.yLength):
      for x in range(location[0], location[0]+ Tetromino.xLength):
        ignoreCurrentBlock = False

        try: #incase we go outside of the bounds
          if self.board[x][y].color != Colors.NO_COLOR: #check to make sure it doesnt draw on an occupied space
            return -100
          if Tetromino.shape[Tetromino.currentRotation][j][i].value == 0: #will wont draw over the board if the value in the shape is NO_COLOR
            ignoreCurrentBlock = True
          if ignoreCurrentBlock == False:
              Block = Tetromino.shape[Tetromino.currentRotation][j][i]
              Block.shapeID = blockID
              Block.location = [x, y]
              board[x][y] = Block
        except IndexError: #return -200 if we go outside of the bounds
          print("Draw Shape Function went out of range of the board at:", f"[{x}, {y}]")
          return -200

        i += 1
      j += 1
      i = 0
    self.currentTetrominoFalling["shape"].lastPositionDrawn = location
    del Tetromino
    self.board = board
    return 0
  
  def draw(self):
    for colum in self.board:
      for Block in colum:

        if Block.color == Colors.CYAN:
          self.screen.blit(img_Cyan, coordinates_to_pixel_loc(Block.location))
        if Block.color == Colors.BLUE:
          self.screen.blit(img_Blue, coordinates_to_pixel_loc(Block.location))
        if Block.color == Colors.ORANGE:
          self.screen.blit(img_Orange, coordinates_to_pixel_loc(Block.location))
        if Block.color == Colors.YELLOW:
          self.screen.blit(img_Yellow, coordinates_to_pixel_loc(Block.location))
        if Block.color == Colors.RED:
          self.screen.blit(img_Red, coordinates_to_pixel_loc(Block.location))
        if Block.color == Colors.PURPLE:
          self.screen.blit(img_Purple, coordinates_to_pixel_loc(Block.location))
        if Block.color == Colors.GREEN:
          self.screen.blit(img_Green, coordinates_to_pixel_loc(Block.location))

  def spawnTetromino(self, Tetromino=random.choice(shapes)) -> str:
    self.numberOfTetrominosSpawned += 1
    Tetromino.id = self.numberOfTetrominosSpawned
    self.currentTetrominoFalling = {"shape": Tetromino, "id": Tetromino.id}
    print(f"spawning {Tetromino.name}")
    self.drawShapeAtLocation([(self.width // 2) - 2, 0], Tetromino.id)
    self.currentTetrominoFalling["shape"].lastPositionDrawn = [(self.width // 2) - 2, 0]
    return Tetromino.name
  
  def moveTetromino(self, dX: int, dY: int): #delta x and delta y; Tetromino to move is like current Tetromino Falling property except it is not bound to the current Tetromino falling, i.e it can be any Tetromino
    if self.currentTetrominoFalling["shape"] == None or self.currentTetrominoFalling["id"] == None: 
      print("Move Tetromino Function tried to move current Falling Tetromino however it is a none type")
      return -1
    TetObj: Shape = self.currentTetrominoFalling['shape']
    TetID: int = self.currentTetrominoFalling['id']
    lastPositionDrawn = TetObj.lastPositionDrawn
    self._removeID(TetID)
    self.drawShapeAtLocation([lastPositionDrawn[0] + dX, lastPositionDrawn[1] + dY], TetID)
game = Game()


running = True
dx, dy = 0, 0
game.spawnTetromino()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False

    if event.type == pygame.KEYDOWN:            
        if event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_DOWN:
            game.moveTetromino(0, 1)
        if event.key == pygame.K_RIGHT:
            game.moveTetromino(1, 0)
        if event.key == pygame.K_LEFT:
            game.moveTetromino(-1, 0)
      

    
    if event.type == SECONDPASSED:
      game.moveTetromino(0, 1)

    game.screen.fill(GRAY)
    game.draw()
    pygame.display.flip()