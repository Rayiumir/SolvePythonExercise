import csv  # ایمپورت کتابخانه CSV

# نام فایل CSV که شامل اطلاعات فروشندگان است
filename = "vendors.csv"

# دریافت مقدار فروش مورد نظر از کاربر
threshold = float(input("مقدار فروش مورد نظر را وارد کنید: "))

# باز کردن فایل CSV و خواندن داده‌ها به صورت دیکشنری
with open(filename, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print(f"\nفروشندگانی که فروش آن‌ها بیشتر از {threshold} است:")
    for row in reader:
        try:
            sales = float(row["Sales"])
            if sales > threshold:
                print(f"نام فروشنده: {row['Name']}, فروش: {sales}")
        except ValueError:
            print("خطا در تبدیل مقدار فروش:", row["Sales"])

# نمونه ورودی (محتوای فایل vendors.csv):
# Name,Sales,Region
# Ali,1200,Tehran
# Sara,950,Isfahan
# Reza,1500,Shiraz
#
# نمونه خروجی:
# مقدار فروش مورد نظر را وارد کنید: 1000
#
# فروشندگانی که فروش آن‌ها بیشتر از 1000.0 است:
# نام فروشنده: Ali, فروش: 1200.0
# نام فروشنده: Reza, فروش: 1500.0
