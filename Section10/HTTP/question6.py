import requests  # ایمپورت کتابخانه

# ارسال درخواست GET به JSONPlaceholder
response = requests.get("https://jsonplaceholder.typicode.com/todos")

# بررسی موفقیت درخواست
if response.status_code == 200:
    data = response.json()  # تبدیل پاسخ به فرمت JSON
    for todo in data:
        if not todo["completed"]:  # اگر کار تکمیل نشده باشد
            print(f"عنوان: {todo['title']}, کاربر: {todo['userId']}, وضعیت: {todo['completed']}")
else:
    print("خطا در دریافت اطلاعات! کد وضعیت:", response.status_code)

# نمونه خروجی:
# عنوان: delectus aut autem, کاربر: 1, وضعیت: False
# عنوان: quis ut nam facilis et officia qui, کاربر: 1, وضعیت: False
# عنوان: fuga molestias quia, کاربر: 1, وضعیت: False
# عنوان: qui est esse, کاربر: 1, وضعیت: False
# عنوان: ea molestias quasi exercitationem repellat qui ipsa sit aut, کاربر: 1, وضعیت: False
