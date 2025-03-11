from openpyxl import Workbook

# ایجاد یک شیء Workbook
wb = Workbook()

# انتخاب برگه فعال
ws = wb.active
ws.title = "دانش‌آموزان"

# وارد کردن نام دانش‌آموزان و نمرات آنها
students = [
    ("علی", 85),
    ("سارا", 90),
    ("محمد", 78),
    ("مریم", 92),
    ("حسین", 80)
]

# وارد کردن داده‌ها به اکسل
ws.append(["نام", "نمره"])  # عنوان ستون‌ها
for student in students:
    ws.append(student)

# وارد کردن فرمول برای محاسبه نمره متوسط در سلول B7
ws["B7"] = "=AVERAGE(B2:B6)"

# ذخیره فایل اکسل
wb.save("students_scores_with_average.xlsx")

# پیامی که نشان دهد فایل ذخیره شده است
print("فایل اکسل با موفقیت ذخیره شد.")
