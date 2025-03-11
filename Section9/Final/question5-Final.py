# 5. یک فایل متنی حاوی نام مشتریان و تاریخ خرید آنها ایجاد کنید. سپس، مشتریانی را که در تاریخ خاصی خرید کرده اند چاپ کنید.

# لیستی از نام مشتریان و تاریخ خرید آنها
customers_and_dates = [
    ("مشتری 1", "2025-02-06"),
    ("مشتری 2", "2025-01-15"),
    ("مشتری 3", "2025-02-06"),
    ("مشتری 4", "2024-12-25"),
    ("مشتری 5", "2025-02-06"),
]

# ایجاد فایل و نوشتن نام مشتریان و تاریخ خرید در فایل
with open("customers_and_dates.txt", "w") as file:
    for customer, date in customers_and_dates:
        file.write(f"{customer}: {date}\n")

# تاریخ خاص برای فیلتر کردن
specific_date = "2025-02-06"

# خواندن داده‌ها از فایل
with open("customers_and_dates.txt", "r") as file:
    lines = file.readlines()

# فیلتر کردن مشتریانی که در تاریخ خاص خرید کرده‌اند
customers_on_specific_date = [line.strip() for line in lines if specific_date in line]

# چاپ مشتریانی که در تاریخ خاص خرید کرده‌اند
print(f"مشتریانی که در تاریخ {specific_date} خرید کرده‌اند:")
for customer in customers_on_specific_date:
    print(customer)
