# 2. یک تاپل را معکوس کنید و آن را به یک لیست تبدیل کنید

def reverse_tuple_to_list(t):
    return list(t[::-1])

t = (1, 2, 3, 4)
print(reverse_tuple_to_list(t))  

# Output: [4, 3, 2, 1]


