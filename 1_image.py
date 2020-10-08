import cv2

img = cv2.imread('./dali.jpg')
# print(img.shape)

b=img[:,:,0]
print(b)
g=img[:,:,1]
print(g)
r=img[:,:,2]
print(r)

# cv2.imshow('Image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
