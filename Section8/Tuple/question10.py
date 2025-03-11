# ایجاد tuple از مقادیر رشته‌ای
words_tuple = ("Python", "Java", "C", "JavaScript", "Go", "Ruby", "Swift")

# پیدا کردن رشته‌هایی که بیشتر از ۴ حرف دارند
long_words = tuple(word for word in words_tuple if len(word) > 4)

# نمایش نتیجه
print("tuple از رشته‌ها:", words_tuple)
print("رشته‌هایی که بیشتر از ۴ حرف دارند:", long_words)

# نمونه خروجی:
# tuple از رشته‌ها: ('Python', 'Java', 'C', 'JavaScript', 'Go', 'Ruby', 'Swift')
# رشته‌هایی که بیشتر از ۴ حرف دارند: ('Python', 'JavaScript', 'Ruby', 'Swift')
