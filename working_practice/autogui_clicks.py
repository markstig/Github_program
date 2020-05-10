import pyautogui
import time

for i in range(10):
    pyautogui.moveTo(1717, 252)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(1719, 181, duration=1)
    pyautogui.click()
    time.sleep(2)
    print('{} file(s) has beed downloaded!'.format(i+1))