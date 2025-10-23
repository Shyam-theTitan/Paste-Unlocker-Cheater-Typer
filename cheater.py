import pyautogui
import pyperclip
import keyboard
import time
print("PAG Typer -- By S.S.Shyamshankar")
print("Press '~' to type clipboard contents... (Press ESC to quit)")
#print("Press '$' to add clipboard contents together...") Still testing
print("Link to AI website: ")
print("www.chatgpt.com")
print("gemini.google.com")
print("www.perplexity.ai")
text = ''
con = 0
while True:
    if keyboard.is_pressed('~'):
        time.sleep(0.2)
        text = pyperclip.paste()
        lines = []
        for line in text.splitlines():
            lines.append(line)
        pyautogui.press('backspace')
        print("Typing copied text...")
        #pyautogui.write(text, interval=0.02)
        for l in lines:
            l = l.replace('\t','')
            pyautogui.write(l)
            pyautogui.press('enter')    
        pyautogui.keyDown('shift')
        for i in range(20):
            pyautogui.press('down')
        pyautogui.keyUp('shift')
        pyautogui.press('backspace')
    # if keyboard.is_pressed('$'):
    #     con = 1
    #     text += pyperclip.paste()
    #     text += "\n"
    if keyboard.is_pressed('esc'):
        print("Exiting...")
        break
