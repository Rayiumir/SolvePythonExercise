import json

# آدرس فایل JSON که اطلاعات دانش‌آموزان در آن ذخیره شده
file_path = 'students.json'

# بارگذاری داده‌های فایل JSON
with open(file_path, 'r', encoding='utf-8') as file:
    students = json.load(file)

# استخراج دانش‌آموزانی که نمره بالای ۱۵ دارند
students_above_15 = [student for student in students if student['نمره'] > 15]

# نمایش نتیجه
print("دانش‌آموزانی که نمره بالای ۱۵ دارند:")
for student in students_above_15:
    print(f"نام: {student['نام']}, نمره: {student['نمره']}")

# خروجی
# دانش‌آموزانی که نمره بالای ۱۵ دارند:
# نام: علی, نمره: 18
# نام: سارا, نمره: 16
