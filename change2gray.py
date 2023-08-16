import cv2 as cv

img = cv.imread('photos/boston.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#Blur remove some noise
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# Edge Cascade // Canny edge detection technique

canny = cv.Canny(blur,125, 175)
cv.imshow("Canny", canny)

# Dilating the image 

dilated = cv.dilate(canny,(7,7), iterations=1)
cv.imshow('Dilated', dilated)

#eroding 

eroded = cv.erode(dilated,(3,3), iterations=1)
cv.imshow('Eroded', eroded)



#resize 

resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)

cv.imshow("resized", resized)
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)

 