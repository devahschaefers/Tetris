from classes import Colors, Block, Shape

DEFAULT_BLOCK = Block()
DEFAULT_RAW_SHAPE = [
  [
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK]
  ],
  [
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK]
  ],
  [
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK]
  ],
  [
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK],
    [DEFAULT_BLOCK, DEFAULT_BLOCK, DEFAULT_BLOCK]
  ]
]
DEFAULT_SHAPE_OBJECT = Shape(DEFAULT_RAW_SHAPE, Colors.NO_COLOR, "DEFAULT_SHAPE")
rawShapes = {
    "oBlock": [
               [ 
                [Block(Colors.YELLOW), Block(Colors.YELLOW)], 
                [Block(Colors.YELLOW), Block(Colors.YELLOW)]
               ],
      
               [ 
                [Block(Colors.YELLOW), Block(Colors.YELLOW)], 
                [Block(Colors.YELLOW), Block(Colors.YELLOW)]],
      
               [ 
                [Block(Colors.YELLOW), Block(Colors.YELLOW)], 
                [Block(Colors.YELLOW), Block(Colors.YELLOW)]],
      
               [ 
                [Block(Colors.YELLOW), Block(Colors.YELLOW)], 
                [Block(Colors.YELLOW), Block(Colors.YELLOW)]]
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
                [DEFAULT_BLOCK,DEFAULT_BLOCK,DEFAULT_BLOCK,DEFAULT_BLOCK],
                [Block(Colors.RED), Block(Colors.RED), Block(Colors.RED), Block(Colors.RED)]
              ],
              [
                [DEFAULT_BLOCK, Block(Colors.RED)], 
                [DEFAULT_BLOCK, Block(Colors.RED)], 
                [DEFAULT_BLOCK, Block(Colors.RED)], 
                [DEFAULT_BLOCK, Block(Colors.RED)]
              ]
            ],
    "jBlock": [
                [
                 [Block(Colors.ORANGE), DEFAULT_BLOCK, DEFAULT_BLOCK], 
                 [Block(Colors.ORANGE), Block(Colors.ORANGE), Block(Colors.ORANGE)]
                ],
      
                [
                 [Block(Colors.ORANGE), Block(Colors.ORANGE)], 
                 [Block(Colors.ORANGE), DEFAULT_BLOCK], 
                 [Block(Colors.ORANGE), DEFAULT_BLOCK]
                ],
      
                [  
                 [Block(Colors.ORANGE),   Block(Colors.ORANGE),   Block(Colors.ORANGE)], 
                 [DEFAULT_BLOCK, DEFAULT_BLOCK, Block(Colors.ORANGE)]
                ],
                [
                 [DEFAULT_BLOCK, Block(Colors.ORANGE)], 
                 [DEFAULT_BLOCK, Block(Colors.ORANGE)], 
                 [Block(Colors.ORANGE), Block(Colors.ORANGE)]
                ]
              ],
    "lBlock": [
                 [
                  [DEFAULT_BLOCK, DEFAULT_BLOCK, Block(Colors.BLUE)],
                  [Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.BLUE)]
                 ],
      
                 [
                  [Block(Colors.BLUE), DEFAULT_BLOCK], 
                  [Block(Colors.BLUE), DEFAULT_BLOCK], 
                  [Block(Colors.BLUE), Block(Colors.BLUE)]
                 ],
      
                 [
                  [Block(Colors.BLUE), Block(Colors.BLUE), Block(Colors.BLUE)], 
                  [Block(Colors.BLUE), DEFAULT_BLOCK, DEFAULT_BLOCK]
                 ],
      
                 [
                  [Block(Colors.BLUE), Block(Colors.BLUE)],  
                  [DEFAULT_BLOCK, Block(Colors.BLUE)],  
                  [DEFAULT_BLOCK, Block(Colors.BLUE)]   
                ]
              ],
    "sBlock": [
                 [
                  [DEFAULT_BLOCK, Block(Colors.PURPLE), Block(Colors.PURPLE)],
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), DEFAULT_BLOCK]
                 ],
      
                 [ 
                  [Block(Colors.PURPLE), DEFAULT_BLOCK], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE)], 
                  [DEFAULT_BLOCK, Block(Colors.PURPLE)]
                 ],
      
                 [ 
                  [DEFAULT_BLOCK, Block(Colors.PURPLE), Block(Colors.PURPLE)], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE), DEFAULT_BLOCK]
                 ],
      
                 [
                  [Block(Colors.PURPLE), DEFAULT_BLOCK], 
                  [Block(Colors.PURPLE), Block(Colors.PURPLE)],
                  [DEFAULT_BLOCK, Block(Colors.PURPLE)]
                ],
              ],
    "zBlock": [
                [
                  [DEFAULT_BLOCK, Block(Colors.GREEN), Block(Colors.GREEN)], 
                  [Block(Colors.GREEN), Block(Colors.GREEN), DEFAULT_BLOCK]
                ],
                [ 
                  [Block(Colors.GREEN), DEFAULT_BLOCK],
                  [Block(Colors.GREEN), Block(Colors.GREEN)], 
                  [DEFAULT_BLOCK, Block(Colors.GREEN)]
                ],
                [ 
                  [DEFAULT_BLOCK, Block(Colors.GREEN), Block(Colors.GREEN)], 
                  [Block(Colors.GREEN), Block(Colors.GREEN), DEFAULT_BLOCK]
                ],
                [ 
                  [Block(Colors.GREEN), DEFAULT_BLOCK],
                  [Block(Colors.GREEN), Block(Colors.GREEN)],
                  [DEFAULT_BLOCK, Block(Colors.GREEN)]
                ]
              ],
    "tBlock": [
                [ 
                  [DEFAULT_BLOCK, Block(Colors.CYAN), DEFAULT_BLOCK], 
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.CYAN)]
                ],
                [
                  [ Block(Colors.CYAN), DEFAULT_BLOCK], 
                  [ Block(Colors.CYAN), Block(Colors.CYAN)],
                  [ Block(Colors.CYAN), DEFAULT_BLOCK]
                ],
                [
                  [Block(Colors.CYAN), Block(Colors.CYAN), Block(Colors.CYAN), DEFAULT_BLOCK], 
                  [DEFAULT_BLOCK, Block(Colors.CYAN), DEFAULT_BLOCK, DEFAULT_BLOCK]
                ],
                [
                  [DEFAULT_BLOCK, Block(Colors.CYAN)],
                  [Block(Colors.CYAN), Block(Colors.CYAN)],
                  [DEFAULT_BLOCK, Block(Colors.CYAN)]
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