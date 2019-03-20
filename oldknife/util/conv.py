from oldknife.util.version import isv3

def to_hex(x):
    s = None
    if isinstance(x, int) or (not isv3() and isinstance(x, long)):
        s = hex(x)[2:].rstrip('L')
    elif isv3():
        from binascii import hexlify
        s = hexlify(to_bytes(x)).decode('ascii')
    else:
        s = x.encode("hex")
    return ('0' + s) if len(s) % 2 == 1 else s

def to_bytes(x):
    if isv3() and isinstance(x, str):
        xs = []
        for c in x:
            xs.append(ord(c))
        x = bytes(xs)
    return x

def to_str(x):
    if isv3() and isinstance(x, bytes):
        s = ''
        for b in x:
            s += chr(b)
        x = s
    return x

def as_str(x):
    if isv3():
        from binascii import unhexlify
        return to_str(unhexlify(to_bytes(to_hex(x))))
    else:
        return to_hex(x).decode("hex")

def as_int(x):
    if isv3():
        from binascii import hexlify
        return int(hexlify(to_bytes(x)).decode('ascii'), 16)
    else:
        return int(x.encode("hex"), 16)

