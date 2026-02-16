# def factorial(n):
#     if n == 0:
#         return "invalid"
#     elif n == 1:
#         return 1
#     elif n > 1:
#         return n*factorial(n-1)
# print(factorial(5))

def fib_rec(n):
    a,b=0,1
    for i in range(0,n):
        a,b = b,a+b
def fib(idx):
    if idx < 0 :
        return 0
    return fib(idx) + fib(idx-1)
print(fib(4))

