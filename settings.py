window_w, window_h = 484, 700
block, side = 20, 40
colors = ((100, 100, 255), # blue 0
          (50, 255, 50), # green 1
          (255, 30, 30), # red 2
          (255, 255, 30), #yellow 3
          (50, 50, 50) #grey 4
          )
figures = {
           '0': [[
              '..xx.',
              '.xx*.',
              '.**..'],
             ['..x..',
              '..xx.',
              '..*x.',
              '...*.']],
           '1': [[
                  '.xx..',
                  '.*xx.',
                  '..**.'],
                 ['..x..',
                  '.xx..',
                  '.x...',
                  '.....']],
           '2': [[
                  '.x...',
                  '.xxx.',
                  '.....'],
                 ['..xx.',
                  '..x..',
                  '..x..',
                  '.....'],
                 ['.xxx.',
                  '...x.',
                  '.....'],
                 ['..x..',
                  '..x..',
                  '.xx..',
                  '.....']],
           '3': [['...x.',
                  '.xxx.',
                  '.....'],
                 ['..x..',
                  '..x..',
                  '..xx.',
                  '.....'],
                 ['.xxx.',
                  '.x...',
                  '.....'],
                 ['.xx..',
                  '..x..',
                  '..x..',
                  '.....']],
           '4': [['..x..',
                  '..x..',
                  '..x..',
                  '..x..',
                  '.....'],
                 ['xxxx.',
                  '.....']],
           '5': [['.xx..',
                  '.xx..',
                  '.....']],
           '6': [['..x..',
                  '.xxx.',
                  '.....'],
                 ['..x..',
                  '..xx.',
                  '..x..',
                  '.....'],
                 ['.xxx.',
                  '..x..',
                  '.....'],
                 ['..x..',
                  '.xx..',
                  '..x..',
                  '.....']]}
