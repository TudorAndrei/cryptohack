from pwn import xor
import codecs

obj1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
obj2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
obj3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
obj4 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

obj1 = bytes.fromhex(obj1)
obj2 = bytes.fromhex(obj2)
obj3 = bytes.fromhex(obj3)
obj4 = bytes.fromhex(obj4)

key2 = xor(obj1, obj2)
key3 = xor(obj3, key2)

flag = xor(key2, obj4)
flag = xor(flag, key3)
flag = xor(flag, obj1)
result = "".join([chr(x) for x in list(flag)])
print(result)
