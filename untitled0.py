# -*- coding: utf-8 -*-
####
###
## Code by Schrojam

import mouse
import time

i = 1
movements = [[1981,1640],[1971,1640]]
while True:
    i = (i+1)%2
    x = movements[i][0]
    y = movements[i][1]
    #print(f"x={x},y={y}")
    mouse.move(x,y)
    mouse.click()
    time.sleep(240)

        