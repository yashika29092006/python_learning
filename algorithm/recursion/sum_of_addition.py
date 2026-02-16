def adds(n):
    if n == 0:
        return False
    elif n == 1:
        return 1
    else:
        return n + adds(n - 1)
print(adds(5))
