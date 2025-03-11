import csv
from collections import defaultdict

# نام فایل CSV که شامل اطلاعات خرید و فروش کالاها است
csv_filename = "products_sales.csv"

# دیکشنری برای ذخیره سود هر محصول و سود هر دسته‌بندی
product_profit = {}
category_profit = defaultdict(float)

# خواندن فایل CSV
with open(csv_filename, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # خواندن هدر (نام ستون‌ها)

    for row in reader:
        product_name = row[0]  # نام محصول
        category = row[1]  # دسته‌بندی
        buy_price = float(row[2])  # قیمت خرید
        sell_price = float(row[3])  # قیمت فروش
        quantity = int(row[4])  # تعداد فروخته شده

        # محاسبه سود خالص محصول
        profit = (sell_price - buy_price) * quantity
        product_profit[product_name] = profit

        # اضافه کردن سود به دسته‌بندی مربوطه
        category_profit[category] += profit

# نمایش سود خالص هر محصول
print("سود خالص هر محصول")
print("-" * 40)
for product, profit in product_profit.items():
    print(f"{product}: {profit:.2f}")

# نمایش سود خالص هر دسته‌بندی
print("\nسود خالص هر دسته‌بندی")
print("-" * 40)
for category, total_profit in category_profit.items():
    print(f"{category}: {total_profit:.2f}")

# نمونه خروجی:
# سود خالص هر محصول
# ----------------------------------------
# لپ‌تاپ ایسوس: 5000000.00
# گوشی سامسونگ: 3200000.00
# تلویزیون ال‌جی: 4500000.00

# سود خالص هر دسته‌بندی
# ----------------------------------------
# الکترونیک: 12700000.00
