import requests  # ایمپورت کتابخانه

# ارسال درخواست GET برای دریافت تمام آلبوم‌ها
response = requests.get("https://jsonplaceholder.typicode.com/albums")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    user_1_albums = [album for album in data if album['userId'] == 1]  # فیلتر کردن آلبوم‌ها برای کاربر شماره ۱

    print("آلبوم‌های مربوط به کاربر شماره ۱:")
    for album in user_1_albums:
        print(f"عنوان آلبوم: {album['title']}")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# آلبوم‌های مربوط به کاربر شماره ۱:
# عنوان آلبوم:quidem molestiae enim
# عنوان آلبوم: sunt qui excepturi placeat culpa
# عنوان آلبوم: animi autem
# ...
