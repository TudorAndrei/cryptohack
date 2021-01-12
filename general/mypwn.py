from pwn import *  # pip install pwntools
import codecs
import json
from Crypto.Util.number import long_to_bytes
import base64

r = remote("socket.cryptohack.org", 13377, level="debug")


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode(coded, typ):
    if typ == "rot13":
        # 1
        result = codecs.decode(coded, "rot13")
    elif typ == "utf-8":
        # 0
        result = "".join([chr(x) for x in coded])
    elif typ == "base64":
        # 0
        coded = base64.b64decode(coded)
        result = str(coded, "utf-8")
    elif typ == "bigint":
        # 0
        result = long_to_bytes(int(coded, 16))
        result = result.decode()
    elif typ == "hex":
        # 0
        coded = bytes.fromhex(coded)
        result = codecs.decode(coded)

    return result


received = json_recv()

while received:
    try:
        print(received["flag"])
        break
    except:
        pass

    to_send = {"decoded": decode(received["encoded"], received["type"])}
    json_send(to_send)
    received = json_recv()
