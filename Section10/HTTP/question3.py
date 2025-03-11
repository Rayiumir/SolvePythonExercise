import requests  # ایمپورت کتابخانه

# ارسال درخواست GET به API کاربران
response = requests.get("https://jsonplaceholder.typicode.com/users")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    print("لیست کاربران:")
    for user in data:
        print(f"نام: {user['name']}, ایمیل: {user['email']}")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# لیست کاربران:
# نام: Leanne Graham, ایمیل: Sincere@april.biz
# نام: Ervin Howell, ایمیل: Shanna@melissa.tv
# نام: Clementine Bauch, ایمیل: Nathan@yesenia.net
# نام: Patricia Lebsack, ایمیل: Julianne.OConner@kory.org
# نام: Chelsey Dietrich, ایمیل: Lucio_Hettinger@annie.ca
# نام: Mrs. Dennis Schulist, ایمیل: Karley_Dach@jasper.info
# نام: Kurtis Weissnat, ایمیل: Telly.Hoeger@billy.biz
# نام: Nicholas Runolfsdottir V, ایمیل: Sherwood@rosamond.me
# نام: Glenna Reichert, ایمیل: Chaim_McDermott@dana.io
# نام: Clementina DuBuque, ایمیل: Rey.Padberg@karina.biz
