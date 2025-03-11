# تعریف دو دی‌کشنری با اطلاعات مشابه
dict1 = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

dict2 = {
    "Alice": 25,
    "Bob": 28,
    "David": 40
}

# پیدا کردن تفاوت بین دو دی‌کشنری
# مقادیر در dict1 که در dict2 وجود ندارند یا متفاوت هستند
diff_dict1 = {key: value for key, value in dict1.items() if key not in dict2 or dict2[key] != value}

# مقادیر در dict2 که در dict1 وجود ندارند یا متفاوت هستند
diff_dict2 = {key: value for key, value in dict2.items() if key not in dict1 or dict1[key] != value}

# نمایش تفاوت‌ها
print("تفاوت‌ها در dict1:", diff_dict1)
print("تفاوت‌ها در dict2:", diff_dict2)

# نمونه خروجی:
# تفاوت‌ها در dict1: {'Charlie': 35}
# تفاوت‌ها در dict2: {'Bob': 28, 'David': 40}
