# 10. 10. تشخیص چهره در ویدیو و شمارش تعداد چهره‌ها haarcascade_frontalface_default.xml

import cv2

# بارگذاری مدل تشخیص چهره
face_cascade = cv2.CascadeClassifier("https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml")

# خواندن ویدیو
video = cv2.VideoCapture("2.mp4")  # مسیر ویدیو خود را جایگزین کنید

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # تبدیل فریم به سطح خاکستری

    # تشخیص چهره‌ها
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # رسم مستطیل دور چهره‌ها
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # نمایش تعداد چهره‌ها
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # نمایش فریم
    cv2.imshow("Face Detection", frame)

    # خروج با فشردن کلید 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
