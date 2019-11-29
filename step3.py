import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1) # number 0 for one camera

# GRAY SCALE FOR ALL PIC
while(True): #video is pics
    ret,fram = cap.read()
    #gray = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY) # cv2 =>blue - green -red
    cv2.imshow('cameras',fram)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()