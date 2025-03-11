# 1. تبدیل تصویر به سیاه و سفید:

import cv2

image = cv2.imread("1.jpg")  # جایگزین با مسیر تصویر خود
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()