import pyautogui

# print(pyautogui.size()) # Get the size of the screen window

# width, height = pyautogui.size()
# print(width)
# print(height)
print(pyautogui.position())  # get the current position of  the mouse cursor

pyautogui.moveTo(10,10)
pyautogui.moveTo(20,20, duration=1.5)

pyautogui.moveRel(20, 0, duration=2)
pyautogui.moveRel(20,20, duration=2)

pyautogui.click(0,0)
pyautogui.doubleClick(0, 0)  # middleclick(), rightclick()

pyautogui.dragRel(1,1, duration=2)


# check real time coordinates
# open cmd/shell
# python3
# import pyautogui
# pyautogui.displayMousePosition()

