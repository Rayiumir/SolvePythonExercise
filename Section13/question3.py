# 3. استفاده از الگوریتم Canny برای تشخیص لبه‌ها:

import cv2

image = cv2.imread("1.jpg")  # جایگزین با مسیر تصویر خود
edges = cv2.Canny(image, 100, 200)

cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
