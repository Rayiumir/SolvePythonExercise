# 1. چاپ اعداد فیبوناچی تا n

def fibonacci(n):
  """Prints the Fibonacci sequence up to n."""
  a, b = 0, 1
  while a <= n:
    print(a, end=" ")
    a, b = b, a + b

# نمونه استفاده:
fibonacci(200)

# Output > 0 1 1 2 3 5 8 13 21 34 55 89 144 % 
