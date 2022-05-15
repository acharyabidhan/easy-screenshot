from keyboard import is_pressed
from time import strftime
from pyautogui import screenshot
from os import path, mkdir
from winsound import MessageBeep
from time import sleep
from shutil import copy
username = (path.split(path.expanduser('~'))[-1])
try:
    try:mkdir(f"C:\\Users\\{username}\\Pictures\\Screenshots")
    except:mkdir(f"C:\\Users\\{username}\\OneDrive\\Pictures\\Screenshots")
except:pass
try:copy("screenshot.exe", f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
except:pass
def takeSS():
    ssName = strftime("%Y%m%d%H%M%S")
    ssImage = screenshot()
    try:
        try:ssImage.save(f"C:\\Users\\{username}\\Pictures\\Screenshots\\{ssName}.png")
        except:ssImage.save(f"C:\\Users\\{username}\\OneDrive\\Pictures\\Screenshots\\{ssName}.png")
    except:pass
    MessageBeep()
while True:
    if is_pressed("ctrl+alt"):
        takeSS()
    sleep(1)
#This much :) -Bidhan Acharya