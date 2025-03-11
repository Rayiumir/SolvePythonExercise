import csv
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

# نام فایل CSV که شامل اطلاعات درآمدهای روزانه است
csv_filename = "daily_sales.csv"

# دیکشنری برای ذخیره مجموع درآمد ماهانه
monthly_sales = defaultdict(float)
monthly_high_low = defaultdict(lambda: {"max": float('-inf'), "min": float('inf')})

# خواندن فایل CSV
with open(csv_filename, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # خواندن هدر (نام ستون‌ها)

    for row in reader:
        date_str, sales = row[0], float(row[1])  # استخراج تاریخ و مبلغ فروش
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # تبدیل رشته به تاریخ
        month_key = date_obj.strftime("%Y-%m")  # استخراج ماه به فرمت YYYY-MM

        # جمع‌بندی فروش ماهانه
        monthly_sales[month_key] += sales

        # پیدا کردن بالاترین و پایین‌ترین درآمد روزانه در هر ماه
        if sales > monthly_high_low[month_key]["max"]:
            monthly_high_low[month_key]["max"] = sales
        if sales < monthly_high_low[month_key]["min"]:
            monthly_high_low[month_key]["min"] = sales

# نمایش اطلاعات فروش ماهانه
print("گزارش درآمد ماهانه")
print("-" * 40)
for month, total_sales in sorted(monthly_sales.items()):
    high = monthly_high_low[month]["max"]
    low = monthly_high_low[month]["min"]
    print(
        f"{month}: مجموع درآمد = {total_sales:.2f}, بیشترین درآمد روزانه = {high:.2f}, کمترین درآمد روزانه = {low:.2f}")

# رسم نمودار درآمد ماهانه
months = list(sorted(monthly_sales.keys()))
sales_values = [monthly_sales[m] for m in months]

plt.figure(figsize=(10, 5))
plt.plot(months, sales_values, marker='o', linestyle='-', color='b', label="مجموع درآمد ماهانه")
plt.xlabel("ماه")
plt.ylabel("مجموع درآمد")
plt.title("نمودار درآمد ماهانه فروشگاه")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

# نمونه خروجی:
# گزارش درآمد ماهانه
# ----------------------------------------
# 2023-01: مجموع درآمد = 45000.00, بیشترین درآمد روزانه = 5000.00, کمترین درآمد روزانه = 1500.00
# 2023-02: مجموع درآمد = 47000.00, بیشترین درآمد روزانه = 5200.00, کمترین درآمد روزانه = 1800.00
