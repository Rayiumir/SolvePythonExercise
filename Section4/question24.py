import time
import sys

# لیست رنگ‌های ANSI برای تغییر رنگ
colors = [
    "\033[31m",  # قرمز
    "\033[32m",  # سبز
    "\033[33m",  # زرد
    "\033[34m",  # آبی
    "\033[35m",  # بنفش
    "\033[36m",  # فیروزه‌ای
    "\033[37m"  # سفید
]


# تابع برای نمایش متن متحرک
def moving_text(text, width, height, delay=0.1):
    # طول متن
    text_length = len(text)

    # حرکت متن به صورت افقی و عمودی
    while True:
        for i in range(width - text_length):
            # ایجاد فضای خالی برای حرکت افقی
            sys.stdout.write("\033[H")  # بازنشانی مکان چاپ
            # ایجاد خطوط خالی قبل از متن
            for _ in range(height):
                sys.stdout.write(" " * i + colors[i % len(colors)] + text + "\033[0m" + "\n")
            time.sleep(delay)
            sys.stdout.flush()  # برای چاپ به موقع متن


# ورودی از کاربر
text = input("متن دلخواه خود را وارد کنید: ")
width = 40  # عرض کنسول
height = 10  # ارتفاع کنسول

# اجرای نمایش متن متحرک
moving_text(text, width, height)

