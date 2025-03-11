import requests  # ایمپورت کتابخانه

# ارسال درخواست GET برای دریافت اطلاعات آخرین پرتاب فضایی
response = requests.get("https://api.spacexdata.com/v4/launches")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    latest_launch = data[0]  # اولین پرتاب (آخرین پرتاب)
    launch_name = latest_launch["name"]  # نام پرتاب
    launch_date = latest_launch["date_utc"]  # تاریخ پرتاب
    launch_success = latest_launch["success"]  # وضعیت موفقیت
    print(f"نام پرتاب: {launch_name}")
    print(f"تاریخ پرتاب: {launch_date}")
    print(f"موفقیت پرتاب: {'موفق' if launch_success else 'ناموفق'}")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# نام پرتاب: Falcon 9 Block 5 | Starlink 4-9
# تاریخ پرتاب: 2023-02-17T00:30:00Z
# موفقیت پرتاب: موفق
