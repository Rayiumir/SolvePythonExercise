# 9. دو دیکشنری شامل اطلاعات مشابه بسازید و مواردی که هر دو مشترک هستند را پیدا کنید.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 3}

common_items = {k: dict1[k] for k in dict1 if k in dict2 and dict1[k] == dict2[k]}
print(common_items)

# Output > {'b': 2}