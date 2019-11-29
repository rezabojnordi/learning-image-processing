
import cv2
import numpy as np
img = cv2.imread('1.png',cv2.IMREAD_GRAYSCALE) # 2 params flags
cv2.imshow("image",img) # one params 
cv2.waitKey(0)
cv2.destroyAllWindows() # for clean rams 
