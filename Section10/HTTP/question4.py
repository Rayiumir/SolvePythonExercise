import requests  # ایمپورت کتابخانه
from PIL import Image  # ایمپورت کتابخانه برای نمایش تصویر
# با این دستور نصب کنید pip install Pillow
from io import BytesIO  # تبدیل داده‌های دریافتی به تصویر

# ارسال درخواست GET برای دریافت لینک تصویر تصادفی از سگ‌ها
response = requests.get("https://dog.ceo/api/breeds/image/random")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    image_url = data["message"]  # دریافت لینک تصویر
    print("لینک تصویر:", image_url)

    # دانلود تصویر
    img_response = requests.get(image_url)

    if img_response.status_code == 200:
        image = Image.open(BytesIO(img_response.content))  # تبدیل داده به تصویر
        image.show()  # نمایش تصویر
    else:
        print("خطا در دریافت تصویر!")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# لینک تصویر: https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg
# (نمایش تصویر سگ)
