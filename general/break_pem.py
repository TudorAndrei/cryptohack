import base64

f = open("./misc/privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem", "r")

file = f.read()
f.close()
file = file.split("\n")
file = file[1:-2]
result = []

for line in file:
    aux = base64.b64decode(line)
    print(aux)
    aux = list(aux)
