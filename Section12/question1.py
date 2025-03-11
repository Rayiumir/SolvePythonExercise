import csv  # ایمپورت کتابخانه CSV برای کار با فایل‌های CSV

# مسیر فایل CSV (فرض می‌کنیم فایل "data.csv" در همان مسیر قرار دارد)
filename = "data.csv"

# باز کردن فایل CSV برای خواندن
with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)  # خواندن فایل با استفاده از csv.reader
    header = next(csv_reader)  # خواندن سرستون‌ها (اولین سطر)
    print("سرستون‌ها:", header)

    # خواندن بقیه سطرها و چاپ آنها
    for row in csv_reader:
        print("ردیف:", row)

# نمونه ورودی (محتوای فایل data.csv):
# Name,Age,Gender
# Ali,30,Male
# Sara,25,Female
# Ahmad,35,Male
#
# نمونه خروجی:
# سرستون‌ها: ['Name', 'Age', 'Gender']
# ردیف: ['Ali', '30', 'Male']
# ردیف: ['Sara', '25', 'Female']
# ردیف: ['Ahmad', '35', 'Male']
