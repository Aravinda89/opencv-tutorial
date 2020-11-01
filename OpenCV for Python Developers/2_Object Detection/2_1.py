# Simple Thresholding

import numpy as np
import cv2

bw = cv2.imread('./detect_blob.png',0)
print(bw.shape)
# cv2.imshow('BW',bw)



cv2.waitKey(0)
cv2.destroyAllWindows()
