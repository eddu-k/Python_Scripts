import pyautogui
import time

# Simulate pressing the Windows key
pyautogui.press('win')

# Wait for the Start menu to open
time.sleep(1)

# Type 'Notepad'
pyautogui.write('Notepad')

# Wait for the search results to appear
time.sleep(1)

# Press 'Enter' to open Notepad
pyautogui.press('enter')
