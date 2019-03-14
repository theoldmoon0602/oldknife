def nth_root(c, e):
    import gmpy

    x = gmpy.root(c, e)[0]
    try:
        return long(x)
    except:
        return int(x)

def rsa_d(p, q, e):
    import gmpy

    phi = (p-1)*(q-1)
    modinv = gmpy.divm(1, e, phi)
    try:
        return long(modinv)
    except:
        return int(modinv)

def rsa_from_n_phi(n, phi):
    from gmpy import mpz
    b = -(n + 1 - phi)
    x = (-b + mpz(b**2 - 4*n).sqrt()) // 2
    y = (-b - mpz(b**2 - 4*n).sqrt()) // 2

    try:
        return [long(x), long(y)]
    except:
        return [int(x), int(y)]
