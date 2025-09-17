import pyautogui
import pyperclip
import keyboard
import time
print("Cheater Typer 2.0 -- by Shyam Shankar")
print("Press '~' to type clipboard contents... (Press ESC to quit)")
print("Press '$' to add clipboard contents together...")
print("Link to AI website: ")
print("www.chatgpt.com")
print("gemini.google.com")
print("www.perplexity.ai")
text = ''
con = 0
while True:
    if keyboard.is_pressed('~'):
        time.sleep(0.2)
        if con == 0:
            text = pyperclip.paste()
        else:
            text = text
        pyautogui.press('backspace')
        print("Typing copied text...")
        pyautogui.write(text, interval=0.02)
        pyautogui.keyDown('shift')
        for i in range(12):
            pyautogui.press('down')
        pyautogui.keyUp('shift')
        pyautogui.press('backspace')
    if keyboard.is_pressed('$'):
        con = 1
        text += pyperclip.paste()
        text += "\n"


    if keyboard.is_pressed('esc'):
        print("Exiting...")
        break
