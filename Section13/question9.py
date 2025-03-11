# 9. تشخیص گوشه‌ها با الگوریتم Harris Corner Detection در OpenCV

import cv2
import numpy as np

# خواندن تصویر
image = cv2.imread("1.jpg")  # مسیر تصویر خود را جایگزین کنید
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # تبدیل به سطح خاکستری

# اعمال الگوریتم Harris Corner Detection
gray = np.float32(gray)
harris_corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# افزایش نواحی گوشه‌ای برای نمایش بهتر
harris_corners = cv2.dilate(harris_corners, None)

# نمایش نقاط گوشه‌ای روی تصویر اصلی (به رنگ قرمز)
image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

# نمایش تصویر خروجی
cv2.imshow("Harris Corners", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
