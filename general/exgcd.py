p = 26513
q = 32321

u = 1
v = 1
c = True

while p * u + q * v != 1:
    print(u, v)
    if c:
        u += 1
        c = False
    else:
        v += 2
        c = True

print(u, v)
