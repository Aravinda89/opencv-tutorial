import numpy as np
import cv2

img = cv2.imread('./images/typewriter.jpg')

all_rows = open('./models/synset_words.txt').read().strip().split('\n')
classes = [r[r.find(' ')+1:] for r in all_rows]

# for (i,c) in enumerate(classes):
#     if i==4:
#         break
#     print(i,c)

net = cv2.dnn.readNetFromCaffe('models/bvlc_googlenet.prototxt','models/bvlc_googlenet.caffemodel')
blob = cv2.dnn.blobFromImage(img, 1, (224, 224))
net.setInput(blob)

outp = net.forward()
idx = np.argsort(outp[0])[::-1][:5]

for (i,id) in enumerate(idx):
    print('{}. ({}): Prob {:.3}%'.format(i+1, classes[id], outp[0][id]*100))

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
