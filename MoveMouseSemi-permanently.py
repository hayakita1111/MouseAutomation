import pyautogui
import keyboard

screenWidth, screenHeight = pyautogui.size()

while True:
    pyautogui.moveTo(100, 500, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(400, 500, duration=2, tween=pyautogui.easeInOutQuad)

    if keyboard.is_pressed('s'):
        break