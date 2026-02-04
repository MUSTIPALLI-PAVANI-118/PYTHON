a, b = 0, 1
print("First 10 Fibonacci numbers:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
