import csv
from collections import defaultdict

csv_file = "products.csv"

# دیکشنری برای ذخیره جمع قیمت‌ها و تعداد محصولات هر دسته‌بندی
category_prices = defaultdict(lambda: {"total_price": 0, "count": 0})

# خواندن داده‌ها از CSV
with open(csv_file, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        category = row["دسته‌بندی"]
        price = int(row["قیمت"])

        # افزودن به مجموع و شمارش تعداد محصولات
        category_prices[category]["total_price"] += price
        category_prices[category]["count"] += 1

# نمایش نتایج
for category, values in category_prices.items():
    total = values["total_price"]
    average = total / values["count"]
    print(f"دسته‌بندی: {category} | مجموع قیمت: {total:,} تومان | میانگین قیمت: {average:,.0f} تومان")

#  خروجی برنامه:
# دسته‌بندی: الکترونیکی | مجموع قیمت: 63,000,000 تومان | میانگین قیمت: 21,000,000 تومان
# دسته‌بندی: مبلمان | مجموع قیمت: 7,000,000 تومان | میانگین قیمت: 3,500,000 تومان
# دسته‌بندی: فرهنگی | مجموع قیمت: 450,000 تومان | میانگین قیمت: 225,000 تومان
