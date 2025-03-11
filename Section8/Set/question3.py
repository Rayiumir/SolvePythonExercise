# تعریف یک set از رشته‌ها
my_set = {"Python", "Java", "JavaScript", "C#", "C++", "PHP", "Ruby"}

# حرف خاص که می‌خواهیم بررسی کنیم
specific_char = "J"

# یافتن رشته‌هایی که با حرف خاص شروع می‌شوند
filtered_set = {word for word in my_set if word.startswith(specific_char)}

# نمایش نتیجه
print("Set اصلی:", my_set)
print(f"رشته‌هایی که با '{specific_char}' شروع می‌شوند:", filtered_set)

# نمونه خروجی:
# Set اصلی: {'Python', 'Ruby', 'PHP', 'C++', 'Java', 'JavaScript', 'C#'}
# رشته‌هایی که با 'J' شروع می‌شوند: {'Java', 'JavaScript'}
