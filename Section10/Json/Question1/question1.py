import json

file_name = "./user_data.json"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        user_data = json.load(file)

    print("اطلاعات کاربر:")
    for key, value in user_data.items():
        print(f"{key}: {value}")

except FileNotFoundError:
    print(f"فایل '{file_name}' یافت نشد")
except json.JSONDecodeError:
    print(f"خطا در خواندن فایل JSON. لطفاً ساختار فایل را بررسی کنید")

# خروجی مورد انتظار در صورتی که فایل JSON به درستی خوانده شود:
# اطلاعات کاربر:
# نام: علی
# سن: 25
# شهر: اصفهان
