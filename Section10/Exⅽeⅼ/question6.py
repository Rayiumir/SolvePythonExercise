from openpyxl import Workbook

# ایجاد یک شیء Workbook
wb = Workbook()
ws = wb.active
ws.title = "روزهای هفته"

# لیست روزهای هفته
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# اضافه کردن عنوان ستون‌ها
ws.append(["نام روز", "دارای حرف A؟"])

# افزودن داده‌ها و بررسی وجود حرف "A" یا "a"
for day in days:
    has_a = "✔" if "a" in day.lower() else "✘"
    ws.append([day, has_a])

# ذخیره فایل اکسل
wb.save("weekdays_with_A.xlsx")

print("فایل اکسل با موفقیت ایجاد شد.")
