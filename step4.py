import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1) # number 0 for one camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out  = cv2.VideoWriter('output.avi',fourcc,24.0,(640,480)) #params 3 = fram rate speed fram for save

# GRAY SCALE FOR ALL PIC
while(True): #video is pics
    ret,fram = cap.read()
    gray = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY) # cv2 =>blue - green -red
    out.write(fram)
    cv2.imshow('cameras',fram)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()