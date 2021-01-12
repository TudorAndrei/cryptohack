string = 'label'
restul = [x for x in string]
result = "".join([chr(ord(x) ^ 13) for x in restul])
print("crypto{}".format(result))
