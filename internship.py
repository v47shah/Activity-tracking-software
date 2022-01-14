import cv2 #OpenCV
import pyautogui
import numpy as np
from PIL import ImageGrab
import numpy as np
import cv2
#from win32api import GetSystemMetrics
import datetime
import time
import pyautogui as pg

#width = GetSystemMetrics(0)
#height = GetSystemMetrics(1)

Recording_time = time.time() + 120

while time.time() <= Recording_time:
    time.sleep(10)
    
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    file_name = f'{time_stamp}.mp4'
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    captured_video = cv2.VideoWriter(file_name, fourcc, 10.0, (3000, 1500))

    t_end = time.time() + 5
    file_name1 = f'{time_stamp}.png'
    
    image = pg.screenshot()
    image.save(file_name1)
    
    while time.time() <= t_end:
        
        img = ImageGrab.grab(bbox=(0, 0, 3000, 1500))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('Recorder', img_final)
        captured_video.write(img_final)
        cv2.waitKey(10)
    

