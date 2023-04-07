import pyautogui, webbrowser
from time import sleep

OPT_Y = "Si" 
OPT_N = "No"


opt = pyautogui.confirm(
    "¿Tienes Youtube Premium?",
    "Confirm",
    [OPT_Y, OPT_N]
)

# Aquí pon el nombre de tu canción o video que quieras reproducir
Video = pyautogui.prompt("Ingrese el nombre de su video ", "Reproducir")

webbrowser.open('https://www.youtube.com/')

# Esto es el tiempo para que abra youtube y que carge, esto varía
sleep (8)
pyautogui.moveTo(370, 140)

if opt == OPT_N:
    for i in range(4):
        pyautogui.press("tab")              
    
        
    pyautogui.typewrite(Video)
    pyautogui.press("enter")

    sleep(3)

    for i in range(4):
        pyautogui.press("tab")

    pyautogui.press("enter")

elif opt == OPT_Y:
    for i in range(4):
        pyautogui.press("tab")              
    
        
    pyautogui.typewrite(Video)
    pyautogui.press("enter")

    sleep(3)

    pyautogui.press("enter")