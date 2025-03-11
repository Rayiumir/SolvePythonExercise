# 4. اولین و آخرین عنصر یک تاپل را با هم جابه جا کنید

def swap_first_last(t):
    if len(t) < 2:
        return t
    return (t[-1],) + t[1:-1] + (t[0],)

# نمونه استفاده
t = (1, 2, 3, 4)
print(swap_first_last(t))  

# Output: (4, 2, 3, 1)