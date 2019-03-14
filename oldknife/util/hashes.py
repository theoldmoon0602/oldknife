from oldknife.util.conv import *

def hashhex(f, s):
    return f(to_bytes(s)).hexdigest()

def hashraw(f, s):
    r = f(to_bytes(s)).digest()

    return to_str(r)

def md5hex(s):
    from hashlib import md5
    return hashhex(md5, s)

def md5raw(s):
    from hashlib import md5
    return hasraw(md5, s)

def sha1hex(s):
    from hashlib import sha1
    return hashhex(sha1, s)

def sha1raw(s):
    from hashlib import sha1
    return hasraw(sha1, s)
