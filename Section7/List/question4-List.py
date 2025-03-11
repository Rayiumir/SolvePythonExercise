# 4. رشته های معکوس در یک لیست

def reverse_strings(strings):
    return [s[::-1] for s in strings]

# نمونه استفاده:
strings = ["hello", "world"]
print("Reversed strings:", reverse_strings(strings))

# Output > Reversed strings: ['olleh', 'dlrow']