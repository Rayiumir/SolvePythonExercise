import json

# آدرس فایل JSON که اطلاعات کارمندان در آن ذخیره می‌شود
file_path = 'employees.json'

# خواندن اطلاعات از فایل JSON
with open(file_path, 'r', encoding='utf-8') as file:
    employees = json.load(file)

# افزایش حقوق به ۱۰ درصد
for employee in employees:
    employee['حقوق'] *= 1.1  # افزایش ۱۰ درصدی حقوق

# ذخیره اطلاعات به روز شده در همان فایل JSON
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(employees, file, ensure_ascii=False, indent=4)

# نمایش اطلاعات به روز شده
print("اطلاعات کارمندان با حقوق جدید:")
for employee in employees:
    print(f"نام: {employee['نام']}, سمت: {employee['سمت']}, حقوق: {employee['حقوق']:.2f}")

# خروجی:
# اطلاعات کارمندان با حقوق جدید:
# نام: علی, سمت: مدیر, حقوق: 5500000.00
# نام: مهدی, سمت: برنامه‌نویس, حقوق: 4400000.00
# نام: سارا, سمت: تحلیلگر داده, حقوق: 4950000.00
# نام: فاطمه, سمت: مدیر پروژه, حقوق: 6600000.00
