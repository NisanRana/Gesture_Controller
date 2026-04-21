import pyautogui

def execute(gesture):
    if gesture == "palm":
        print("⏯ PLAY/PAUSE")
        pyautogui.press("space")

    elif gesture == "fist":
        print("⏹ full screen")
        pyautogui.press("f")