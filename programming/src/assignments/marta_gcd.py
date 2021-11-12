def gcd(a, b):
    k = 0
    x = 1
    while x != 0:
        x = a % b
        k = b
        a = b
        b = x
    return k


while True:
    m = int(input("Ievadiet m vērtību: "))
    n = int(input("Ievadiet n vērtību: "))
    while gcd(m, n) != 1:
        k = gcd(m, n)
        m //= k
        n //= k
    print("p =", int(m), "; q =", int(n))
    answer = int(input("Vai rēķināt vēl(0 - nē, 1 - jā)  "))
    if answer == 0:
        break
