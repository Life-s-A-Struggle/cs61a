def hailstone(n):
    i=0
    while n >0 and n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        i = i + 1
    return i
