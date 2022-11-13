from random import choice

def fastsort(a):
    if len(a) <= 1:
        return a
    b = choice(a)
    A1 = [q for q in a if q < b]
    A2 = [q for q in a if q == b]
    A3 = [q for q in a if q > b]
    return fastsort(A1) + A2 + fastsort(A3)


def rassort(a):
    l = len(a)
    st = l
    while st > 1 or fl:
        if st > 1:
            st -= 1
        fl, i = False, 0
        while i + st < l:
            if a[i] > a[st + i]:
                a[i], a[st + i] = a[st + i], a[i]
                fl = True
            i += st
    return a


