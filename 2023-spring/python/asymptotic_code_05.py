def f5(n):
    for i in range(0, n):
        k = 1
        while k < i:
            k *= 2
            print("!")

f5(10)