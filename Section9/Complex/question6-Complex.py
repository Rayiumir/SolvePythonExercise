# 6. یک فایل متنی حاوی لیستی از تاریخ مختلف ایجاد کنید، سپس روز هفته را برای هر تاریخ محاسبه کنید و آن را به انتها اضافه کنید.

from datetime import datetime

# ایجاد لیستی از تاریخ‌ها
dates = [
    "2025-02-06",
    "2024-12-25",
    "2023-08-15",
    "2022-11-01",
]

# ایجاد و نوشتن تاریخ‌ها در فایل
with open("dates.txt", "w") as file:
    for date in dates:
        file.write(date + "\n")

# خواندن تاریخ‌ها از فایل
with open("dates.txt", "r") as file:
    dates = file.readlines()

# ایجاد فایل جدید با روز هفته برای هر تاریخ
with open("dates.txt", "a") as file:
    file.write("\nروزهای هفته مربوط به تاریخ‌ها:\n")
    for date in dates:
        date_str = date.strip()  # حذف فاصله‌های اضافی
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # تبدیل به شی تاریخ
        day_of_week = date_obj.strftime("%A")  # گرفتن روز هفته
        file.write(f"{date_str}: {day_of_week}\n")
