def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    i, j = 0, 1 
    while n != 0:
        i = n % 10
        if i == 8:
            j = (n // 10) % 10
            if i == j:
                return True
            else:
                return False
        n = n // 10


def two_eights(n):
    """"the function use to check whether the number N have two eights or not
    >> two_eights(8)
     0
    >> two_eights(88)
    1
    """
    i, j = 0, 1
    while n != 0:
        i = n % 10
        if i == 8:
            j = n % 100
            if i == j:
                return 1
            else:
                return 0
        n = n // 10


double_eights(8)
double_eights(88)
