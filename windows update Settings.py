import pyautogui
import time

# Simulate pressing the Windows key
pyautogui.press('win')

# Wait for the Start menu to open
time.sleep(1)


#pyautogui.write('Windows Update')
pyautogui.write('Check for updates')

# Wait for the search results to appear
time.sleep(1)

# Press 'Enter' to open Notepad
pyautogui.press('enter')

time.sleep(1)

pyautogui.press('enter')

#pyautogui.press
