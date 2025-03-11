# 9. یک تاپل بسازید و تمام مقادیر بین دو عدد مشخص را از آن حذف کنید.

def remove_element(t, element):
    return tuple(x for x in t if x != element)

# نمونه استفاده
t = (1, 2, 3, 4)
print(remove_element(t, 2))  

# Output: (1, 3, 4)