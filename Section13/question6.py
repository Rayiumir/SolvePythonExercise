# 6. دریافت فریم‌های ویدئو و نمایش تعداد اشیا در هر فریم:

import cv2

# بارگذاری ویدئو
video = cv2.VideoCapture("1.mp4")

#خواندن و نمایش تعداد اشیا در هر فریم 
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = cv2.Canny(gray, 50, 150)
    
    cv2.imshow("Objects in Frame", objects)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# نمایش ویدئو
video.release()
cv2.destroyAllWindows()