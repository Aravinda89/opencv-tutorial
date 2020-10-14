import cv2
import numpy as np

img = cv2.imread('opencv-logo.png', 1)

print(img)
print(type(img))
print(img.shape)
print(img.dtype)
print(img[10, 5])
print(img.size) # Total pixels
