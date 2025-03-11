import csv  # ایمپورت کتابخانه CSV برای کار با فایل‌های CSV

# نام فایل CSV که شامل نمرات دانش‌آموزان است
filename = "grades.csv"

total = 0   # برای جمع نمرات
count = 0   # شمارنده تعداد دانش‌آموزان

# باز کردن فایل CSV برای خواندن داده‌ها
with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # خواندن فایل به صورت دیکشنری
    for row in reader:
        try:
            grade = float(row["Grade"])  # تبدیل نمره به عدد اعشاری
            total += grade
            count += 1
        except ValueError:
            print("خطا در تبدیل نمره:", row["Grade"])

# محاسبه و چاپ میانگین نمرات در صورت وجود داده
if count > 0:
    average = total / count
    print("میانگین نمرات:", average)
else:
    print("هیچ نمره‌ای یافت نشد.")

# نمونه ورودی (محتوای فایل grades.csv):
# Name,Grade
# Ali,80
# Sara,90
# Reza,85
#
# نمونه خروجی:
# میانگین نمرات: 85.0
