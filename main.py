'''
ERRORS

-200 = IndexError
-100 = Hit an object
 100 = Hit bottom
'''

from turtle import shape
import pygame
import random
import copy, time, os, sys
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
SPAWN_TETROMINO = pygame.USEREVENT + 2

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
  del shape
  
def printBoard(board):
    print("Printing Board:\n")
    width = len(board[0])
    for j in range(0, width - 1): #walks throughout the board from right to left 
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
      self.currentTetrominoFalling = {"shapeObj": mShapes.DEFAULT_RAW_SHAPE, "id": -1}
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
    #create copy of the board which will replace the actual board if the function doesn't encounter errors
    board = copy.deepcopy(self.board)
    Tetromino: Shape = self.currentTetrominoFalling["shapeObj"]

    j = 0 #x
    i = 0 #y
    printShape(Tetromino)
    for y in range(location[1], location[1] + Tetromino.yLength()):
      for x in range(location[0], location[0]+ Tetromino.xLength()):
        ignoreCurrentBlock = False
        if y > self.height - 1:
          print("hit the bottom at", y)
          print(f"returned 100 at {x}, {y}")
          return 100
        if x >= 0 and x < self.width: #incase we go outside of the bounds x bounds
          if self.board[x][y].color != Colors.NO_COLOR and not Tetromino.shape[Tetromino.currentRotation][j][i].value == 0: #check to make sure it doesn't draw on an occupied space
            return -100
          print("went out of range at", j, i)
          if Tetromino.shape[Tetromino.currentRotation][j][i].value == 0: #will wont draw over the board if the value in the shape is NO_COLOR
            ignoreCurrentBlock = True
          if ignoreCurrentBlock == False:
              Block = Tetromino.shape[Tetromino.currentRotation][j][i]
              Block.shapeID = blockID
              Block.location = [x, y]
              board[x][y] = Block
        else: #return -200 if we go outside of the bounds
          print("Draw Shape Function went out of range of the board at:", f"[{x}, {y}]")
          return -200

        i += 1
      j += 1
      i = 0
    self.currentTetrominoFalling["shapeObj"].lastPositionDrawn = location
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

  def spawnTetromino(self, Tetromino : Shape=mShapes.DEFAULT_SHAPE_OBJECT) -> str:
    if Tetromino == mShapes.DEFAULT_SHAPE_OBJECT:
      Tetromino = random.choice(shapes)
    self.numberOfTetrominosSpawned += 1
    Tetromino.id = self.numberOfTetrominosSpawned
    self.currentTetrominoFalling = {"shapeObj": Tetromino, "id": Tetromino.id}
    print(f"spawning {Tetromino.name}")
    self.drawShapeAtLocation([(self.width // 2) - 2, 0], Tetromino.id)
    self.currentTetrominoFalling["shapeObj"].lastPositionDrawn = [(self.width // 2) - 2, 0]
    TetrominoName = Tetromino.name
    return TetrominoName
  
  def moveTetromino(self, dX: int, dY: int): #delta x and delta y; Tetromino to move is like current Tetromino Falling property except it is not bound to the current Tetromino falling, i.e it can be any Tetromino
    if self.currentTetrominoFalling["shapeObj"] == None or self.currentTetrominoFalling["id"] == None: 
      print("Move Tetromino Function tried to move current Falling Tetromino however it is a none type")
      return -1
    
    TetObj: Shape = self.currentTetrominoFalling['shapeObj']
    TetID: int = self.currentTetrominoFalling['id']
    lastPositionDrawn = TetObj.lastPositionDrawn
    board = copy.deepcopy(self.board)
    self._removeID(TetID)
    returnValueOfDraw : int = self.drawShapeAtLocation([lastPositionDrawn[0] + dX, lastPositionDrawn[1] + dY], TetID)
    if returnValueOfDraw != 0:
      if returnValueOfDraw == 100 or returnValueOfDraw == -100:
        pygame.event.post(pygame.event.Event(SPAWN_TETROMINO))
      self.board = board


game = Game()

running = True
dx, dy = 0, 0
game.spawnTetromino()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False

    if event.type == pygame.KEYDOWN:            
        if event.key == pygame.K_UP:
            game.currentTetrominoFalling["shapeObj"].rotate()
            game.moveTetromino(0, 0)
        if event.key == pygame.K_DOWN:
            game.moveTetromino(0, 1)
        if event.key == pygame.K_RIGHT:
            game.moveTetromino(1, 0)
        if event.key == pygame.K_LEFT:
            game.moveTetromino(-1, 0)
    
    if event.type == SECONDPASSED:
      game.moveTetromino(0, 1)
    if event.type == SPAWN_TETROMINO:
      game.spawnTetromino()

    game.screen.fill(GRAY)
    game.draw()
    pygame.display.flip()