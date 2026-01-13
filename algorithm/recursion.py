def factorial(n):
    if n == 0:
        return "invalid"
    elif n == 1:
        return 1
    elif n > 1:
        return n*factorial(n-1)
print(factorial(5))

def fibonacci_sequence_loop(n):
    a, b = 0, 1
    sequence = []
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b # Swap and calculate next term
    return sequence

print(fibonacci_sequence_loop(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fibo(n):
    a,b=0,1
    li = []
    for i in range(0,n):
        li.append(a)
        a,b = b,a+b
    return li
print(fibo(5))