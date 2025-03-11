import csv
from collections import defaultdict
from datetime import datetime

# نام فایل CSV که شامل اطلاعات فروش ماهانه است
csv_filename = "monthly_sales.csv"

# دیکشنری‌ها برای ذخیره فروش سالیانه و فصلی
yearly_sales = defaultdict(float)
seasonal_sales = defaultdict(lambda: defaultdict(float))

# خواندن فایل CSV
with open(csv_filename, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # خواندن هدر (نام ستون‌ها)

    for row in reader:
        date_str, sales = row[0], float(row[1])  # استخراج تاریخ و مقدار فروش
        date_obj = datetime.strptime(date_str, "%Y-%m")  # تبدیل رشته به تاریخ
        year = date_obj.year  # استخراج سال
        month = date_obj.month  # استخراج ماه

        # تعیین فصل بر اساس ماه
        if month in [12, 1, 2]:
            season = "Winter"
        elif month in [3, 4, 5]:
            season = "Spring"
        elif month in [6, 7, 8]:
            season = "Summer"
        else:
            season = "Fall"

        # ذخیره داده‌ها
        yearly_sales[year] += sales
        seasonal_sales[year][season] += sales

# نمایش روند سالیانه
print("فروش سالیانه:")
for year, total_sales in sorted(yearly_sales.items()):
    print(f"سال {year}: {total_sales:.2f}")

# نمایش روند فصلی
print("\nفروش فصلی:")
for year, seasons in sorted(seasonal_sales.items()):
    print(f"سال {year}:")
    for season, sales in seasons.items():
        print(f"  - {season}: {sales:.2f}")

# نمونه خروجی:
# فروش سالیانه:
# سال 2022: 125000.50
# سال 2023: 139800.75
#
# فروش فصلی:
# سال 2022:
#   - Winter: 30000.00
#   - Spring: 32000.50
#   - Summer: 35000.00
#   - Fall: 28000.00
# سال 2023:
#   - Winter: 31000.75
#   - Spring: 33000.00
#   - Summer: 40000.00
