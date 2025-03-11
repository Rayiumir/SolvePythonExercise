# 4. تشخیص چهره و رسم مستطیل دور آن haarcascade_frontalface_default.xml

import cv2
# بارگذاری مدل تشخیص چهره
face_cascade = cv2.CascadeClassifier("https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml")

# خواندن تصویر
image = cv2.imread("girl.jpeg")  # مسیر تصویر خود را جایگزین کنید
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # تبدیل تصویر به سطح خاکستری

# تشخیص چهره‌ها
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# رسم مستطیل دور چهره‌های شناسایی‌ شده
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# نمایش تصویر
cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
