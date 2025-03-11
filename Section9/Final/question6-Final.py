# 6. یک فایل متنی حاوی لیستی از محصولات و قیمت آنها ایجاد کنید. سپس گران ترین و ارزان ترین محصولات را از فایل استخراج کرده و چاپ کنید.

# لیستی از محصولات و قیمت‌های آن‌ها
products_and_prices = [
    ("محصول 1", 15000),
    ("محصول 2", 30000),
    ("محصول 3", 20000),
    ("محصول 4", 50000),
    ("محصول 5", 10000),
]

# ایجاد فایل و نوشتن نام محصولات و قیمت‌ها در فایل
with open("products_and_prices.txt", "w") as file:
    for product, price in products_and_prices:
        file.write(f"{product}: {price} تومان\n")


# خواندن داده‌ها از فایل
with open("products_and_prices.txt", "r") as file:
    lines = file.readlines()

# تبدیل داده‌ها به لیستی از tuples (محصول، قیمت)
products_and_prices_from_file = []
for line in lines:
    product, price = line.strip().split(": ")
    price = int(price.split()[0])  # تبدیل قیمت به عدد
    products_and_prices_from_file.append((product, price))

# پیدا کردن گران‌ترین و ارزان‌ترین محصول
max_price_product = max(products_and_prices_from_file, key=lambda x: x[1])
min_price_product = min(products_and_prices_from_file, key=lambda x: x[1])

# چاپ گران‌ترین و ارزان‌ترین محصولات
print(f"گران‌ترین محصول: {max_price_product[0]} - {max_price_product[1]} تومان")
print(f"ارزان‌ترین محصول: {min_price_product[0]} - {min_price_product[1]} تومان")
