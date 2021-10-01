import cv2

img = "Money-Heist.jpg"
img1 = cv2.imread(img)

gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


Inverted_gray_image = 255 - gray_image


blurred_img = cv2.GaussianBlur(Inverted_gray_image, (21,21), 0)

Inverted_blurred_img = 255 - blurred_img

pencil_img = cv2.divide(gray_image, Inverted_blurred_img, scale=256.0)

cv2.imshow('Image1',img1)
cv2.imshow('Image',pencil_img)
#cv2.waitKeyEx(0)
