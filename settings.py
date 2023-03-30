fps = 25
window_w, window_h = 484, 700
block, side = 20, 40
colors = ((100, 100, 255), # blue 0
          (50, 255, 50), # green 1
          (255, 30, 30), # red 2
          (255, 255, 30), #yellow 3
          (50, 50, 50) #grey 4
          )
figures = {'S': [['.....',
                  '.....',
                  '..xx.',
                  '.xx..',
                  '.....'],
                 ['.....',
                  '..x..',
                  '..xx.',
                  '...x.',
                  '.....']],
           'Z': [['.....',
                  '.....',
                  '.xx..',
                  '..xx.',
                  '.....'],
                 ['.....',
                  '..x..',
                  '.xx..',
                  '.x...',
                  '.....']],
           'J': [['.....',
                  '.x...',
                  '.xxx.',
                  '.....',
                  '.....'],
                 ['.....',
                  '..xx.',
                  '..x..',
                  '..x..',
                  '.....'],
                 ['.....',
                  '.....',
                  '.xxx.',
                  '...x.',
                  '.....'],
                 ['.....',
                  '..x..',
                  '..x..',
                  '.xx..',
                  '.....']],
           'L': [['.....',
                  '...x.',
                  '.xxx.',
                  '.....',
                  '.....'],
                 ['.....',
                  '..x..',
                  '..x..',
                  '..xx.',
                  '.....'],
                 ['.....',
                  '.....',
                  '.xxx.',
                  '.x...',
                  '.....'],
                 ['.....',
                  '.xx..',
                  '..x..',
                  '..x..',
                  '.....']],
           'I': [['..x..',
                  '..x..',
                  '..x..',
                  '..x..',
                  '.....'],
                 ['.....',
                  '.....',
                  'xxxx.',
                  '.....',
                  '.....']],
           '.': [['.....',
                  '.....',
                  '.xx..',
                  '.xx..',
                  '.....']],
           'T': [['.....',
                  '..x..',
                  '.xxx.',
                  '.....',
                  '.....'],
                 ['.....',
                  '..x..',
                  '..xx.',
                  '..x..',
                  '.....'],
                 ['.....',
                  '.....',
                  '.xxx.',
                  '..x..',
                  '.....'],
                 ['.....',
                  '..x..',
                  '.xx..',
                  '..x..',
                  '.....']]}
