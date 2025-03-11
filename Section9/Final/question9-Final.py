# 9. یک فایل متنی ایجاد کنید و یک آدرس ایمیل در آن بنویسید. سپس آن را ویرایش کرده و نام کاربری و رمز عبور را به آن اضافه کنید.

# آدرس ایمیل اولیه
email = "user@example.com"

# ایجاد فایل و نوشتن آدرس ایمیل در آن
with open("email_info.txt", "w") as file:
    file.write(f"ایمیل: {email}\n")

# اطلاعات اضافی
username = "my_username"
password = "my_secure_password"

# ویرایش فایل و اضافه کردن نام کاربری و رمز عبور
with open("email_info.txt", "a") as file:
    file.write(f"نام کاربری: {username}\n")
    file.write(f"رمز عبور: {password}\n")

# چاپ محتویات فایل
with open("email_info.txt", "r") as file:
    print(file.read())
