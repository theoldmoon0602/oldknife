import sys
import struct
from oldknife.util.conv import *
from oldknife.util.version import isv3

z85_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#'

def z85enc(src):
    if len(src) % 4 != 0:
        raise ValueError("len(src) % 4 != 0")

    dst = []
    for i in range(0, len(src), 4): 
        x = as_int(src[i:i+4])
        buf = []
        for _ in range(5):
            buf.append(z85_chars[x % 85])
            x = int(x / 85)
        dst += buf[::-1]

    return ''.join(dst)

def z85dec(src):
    if isv3() and isinstance(src, bytes):
        src = b2s(src)
    src += '0'*((5 - len(src)) % 5)

    lookup = {}
    for i, c in enumerate(z85_chars):
        lookup[c] = i
    
    xs = []
    for i, c in enumerate(src):
        if i % 5 == 0:
            x = 0
        x = x*85 + lookup[c]

        if i % 5 == 4:
            xs.append(x)

    return struct.pack('>{}I'.format(len(xs)), *xs)
