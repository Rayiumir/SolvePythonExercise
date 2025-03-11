import csv  # ایمپورت کتابخانه CSV برای کار با فایل‌های CSV
from tabulate import tabulate  # ایمپورت کتابخانه tabulate برای نمایش جدول

# نام فایل CSV (فرض بر این است که فایل products.csv در همان مسیر قرار دارد)
filename = "products.csv"

# لیست خالی برای ذخیره رکوردها
products = []

# باز کردن فایل CSV و خواندن محتوا به صورت دیکشنری
with open(filename, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row)

# نمایش داده‌ها به صورت جدول
if products:
    print(tabulate(products, headers="keys", tablefmt="grid"))
else:
    print("فایلی حاوی رکورد نیست!")

# نمونه ورودی (محتوای فایل products.csv):
# ProductID,Name,Price,Quantity
# 101,Apple,1.20,50
# 102,Banana,0.80,100
# 103,Orange,1.00,80

# نمونه خروجی:
# +-------------+---------+---------+------------+
# | ProductID   | Name    | Price   | Quantity   |
# +=============+=========+=========+============+
# | 101         | Apple   | 1.20    | 50         |
# +-------------+---------+---------+------------+
# | 102         | Banana  | 0.80    | 100        |
# +-------------+---------+---------+------------+
# | 103         | Orange  | 1.00    | 80         |
# +-------------+---------+---------+------------+
