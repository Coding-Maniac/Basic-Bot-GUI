from PIL import ImageGrab , ImageOps
import pyautogui
import time
from numpy import *
class cordinates():
    replaybtn = (502,494) #1
    dinosaur =(511,199)
    #x=230 
    #y= 540

def restartGame():
    pyautogui.click(cordinates.replaybtn)
restartGame()
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')
def imageGrab():
    box=(cordinates.dinosaur[0]+60,cordinates.dinosaur[1],cordinates.dinosaur[0]+100,cordinates.dinosaur[1]+45)
    image = ImageGrab.grab(box)
    grayImage =  ImageOps.grayscale(image)
    a = array(grayImage.getcolors())

    return a.sum()
def main():
    restartGame()
    while True:
        if(imageGrab()!=2047):
            pressSpace()
            time.sleep(0.1)
main()


