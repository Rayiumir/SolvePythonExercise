import requests  # ایمپورت کتابخانه

# مشخص کردن مختصات جغرافیایی تهران
latitude = 35.6892
longitude = 51.3890

# ارسال درخواست GET به Open-Meteo برای دریافت وضعیت آب‌وهوا
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = requests.get(url)

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    weather = data["current_weather"]
    temperature = weather["temperature"]  # دما
    windspeed = weather["windspeed"]  # سرعت باد

    print(f"وضعیت آب‌وهوا: دما {temperature}°C و سرعت باد {windspeed} km/h")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# وضعیت آب‌وهوا: دما 18.5°C و سرعت باد 10.2 km/h
