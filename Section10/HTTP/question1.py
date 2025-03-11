import requests  # ایمپورت کتابخانه

# ارسال درخواست GET
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    for post in data[:5]:  # فقط 5 مورد اول را نمایش می‌دهیم تا خروجی طولانی نشود
        print(f"شناسه: {post['id']}, عنوان: {post['title']}\n")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# شناسه: 1, عنوان: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
#
# شناسه: 2, عنوان: qui est esse
#
# شناسه: 3, عنوان: ea molestias quasi exercitationem repellat qui ipsa sit aut
#
# شناسه: 4, عنوان: eum et est occaecati
#
# شناسه: 5, عنوان: nesciunt quas odio
