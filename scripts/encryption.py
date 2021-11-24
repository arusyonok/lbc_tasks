import base64

def poorcipher(text):
    xorred = ''.join(chr(ord(k) ^ 15) for k in text).encode("utf-8")
    return base64.encodebytes(xorred)


def depoorcipher(bytez):
    decoded = base64.decodebytes(bytez).decode("ascii")
    initial_text = ''.join(chr(ord(k) ^ 15) for k in decoded)
    return initial_text
