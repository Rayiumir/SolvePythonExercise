import json
import os

file_path = "products.json"

# بررسی وجود فایل
if not os.path.exists(file_path):
    print(f"فایل '{file_path}' یافت نشد.")
else:
    # خواندن داده‌ها از فایل JSON
    with open(file_path, "r", encoding="utf-8") as file:
        products = json.load(file)

    # افزایش ۱۰ درصدی قیمت محصولات
    for product in products:
        product["قیمت"] = int(product["قیمت"] * 1.1)

    # ذخیره تغییرات در همان فایل
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)

    print("قیمت محصولات ۱۰٪ افزایش یافت و فایل به‌روزرسانی شد.")

    # نمایش خروجی نهایی
    print("لیست به‌روزرسانی‌شده محصولات:")
    for product in products:
        print(f"{product['نام']}: {product['قیمت']} تومان")

# خروجی نمونه پس از اجرا:
# لپ‌تاپ: 22000000 تومان
# گوشی موبایل: 16500000 تومان
# هدفون: 550000 تومان
# مانیتور: 8800000 تومان
