# 1. اعداد فیبوناچی ساده

def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# نمونه استفاده :

print("Simple Fibonacci numbers(first 10 numbers):", fibonacci(10))

# Output > Simple Fibonacci numbers(first 10 numbers): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]