import csv  # ایمپورت کتابخانه CSV برای کار با فایل‌های CSV

# لیست داده‌ها (دیکشنری‌ها) که قرار است در فایل CSV نوشته شوند
data = [
    {"Name": "Ali", "Age": 30, "Gender": "Male"},
    {"Name": "Sara", "Age": 25, "Gender": "Female"},
    {"Name": "Ahmad", "Age": 35, "Gender": "Male"}
]

# نام فایل CSV که می‌خواهیم در آن داده‌ها را ذخیره کنیم
filename = "output.csv"

# باز کردن فایل CSV به صورت نوشتن
with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    # گرفتن کلیدهای اولین دیکشنری به عنوان سرستون (فرض بر این است که همه دیکشنری‌ها کلیدهای یکسانی دارند)
    fieldnames = data[0].keys()

    # ایجاد شیء DictWriter با استفاده از کلیدها
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # نوشتن سرستون‌ها در فایل
    writer.writeheader()

    # نوشتن هر دیکشنری به عنوان یک ردیف در فایل CSV
    for item in data:
        writer.writerow(item)

print(f"داده‌ها با موفقیت در فایل '{filename}' نوشته شدند.")

# نمونه ورودی:
# [
#     {"Name": "Ali", "Age": 30, "Gender": "Male"},
#     {"Name": "Sara", "Age": 25, "Gender": "Female"},
#     {"Name": "Ahmad", "Age": 35, "Gender": "Male"}
# ]
#
# نمونه خروجی (محتوای فایل output.csv):
# Name,Age,Gender
# Ali,30,Male
# Sara,25,Female
# Ahmad,35,Male
