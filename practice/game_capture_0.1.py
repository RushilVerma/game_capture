import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import ReleaseKey, PressKey, W, A, S, D

def process_img(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_img = cv2.Canny(gray_img, threshold1=200, threshold2=500)
    final_img = canny_img
    return final_img

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

prev_time=time.time()
while(True):

    Screen = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0,32,801,633))), cv2.COLOR_BGR2RGB)
    proc_screen = process_img(Screen)
    
    PressKey(W)
    cv2.imshow('Screen',proc_screen)
    print(time.time()-prev_time)
    prev_time=time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break 