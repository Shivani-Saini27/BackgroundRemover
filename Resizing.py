import cv2
import os

for root, subdirs, files in os.walk('/home/shivani/Desktop/BackgroundRemover/BackgroundImages'):
	for f in files:
		if f.endswith('jpg'):
			img = cv2.imread('/home/shivani/Desktop/BackgroundRemover/BackgroundImages/' + f)
			img = cv2.resize(img, (640, 480))
			cv2.imwrite('/home/shivani/Desktop/BackgroundRemover/BackgroundImages/' +f, img)
			print(*["Image", f, "is resized to 640 x 480"])