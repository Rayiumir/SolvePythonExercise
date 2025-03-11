import csv  # ایمپورت کتابخانه CSV

# مسیر فایل CSV (فرض می‌کنیم فایل students.csv در همان مسیر قرار دارد)
filename = "students.csv"

# شمارش تعداد رکوردها (بدون سرستون)
row_count = 0

# باز کردن فایل CSV برای خواندن
with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader, None)  # خواندن سطر اول به عنوان سرستون (در صورت وجود)
    for row in reader:
        row_count += 1

print(f"تعداد دانش‌آموزان: {row_count}")

# نمونه ورودی (محتوای فایل students.csv):
# Name,Age,Grade
# Ali,15,10
# Sara,14,9
# Reza,16,11
#
# نمونه خروجی:
# تعداد دانش‌آموزان: 3
