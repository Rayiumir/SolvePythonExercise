#5. تشخیص خودرو در تصویر با استفاده از haarcascade_car.xml

import cv2

# بارگذاری مدل تشخیص چهره
car_cascade = cv2.CascadeClassifier("https://github.com/souravdeyone/OpenCV-Reference/blob/master/Haarcascades/haarcascade_car.xml")

image = cv2.imread("car.jpg")  # جایگزین با مسیر تصویر خود
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# تشخیص عکس ها
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

# رسم مستطیل دور عکس های شناسایی‌ شده
for (x, y, w, h) in cars:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# نمایش تصویر
cv2.imshow("Detected Cars", image)
cv2.waitKey(0)
cv2.destroyAllWindows()