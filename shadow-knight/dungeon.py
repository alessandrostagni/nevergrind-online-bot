import pyautogui
import time

sanguine_harvest_interval = 60 * 3
vampire_feast_interval = 5 
i = 0
j = 0
pyautogui.press('3')

while True:
    pyautogui.press('1')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('\\')
    time.sleep(1)
    if i == sanguine_harvest_interval:
        pyautogui.press('3')
        time.sleep(0.5)
        i = 0
    if j == vampire_feast_interval:
        pyautogui.press('9')
        time.sleep(0.5)
        j = 0
    i += 1
    j += 1
