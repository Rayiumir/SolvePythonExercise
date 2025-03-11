# 13. تعیین کنید که اولین عدد در بین n و m بر k بخش پذیر است یا خیر

def is_multiple(m, n): # بررسی می کند که آیا m مضرب n است یا خیر.
    return m % n == 0

# Example usage:
m = 10
n = 5
print(f"{m} is a multiple of {n}: {is_multiple(m, n)}.")

# Output > 10 is a multiple of 5: True.


