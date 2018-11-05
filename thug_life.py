import cv2 # we import the necessary modules
import numpy as np

img = cv2.imread('face.jpg', -1) # we read the image or store the image cv2.imread(img_name,data type)
# 1 = colorful image
# 0 = grayscale image
#-1 = unchanged image
specs = cv2.imread('thuglifespecs.png', -1) # this will store the specs image


cv2.imshow('Original',img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # we convert the image to grayscale for opencv processing
eyes_cascade = cv2.CascadeClassifier('frontalEyes.xml') # we initialise the cascade classifier
eyes = eyes_cascade.detectMultiScale(gray, 2, 5) # .detectMultiScale(img_name,scake_factor,min_neighbours)

found = 0 # if we do no find any eyes
for (x, y, w, h) in eyes: # we get the coordinates for the eyes and we draw the rectangle
    cv2.rectangle(gray, (x, y), (x + w, y + h), (125, 155, 155), 3)
    found = 1 # we found the eyes
    break

if found == 0: # if we do not find eyes
    print("not found")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA) # this converts the image into alpha
specs = cv2.resize(specs, (w, h)) # this will resize the specs according to the heights
 
w, h, c = specs.shape

for width_eyes in range(0, w): # this loop will resize until perfect match is not found
    for height_eyes in range(0, h):

        if specs[width_eyes, height_eyes][3] != 0:
            img[y + width_eyes, x + height_eyes] = specs[width_eyes, height_eyes]
cv2.imshow('thughlife',img)
cv2.imwrite('thglife.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()