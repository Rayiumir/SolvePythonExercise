# 4. یک فایل متنی حاوی نام محصولات و قیمت ها ایجاد کنید، سپس تمام قیمت ها را 10% افزایش دهید و فایل را به روز کنید.

# ایجاد فایل و نوشتن اطلاعات محصولات و قیمت‌ها
products = [
    ("محصول اول", 10000),
    ("محصول دوم", 15000),
    ("محصول سوم", 20000),
]

with open("products.txt", "w") as file:
    for product, price in products:
        file.write(f"{product}: {price} تومان\n")

# افزایش 10% قیمت‌ها و نوشتن مجدد اطلاعات در فایل
with open("products.txt", "r") as file:
    lines = file.readlines()

# ایجاد فایل جدید با قیمت‌های به روز
with open("products.txt", "w") as file:
    for line in lines:
        parts = line.split(": ")
        product = parts[0]
        price = int(parts[1].replace(" تومان\n", ""))
        new_price = price * 1.10  # افزایش 10%
        file.write(f"{product}: {new_price:.0f} تومان\n")

