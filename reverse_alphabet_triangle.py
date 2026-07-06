n = 5

for i in range(1, n + 1):
    ch = ord('A') + n - 1
    for j in range(i):
        print(chr(ch - j), end="")
    print()
