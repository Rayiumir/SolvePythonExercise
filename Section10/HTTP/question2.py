import requests  # ایمپورت کتابخانه

# ارسال درخواست GET به API گیت‌هاب
response = requests.get("https://api.github.com")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    print("اطلاعات مربوط به گیت‌هاب:")
    print(f"نسخه API: {data.get('current_user_url', 'نامشخص')}")
    print(f"آدرس گیت‌هاب: {data.get('html_url', 'نامشخص')}")
    print(f"توضیحات: {data.get('description', 'نامشخص')}")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# اطلاعات مربوط به گیت‌هاب:
# نسخه API: https://api.github.com/user
# آدرس گیت‌هاب: نامشخص
# توضیحات: نامشخص
