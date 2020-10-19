import numpy
import cv2

image = cv2.imread('thresh.jpg')
cv2.imshow('Original', image)

blur = cv2.GaussianBlur(image, (55,5), 0)
cv2.imshow('Blur', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
