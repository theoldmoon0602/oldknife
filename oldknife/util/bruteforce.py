def bruteforce(charset, maxlength, minlength=1):
    from itertools import combinations_with_replacement

    for i in range(minlength, maxlength+1):
        for cs in combinations_with_replacement(charset, i):
            yield ''.join(cs)
