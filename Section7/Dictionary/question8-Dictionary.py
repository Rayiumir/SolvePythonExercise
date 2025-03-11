# 8. یک دیکشنری شامل اعداد و مقادیرشان ایجاد کنید و فقط مقادیر زوج آنها را ذخیره کنید

data = {
    "Ali": [1, 2, 3, 4],
    "Sara": [10, 15, 20],
    "Reza": [3, 5, 8, 12]
}

even_values_dict = {name: [x for x in values if x % 2 == 0] for name, values in data.items()}
print(even_values_dict)

# Output > {'Ali': [2, 4], 'Sara': [10, 20], 'Reza': [8, 12]}