# 5. یک فایل متنی بسازید و محتوای آن را با استفاده از برنامه درون یک متغییر ذخیره کنید

with open("products.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # کاراکترهای جدید در خط جدید را حذف می کند
