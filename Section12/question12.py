import csv
import json

# خواندن فایل CSV و تبدیل به JSON
csv_file = "data.csv"
json_file = "data.json"

with open(csv_file, encoding="utf-8") as f:
    reader = csv.DictReader(f)  # خواندن CSV به‌صورت دیکشنری
    data = list(reader)  # تبدیل به لیست دیکشنری‌ها

# ذخیره در فایل JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f" فایل JSON ذخیره شد: {json_file}")

from openpyxl import Workbook

# خواندن فایل CSV
csv_file = "data.csv"
excel_file = "data.xlsx"

wb = Workbook()
ws = wb.active  # ایجاد شیت اکسل

with open(csv_file, encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        ws.append(row)  # اضافه کردن هر ردیف به اکسل

# ذخیره فایل اکسل
wb.save(excel_file)
print(f" فایل Excel ذخیره شد: {excel_file}")
