import json
from datetime import datetime

# آدرس فایل JSON که اطلاعات پروژه در آن ذخیره شده است
file_path = 'project.json'

# خواندن اطلاعات پروژه از فایل JSON
with open(file_path, 'r', encoding='utf-8') as file:
    project = json.load(file)

# دریافت تاریخ شروع و پایان از اطلاعات پروژه
start_date_str = project["تاریخ شروع"]
end_date_str = project["تاریخ پایان"]

# تبدیل تاریخ‌های رشته‌ای به شیء datetime (فرمت: YYYY-MM-DD)
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# محاسبه مدت زمان پروژه به صورت روز (تعداد روزهای بین تاریخ پایان و شروع)
duration_days = (end_date - start_date).days

# اضافه کردن کلید "مدت زمان پروژه" به اطلاعات پروژه
project["مدت زمان پروژه"] = duration_days

# ذخیره اطلاعات به روز شده در همان فایل JSON
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(project, file, ensure_ascii=False, indent=4)

# نمایش اطلاعات به روز شده پروژه
print("اطلاعات به روز شده پروژه:")
print(project)

# --------------------------
# نمونه محتویات اولیه فایل project.json:
# {
#     "نام پروژه": "پروژه نمونه",
#     "تاریخ شروع": "2023-01-01",
#     "تاریخ پایان": "2023-03-31"
# }
#
# نمونه خروجی پس از اجرای برنامه:
# اطلاعات به روز شده پروژه:
# {
#     "نام پروژه": "پروژه نمونه",
#     "تاریخ شروع": "2023-01-01",
#     "تاریخ پایان": "2023-03-31",
#     "مدت زمان پروژه": 89
# }
# --------------------------
