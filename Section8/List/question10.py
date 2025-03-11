# ایجاد لیستی از رشته‌ها
words = ["Apple", "banana", "Apricot", "cherry", "avocado", "Mango"]

# فیلتر کردن رشته‌هایی که با حرف "A" یا "a" شروع می‌شوند
words_starting_with_a = [word for word in words if word.lower().startswith('a')]

# نمایش لیست‌ها
print("لیست رشته‌هایی که با 'A' یا 'a' شروع می‌شوند:", words_starting_with_a)

# نمونه خروجی:
# لیست رشته‌هایی که با 'A' یا 'a' شروع می‌شوند: ['Apple', 'Apricot', 'avocado']
