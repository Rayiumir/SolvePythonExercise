# 9. یک فایل متنی ایجاد کنید که برای هر خط تاریخ و زمان فعلی به آن اضافه کنید.

from datetime import datetime

# لیستی از خطوط برای اضافه کردن تاریخ و زمان
lines = [
    "این اولین خط است.",
    "این دومین خط است.",
    "این سومین خط است."
]

# ایجاد و نوشتن تاریخ و زمان به هر خط
with open("datetime_lines.txt", "w") as file:
    for line in lines:
        # دریافت تاریخ و زمان فعلی
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{line} - {current_datetime}\n")
