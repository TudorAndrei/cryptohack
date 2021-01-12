from pwn import xor

a = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

a = bytes.fromhex(a)


print(xor(a, 42))
