import cv2 as cv

img = cv.imread('Photos/Cat03.jpg')
cv.imshow('Cat',img)

#average
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#gaussian
gauss = cv.GaussianBlur(img,(7,7), 0)
cv.imshow('Gaussian', gauss)

#Median Blur
median  =cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

#bilateral
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)