import pyautogui

pyautogui.screenshot('/xx/xxx/xx.png')

pyautogui.locateOnScreen('/xx/xx/xx.png')  # return the coordinate/width/height of the pic

pyautogui.locateCenterOnScreen('/XX/XX/XX.png')
# with the coordinate, we can moveTo and lick for the next operations.

