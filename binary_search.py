def binary_search(a: list, target: int) -> int:
    s = 0
    e = len(a)
    while s+1 < e:
        m = int(s + (e-s)/2)
        if a[m] > target:
            e = m
        else:
            s = m
    
    if a[s] == target:
        return s
    else:
        return -1

if __name__ == "__main__":
    a = [1,3,5,5,10,666]
    target = 666
    binary_search(a, target)
