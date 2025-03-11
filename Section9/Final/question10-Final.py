# 10. یک فایل متنی حاوی اطلاعات مربوط به یک پروژه (نام پروژه، تاریخ شروع، تاریخ پایان) ایجاد کنید. سپس، مدت زمان پروژه را برای هر پروژه محاسبه کنید.

from datetime import datetime

# لیستی از پروژه‌ها به همراه نام پروژه، تاریخ شروع و تاریخ پایان
projects = [
    ("پروژه 1", "2025-01-01", "2025-01-10"),
    ("پروژه 2", "2025-02-01", "2025-02-20"),
    ("پروژه 3", "2025-03-01", "2025-03-15"),
]

# ایجاد فایل و نوشتن اطلاعات پروژه‌ها در آن
with open("projects.txt", "w") as file:
    for project in projects:
        file.write(f"{project[0]}: {project[1]} - {project[2]}\n")

# خواندن اطلاعات پروژه‌ها از فایل
with open("projects.txt", "r") as file:
    lines = file.readlines()

# محاسبه مدت زمان برای هر پروژه و چاپ آن
print("مدت زمان هر پروژه:")
for line in lines:
    # استخراج نام پروژه، تاریخ شروع و تاریخ پایان
    project_name, dates = line.split(": ")
    start_date_str, end_date_str = dates.split(" - ")
    
    # تبدیل تاریخ‌ها به شیء datetime
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str.strip(), "%Y-%m-%d")
    
    # محاسبه مدت زمان پروژه
    duration = (end_date - start_date).days
    
    # چاپ نتیجه
    print(f"{project_name.strip()}: {duration} روز")
