# ایجاد دی‌کشنری اولیه
students_scores = {
    "Ali": 85,
    "Sara": 90,
    "Nima": 75,
    "Bahram": 80,
    "Bita": 95,
    "Reza": 88
}

# اضافه کردن کلیدهایی که حروف اول آنها "B" یا "b" هستند
new_entries = {
    "Bahar": 70,
    "Benyamin": 65
}

for key, value in new_entries.items():
    if key[0].lower() == 'b':
        students_scores[key] = value

# نمایش دی‌کشنری نهایی
print("دی‌کشنری نهایی:", students_scores)

# نمونه خروجی:
# دی‌کشنری نهایی: {'Ali': 85, 'Sara': 90, 'Nima': 75, 'Bahram': 80, 'Bita': 95, 'Reza': 88, 'Bahar': 70, 'Benyamin': 65}
