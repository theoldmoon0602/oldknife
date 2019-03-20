def nth_root(c, e):
    try:
        from gmpy import root
    except:
        from gmpy2 import iroot as root

    x = root(c, e)[0]
    return int(x)

def modinv(e, n):
    try:
        from gmpy import divm
    except:
        from gmpy2 import divm
    return int(divm(1, e, n))

def chinese_remainder(ms, ns):
    assert(len(ms) == len(ns))

    n = 1
    for i in range(len(ms)):
        n = n * ns[i]

    r = 0
    for i in range(len(ms)):
        p = n / ns[i]
        r += ms[i] * modinv(p, ns[i]) * p
    return int(r % n)

def rsa_from_n_phi(n, phi):
    try:
        from gmpy import mpz
        b = -(n + 1 - phi)
        p = (-b + mpz(b**2 - 4*n).sqrt()) // 2
        q = (-b - mpz(b**2 - 4*n).sqrt()) // 2
    except:
        from gmpy2 import mpz

        b = -(n + 1 - phi)
        p = (-b + mpz(b**2 - 4*n).isqrt()) // 2
        q = (-b - mpz(b**2 - 4*n).isqrt()) // 2

    try:
        return [long(p), long(q)]
    except:
        return [int(p), int(q)]

def rsa_params(**kwargs):
    if 'n' in kwargs and 'phi' in kwargs and ('p' not in kwargs or 'q' not in kwargs):
        p, q = rsa_from_n_phi(kwargs['n'], kwargs['phi'])
        kwargs['p'] = p
        kwargs['q'] = q

    if 'p' in kwargs and 'q' in kwargs:
        if 'n' not in kwargs:
            kwargs['n'] = kwargs['p'] * kwargs['q']
        if 'phi' not in kwargs:
            kwargs['n'] = (kwargs['p'] - 1) * (kwargs['q'] - 1)

    if 'phi' in kwargs and 'e' in kwargs and 'd' not in kwargs:
        kwargs['d'] = modinv(kwargs['e'], kwargs['phi']) 

    return kwargs

