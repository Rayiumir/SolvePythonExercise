## روش اول

# دریافت لیست از رشته‌ها
strings = input("لطفاً رشته‌ها را با فاصله وارد کنید: ").split()

# پیدا کردن طولانی‌ترین رشته
longest_string = max(strings, key=len) # استفاده از متود max

# نمایش طولانی‌ترین رشته
print("طولانی‌ترین رشته:", longest_string)


# # روش دوم

# دریافت لیست از رشته‌ها
strings = input("لطفاً رشته‌ها را با فاصله وارد کنید: ").split()

# پیدا کردن طولانی‌ترین رشته با استفاده از حلقه for
longest_string = ""
for string in strings:
    if len(string) > len(longest_string):
        longest_string = string

# نمایش طولانی‌ترین رشته
print("طولانی‌ترین رشته:", longest_string)


# --------------------------
# نمونه ورودی:
# لطفاً رشته‌ها را با فاصله وارد کنید: سلام برنامه‌نویسی پایتون دوست‌داشتنی است
# --------------------------
# نمونه خروجی:
# طولانی‌ترین رشته: برنامه‌نویسی
# --------------------------
