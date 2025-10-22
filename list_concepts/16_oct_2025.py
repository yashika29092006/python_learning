'''
1.Find all the sum of all numbers which are greater than a given number (eg a = [2, 3, 1, 4, 5] num = 3 answer = 9 (5 + 4))
2.Print all the odd numbers in a given list.
'''
# 2
def odd(n):
    sum = 0
    for i in n:
        if i % 2 != 0:
            print(i)
odd([1,4,6,9,8,11])

# 1
def add(n,a):
    sum=0
    if n == 0:
        print("invalid")
    for i in a:
        if i > n:
            sum+=i
    print(sum)
add(3,[2, 3, 1, 4, 5])


            

