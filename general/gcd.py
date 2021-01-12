def gcd(a, b):
    while b:
        t = b
        b = a % b
        a = t
    return a


print(gcd(66528, 52920))
