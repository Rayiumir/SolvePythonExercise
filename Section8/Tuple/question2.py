# ایجاد یک tuple شامل سه tuple
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# استخراج مقادیر خاص از هر کدام
first_tuple_second_element = nested_tuple[0][1]  # دومین مقدار از اولین tuple
second_tuple_first_element = nested_tuple[1][0]  # اولین مقدار از دومین tuple
third_tuple_third_element = nested_tuple[2][2]   # سومین مقدار از سومین tuple

# نمایش نتایج
print("tuple اصلی:", nested_tuple)
print("دومین مقدار از اولین tuple:", first_tuple_second_element)
print("اولین مقدار از دومین tuple:", second_tuple_first_element)
print("سومین مقدار از سومین tuple:", third_tuple_third_element)

# نمونه خروجی:
# tuple اصلی: ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# دومین مقدار از اولین tuple: 2
# اولین مقدار از دومین tuple: 4
# سومین مقدار از سومین tuple: 9
