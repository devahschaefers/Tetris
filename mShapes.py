from classes import Colors, Block, Shape

DEFUALT_BLOCK = Block()

rawShapes = {
    "oBlock": [
               [ 
                [DEFUALT_BLOCK, Block(Colors.YELLOW), Block(Colors.YELLOW), DEFUALT_BLOCK], 
                [DEFUALT_BLOCK, Block(Colors.YELLOW), Block(Colors.YELLOW), DEFUALT_BLOCK]],
      
               [ 
                [DEFUALT_BLOCK, Block(Colors.YELLOW), Block(Colors.YELLOW), DEFUALT_BLOCK], 
                [DEFUALT_BLOCK, Block(Colors.YELLOW), Block(Colors.YELLOW), DEFUALT_BLOCK]],
      
               [ 
                [DEFUALT_BLOCK, Block(Colors.YELLOW), Block(Colors.YELLOW), DEFUALT_BLOCK], 
                [DEFUALT_BLOCK, Block(Colors.YELLOW), Block(Colors.YELLOW), DEFUALT_BLOCK]],
      
               [ 
                [DEFUALT_BLOCK, Block(Colors.YELLOW), Block(Colors.YELLOW), DEFUALT_BLOCK], 
                [DEFUALT_BLOCK, Block(Colors.YELLOW), Block(Colors.YELLOW), DEFUALT_BLOCK]]
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
                [DEFUALT_BLOCK,DEFUALT_BLOCK,DEFUALT_BLOCK,DEFUALT_BLOCK]
              ],
              [
                [Block(Colors.RED), Block(Colors.RED), Block(Colors.RED), Block(Colors.RED)]
              ],
      
              [
                [DEFUALT_BLOCK, Block(Colors.RED)], 
                [DEFUALT_BLOCK, Block(Colors.RED)], 
                [DEFUALT_BLOCK, Block(Colors.RED)], 
                [DEFUALT_BLOCK, Block(Colors.RED)]
              ]
            ],
    "jBlock": [
                [
                 [Block(Colors.ORANGE), DEFUALT_BLOCK, DEFUALT_BLOCK], 
                 [Block(Colors.ORANGE), Block(Colors.ORANGE), Block(Colors.ORANGE)]
                ],
      
                [
                 [DEFUALT_BLOCK, Block(Colors.ORANGE), Block(Colors.ORANGE)], 
                 [DEFUALT_BLOCK, Block(Colors.ORANGE), DEFUALT_BLOCK], 
                 [DEFUALT_BLOCK, Block(Colors.ORANGE), DEFUALT_BLOCK]
                ],
      
                [  
                 [Block(Colors.ORANGE),   Block(Colors.ORANGE),   Block(Colors.ORANGE)], 
                 [DEFUALT_BLOCK, DEFUALT_BLOCK, Block(Colors.ORANGE)]
                ],
                [
                 [DEFUALT_BLOCK, Block(Colors.ORANGE), DEFUALT_BLOCK], 
                 [DEFUALT_BLOCK, Block(Colors.ORANGE), DEFUALT_BLOCK], 
                 [Block(Colors.ORANGE), Block(Colors.ORANGE), DEFUALT_BLOCK]
                ]
              ],
    "lBlock": [
                 [
                  [DEFUALT_BLOCK, DEFUALT_BLOCK, DEFUALT_BLOCK, Block(Colors.BLUE)],
                  [DEFUALT_BLOCK, Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.BLUE)]
                 ],
      
                 [
                  [DEFUALT_BLOCK, Block(Colors.BLUE), DEFUALT_BLOCK], 
                  [DEFUALT_BLOCK, Block(Colors.BLUE), DEFUALT_BLOCK], 
                  [DEFUALT_BLOCK, Block(Colors.BLUE), Block(Colors.BLUE)]
                 ],
      
                 [
                  [Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.BLUE), DEFUALT_BLOCK], 
                  [Block(Colors.BLUE), DEFUALT_BLOCK, DEFUALT_BLOCK, DEFUALT_BLOCK]
                 ],
      
                 [
                  [Block(Colors.BLUE), Block(Colors.BLUE), DEFUALT_BLOCK],  
                  [DEFUALT_BLOCK, Block(Colors.BLUE), DEFUALT_BLOCK],  
                  [DEFUALT_BLOCK, Block(Colors.BLUE), DEFUALT_BLOCK]   
                ]
              ],
    "sBlock": [
                 [
                  [DEFUALT_BLOCK, Block(Colors.PURPLE), Block(Colors.PURPLE)],
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), DEFUALT_BLOCK]
                 ],
      
                 [ 
                  [DEFUALT_BLOCK, Block(Colors.PURPLE), DEFUALT_BLOCK], 
                  [DEFUALT_BLOCK, Block(Colors.PURPLE), Block(Colors.PURPLE)], 
                  [DEFUALT_BLOCK, DEFUALT_BLOCK, Block(Colors.PURPLE)]
                 ],
      
                 [ 
                  [DEFUALT_BLOCK, Block(Colors.PURPLE), Block(Colors.PURPLE)], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), DEFUALT_BLOCK]
                 ],
      
                 [
                  [Block(Colors.PURPLE), DEFUALT_BLOCK, DEFUALT_BLOCK], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), DEFUALT_BLOCK],
                  [DEFUALT_BLOCK, Block(Colors.PURPLE), DEFUALT_BLOCK]
                ],
              ],
    "zBlock": [
                [
                  [DEFUALT_BLOCK, Block(Colors.GREEN), Block(Colors.GREEN)], 
                  [Block(Colors.GREEN), Block(Colors.GREEN), DEFUALT_BLOCK]
                ],
                [ 
                  [Block(Colors.GREEN), DEFUALT_BLOCK, DEFUALT_BLOCK],
                  [Block(Colors.GREEN), Block(Colors.GREEN), DEFUALT_BLOCK], 
                  [DEFUALT_BLOCK, Block(Colors.GREEN), DEFUALT_BLOCK]
                ],
                [ 
                  [DEFUALT_BLOCK, DEFUALT_BLOCK, DEFUALT_BLOCK],
                  [DEFUALT_BLOCK, Block(Colors.GREEN), Block(Colors.GREEN)], 
                  [Block(Colors.GREEN), Block(Colors.GREEN), DEFUALT_BLOCK]
                ],
                [ 
                  [Block(Colors.GREEN), DEFUALT_BLOCK, DEFUALT_BLOCK],
                  [Block(Colors.GREEN), Block(Colors.GREEN), DEFUALT_BLOCK],
                  [DEFUALT_BLOCK, Block(Colors.GREEN), DEFUALT_BLOCK]
                ]
              ],
    "tBlock": [
                [ 
                  [DEFUALT_BLOCK, Block(Colors.CYAN), DEFUALT_BLOCK], 
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.CYAN)]
                ],
                [
                  [ DEFUALT_BLOCK, DEFUALT_BLOCK, DEFUALT_BLOCK], 
                  [ Block(Colors.CYAN), DEFUALT_BLOCK, DEFUALT_BLOCK], 
                  [ Block(Colors.CYAN), Block(Colors.CYAN), DEFUALT_BLOCK], 
                  [ Block(Colors.CYAN), DEFUALT_BLOCK, DEFUALT_BLOCK]
                ],
                [
                  [DEFUALT_BLOCK, DEFUALT_BLOCK, DEFUALT_BLOCK, DEFUALT_BLOCK], 
                  [DEFUALT_BLOCK, DEFUALT_BLOCK, DEFUALT_BLOCK, DEFUALT_BLOCK], 
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.CYAN), DEFUALT_BLOCK], 
                  [DEFUALT_BLOCK, Block(Colors.CYAN), DEFUALT_BLOCK, DEFUALT_BLOCK]
                ],
                [
                  [DEFUALT_BLOCK, Block(Colors.CYAN), DEFUALT_BLOCK],
                  [Block(Colors.CYAN), Block(Colors.CYAN), DEFUALT_BLOCK],
                  [DEFUALT_BLOCK, Block(Colors.CYAN), DEFUALT_BLOCK]
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