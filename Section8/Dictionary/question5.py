# ایجاد دی‌کشنری شامل نام‌ها و سن‌ها
ages = {
    "Ali": 25,
    "Sara": 35,
    "Reza": 40,
    "Nina": 28,
    "John": 32
}

# فیلتر کردن افراد بالای ۳۰ سال
older_than_30 = {name: age for name, age in ages.items() if age > 30}

# نمایش افراد بالای ۳۰ سال
print("افراد بالای ۳۰ سال:", older_than_30)

# نمونه خروجی:
# افراد بالای ۳۰ سال: {'Sara': 35, 'Reza': 40, 'John': 32}
