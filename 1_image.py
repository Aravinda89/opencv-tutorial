import cv2

img = cv2.imread('./dali.jpg')
print(img.shape)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
