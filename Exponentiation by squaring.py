def exponentiation_by_squaring(n: int, a: int) -> int:
    res = 1
    if n == 0:
        return res
    mult = a
    while n!=0:
        if n%2 == 1:
            res *= mult
        mult = mult * mult
        n = int(n/2)
    return res

n=13
a=2
exponentiation_by_squaring(n, a)
