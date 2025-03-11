import time
import random
import sys


# تابع برای رسم رودخانه با عرض مشخص
def draw_river(width, height):
    river = "~" * width

    # پاک کردن صفحه کنسول و رسم رودخانه
    sys.stdout.write("\033[H")  # بازنشانی مکان چاپ به بالا

    for _ in range(height):
        print(river)

    sys.stdout.flush()


# تابع برای تغییر عرض رودخانه به طور داینامیک
def dynamic_river(min_width, max_width, height, duration):
    start_time = time.time()  # شروع زمان

    while True:
        # محاسبه مدت زمان طی شده
        elapsed_time = time.time() - start_time

        # تغییر عرض رودخانه به طور تدریجی
        width = random.randint(min_width, max_width)

        draw_river(width, height)

        time.sleep(1.0)  # تأخیر برای ایجاد حرکت

        # بعد از مدت زمان مشخص، برنامه را متوقف کن
        if elapsed_time > duration:
            break


# ورودی از کاربر
height = 10  # ارتفاع رودخانه
min_width = 20  # حداقل عرض رودخانه
max_width = 50  # حداکثر عرض رودخانه
duration = 30  # مدت زمان اجرای برنامه (ثانیه)

# اجرای برنامه با تغییر عرض رودخانه به صورت داینامیک
dynamic_river(min_width, max_width, height, duration)
