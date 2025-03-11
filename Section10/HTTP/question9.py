import requests  # ایمپورت کتابخانه

# ارسال درخواست GET برای دریافت لیست نژادهای سگ‌ها
response = requests.get("https://dog.ceo/api/breeds/list/all")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    breeds = data["message"]  # نژادهای سگ‌ها
    print("لیست نژادهای سگ‌ها:")
    for breed in breeds:
        print(f"- {breed}")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# لیست نژادهای سگ‌ها:
# - bulldog
# - dalmatian
# - terrier
# - spaniel
# - poodle
# - ...
