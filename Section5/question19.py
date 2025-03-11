# 19. دنباله زمانی با استفاده از حلقه while 

def countdown(n): # با استفاده از حلقه while از n تا 0 معکوس شمارش می کند.
    while n >= 0:
        print(n)
        n -= 1

# نمونه استفاده:
countdown(5)

# Output
# 5
# 4
# 3
# 2
# 1
# 0
