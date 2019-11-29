import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread('1.png',cv2.IMREAD_GRAYSCALE)

plt.imshow(img,cmap='gray',interpolation='bicubic')
position = plt.plot([100,200],[200,300],'r',linewidth=5)   # r =red
plt.show()
cv2.imwrite('imgout.jpg',img)

#cv2.waitKey(0)
#cv2.destroyAllWindows()


