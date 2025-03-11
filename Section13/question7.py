# 7. چرخش تصویر به چپ و راست

import cv2

image = cv2.imread("1.jpg")  # جایگزین با مسیر تصویر خود

# چرخش 90 درجه به سمت چپ
rotated_left = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# چرخش 90 درجه به سمت راست
rotated_right = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Rotated Left", rotated_left)
cv2.imshow("Rotated Right", rotated_right)
cv2.waitKey(0)
cv2.destroyAllWindows()


