def factorial(n):
    if n == 0:
        return "invalid"
    elif n == 1:
        return 1
    elif n > 1:
        return n*factorial(n-1)
# print(factorial(5))
def fact(n):
    print(factorial(n))
fact(5)
# def fib_rec(n):
#     a,b=0,1
#     for i in range(0,n):
#         a,b = b,a+b
# def fib(idx):
#     if idx < 0 :
#         return 0
#     return fib(idx) + fib(idx-1)
# print(fib(4))


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)
print(is_permutation("listen","silent"))


def gcd_of_three(a, b, c):
    result = gcd(gcd(a, b), c)
    print(result)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a  # helper function can return
gcd_of_three(30, 15, 90)  # 15
gcd_of_three(12, 18, 24)  # 6
gcd_of_three(9, 27, 81)  # 9


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    # count characters in s1
    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    # subtract using s2
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True
