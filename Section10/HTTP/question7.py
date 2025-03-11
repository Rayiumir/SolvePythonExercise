import requests  # ایمپورت کتابخانه

# ارسال درخواست GET برای دریافت قیمت بیت کوین
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    bitcoin_price = data["bpi"]["USD"]["rate"]  # قیمت بیت‌کوین به دلار
    print(f"قیمت بیت‌کوین: {bitcoin_price} USD")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# قیمت بیت‌کوین: 27,000.00 USD
