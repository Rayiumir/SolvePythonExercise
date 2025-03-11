from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from datetime import datetime
import jdatetime  # برای کار با تاریخ شمسی

# ایجاد فایل اکسل جدید
wb = Workbook()
ws = wb.active
ws.title = "تاریخ‌ها"

# افزودن عنوان ستون‌ها
ws.append(["تاریخ میلادی", "تاریخ شمسی", "ماه"])

# لیست تاریخ‌های نمونه (میلادی)
dates = [
    datetime(2024, 1, 5),
    datetime(2023, 12, 28),
    datetime(2024, 1, 15),
    datetime(2024, 2, 1),
    datetime(2023, 12, 22),
    datetime(2024, 1, 10),
    datetime(2024, 7, 19),
]

# افزودن تاریخ‌ها به اکسل
for date in dates:
    shamsi_date = jdatetime.datetime.fromgregorian(datetime=date)  # تبدیل میلادی به شمسی
    month_name = shamsi_date.strftime("%B")  # نام ماه شمسی
    ws.append([date.strftime("%Y-%m-%d"), shamsi_date.strftime("%Y-%m-%d"), month_name])

# ذخیره فایل اکسل
file_name = "dates.xlsx"
wb.save(file_name)

print(f"فایل '{file_name}' با موفقیت ذخیره شد.")
