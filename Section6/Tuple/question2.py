# دریافت یک tuple از کاربر
numbers = tuple(map(int, input("اعداد را با فاصله وارد کنید: ").split()))

# دریافت مقدار مورد نظر برای جستجو
target = int(input("عدد مورد نظر را وارد کنید: "))

# بررسی وجود مقدار در tuple
if target in numbers:
    print(f"عدد {target} در tuple وجود دارد.")
else:
    print(f"عدد {target} در tuple وجود ندارد.")

# --------------------------
# ورودی نمونه:
# 10 20 30 40 50
# 30
# خروجی:
# عدد 30 در tuple وجود دارد.
# --------------------------
