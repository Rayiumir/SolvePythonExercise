# 1. یک فایل متنی ایجاد کنید که شامل لیستی از ایمیل ها باشد و برنامه ای بنویسید که ایمیل هایی از دامنه خاص هستند را فیلتر کرده و چاپ کند.

# لیستی از ایمیل‌ها
emails = [
    "john.doe@example.com",
    "alice.smith@domain.com",
    "bob.jones@example.com",
    "carol.white@domain.com",
    "david.brown@otherdomain.com",
]

# ایجاد فایل و نوشتن ایمیل‌ها در آن
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

# دامنه خاص برای فیلتر کردن
domain = "@domain.com"

# خواندن ایمیل‌ها از فایل
with open("emails.txt", "r") as file:
    email_list = file.readlines()

# فیلتر کردن ایمیل‌هایی که دامنه خاص دارند
filtered_emails = [email.strip() for email in email_list if domain in email]

# چاپ ایمیل‌های فیلتر شده
print("ایمیل‌هایی که از دامنه خاص هستند:")
for email in filtered_emails:
    print(email)
