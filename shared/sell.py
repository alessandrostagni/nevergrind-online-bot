## Needs to be adjusted for expanding inventory

import pyautogui
import time

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
position_x_multiplier = 0.494140625
position_y_multiplier = 0.4215277777777778
x_increment_multiplier = 0.0234375
y_increment_multiplier = 0.0416666666666667
pos_x = int(SCREEN_WIDTH * position_x_multiplier)
pos_y = int(SCREEN_HEIGHT * position_y_multiplier)
x_increment =  SCREEN_WIDTH * x_increment_multiplier
y_increment_multiplier = SCREEN_HEIGHT * y_increment_multiplier
identify_x_multiplier = 0.11796875
identify_y_multiplier = 0.5805555555555556

identify_x = int(SCREEN_WIDTH * identify_x_multiplier)
identify_y = int(SCREEN_HEIGHT * identify_y_multiplier)

time.sleep(3)
pyautogui.click(identify_x, identify_y)

time.sleep(0.5)
for x in range(pos_x, pos_x + 60*4, 60):
    for y in range(pos_y, pos_y + 60*6, 60):
        pyautogui.keyDown('ctrl')
        pyautogui.click(x, y)
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)