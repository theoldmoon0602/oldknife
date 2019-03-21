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

def rsa_params(**params):
    if 'n' in params and 'phi' in params and ('p' not in params or 'q' not in params):
        p, q = rsa_from_n_phi(params['n'], params['phi'])
        params['p'] = p
        params['q'] = q

    if 'p' in params and 'q' in params:
        if 'n' not in params:
            params['n'] = params['p'] * params['q']
        if 'phi' not in params:
            params['phi'] = (params['p'] - 1) * (params['q'] - 1)

    assert(params['n'] == params['p'] * params['q'])
    assert(params['phi'] == (params['p'] - 1) * (params['q']- 1))

    if 'phi' in params and 'e' in params and 'd' not in params:
        params['d'] = modinv(params['e'], params['phi']) 

    return params

