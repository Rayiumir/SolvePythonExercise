# 8. تشخیص الگورتیم (Contour Detection):

import cv2

# خواندن تصویر
image = cv2.imread("1.jpg")  # مسیر تصویر خود را جایگزین کنید
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # تبدیل به سطح خاکستری

# اعمال آستانه‌گذاری برای باینری کردن تصویر
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# یافتن الگورتیم کانتورها
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# رسم کانتورها روی تصویر اصلی
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# نمایش تصویر
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
