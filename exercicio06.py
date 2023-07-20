def algoritmo(num, n):
    if (num < n):
        for i in range(num, n + 1, 1):
            print(i)
    else:
        for i in range(num, n-1, -1):
            print(i)

