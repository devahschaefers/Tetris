'''
ERRORS

-200 = IndexError
-100 = Hit an object


'''
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

def coordinates_to_pixel_loc(postion):  # maybe think of a better name
    postion = list(postion)
    postion[0] = postion[0] * SPRITE_SIZE
    postion[1] = postion[1] * SPRITE_SIZE
    return (postion[0], postion[1])

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
      self.currentTetrominoFalling = None
      self.size = (width * SPRITE_SIZE + 2, height * SPRITE_SIZE)
      self.screen = pygame.display.set_mode(self.size)
      pygame.time.set_timer(SECONDPASSED, 1000)
  #-----set up board -------------
      row = []
      for i in range(self.width):
          for j in range(self.height):
              row.append(Block(Colors.NO_COLOR, location = [i, j]))
          self.board.append(row.copy())
          row.clear()
  #---------------------------------
  
  def drawDrawShapeAtLocation(self, location, blockID, Tetromino = None):
    #create copy of the board which will replace the actual board if the fuction doesnt encounter errors
    board = copy.deepcopy(self.board)
    #assumes tetormino is a shape object)
    if Tetromino == None:
      Tetromino = self.currentTetrominoFalling[0]
    y_lengthOfTetromino = len(Tetromino.shape[Tetromino.currentRotation])
    x_lengthOfTetromino = len(Tetromino.shape[Tetromino.currentRotation][0])
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
    self.board = board
  
  def draw(self):
    for collum in self.board:
      for Block in collum:
        if Block.color != Colors.NO_COLOR:
          self.screen.blit(img_Blue, coordinates_to_pixel_loc(Block.location))
       
  def spawnTetromino(self, Tetromino=random.choice(shapes)):
    self.numberOfTetrominosSpawned += 1
    Tetromino.id = self.numberOfTetrominosSpawned
    self.currentTetrominoFalling = {"shape": Tetromino, "id": Tetromino.id}
    print(f"spawming {Tetromino.name}")
    self.drawDrawShapeAtLocation([(self.width // 2) - 2, 0], Tetromino.id, Tetromino)
    return Tetromino.name
  
  def moveTetromino(self, TetrominoID, dX, dY): #delta x and delta y
    currentPositionOfTetromino = []
    #------- find current postions of falling tetromino -------
    for collum in self.board:
      for Block in collum:
        if Block.shapeID == TetrominoID:
          currentPositionOfTetromino.append(Block.location)
    #----------------------------------------------------------      
    
    board = copy.deepcopy(self.board)
    
    try:
      for position in currentPositionOfTetromino:
        board[position[0]][position[1]] = mShapes.DEFUALT_BLOCK
      for position in currentPositionOfTetromino:
        board[position[0] + dX][position[1] + dY] = self.board[position[0]][position[1]]
    except IndexError:
      return -200
    
    self.board = board


game = Game(width =11)

# while True:
#   for event in pygame.event.get():
#     if event.type == SECONDPASSED:
#         os.system("clear")
#         printBoard(game.board)

#   if game.currentTetrominoFalling == None:
#       spawmedTetromino = game.spawnTetromino()
      
#   game.moveTetromino(game.currentTetrominoFalling["id"], 1, 0)

if game.currentTetrominoFalling == None:
    spawmedTetromino = game.spawnTetromino()

printBoard(game.board)

running = True
timeRunning = 0 #in seconds
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
    if event.type == SECONDPASSED:
      game.moveTetromino(game.currentTetrominoFalling["id"], 0, -1)
      timeRunning += 1
      os.system("clear")
      printBoard(game.board)
      print("time running:", timeRunning)


    game.screen.fill(GRAY)
    game.draw()
    pygame.display.flip()
  
  