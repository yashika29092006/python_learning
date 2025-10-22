# ''' 
# 1.Given a list of integers, check if a number is present in the list or not. Print “found” else, print “not found”
# 2.Check if the sum of all numbers in a list is even or not
# 3.Given two numbers a and b and a list of numbers num_list. Print all the elements in num_list between a and b.
# For eg, num_list = [8, 1, 0, 19, 11, 28, 3, 5],  a = 10 and b = 20
# '''
def is_present (n):
    lists=[1,2,3,4,5,90]
    if n == 0:
        print("Invalid")
    else:
        if n in lists :
            print("Found")
        else:
            print("Not Found")
is_present(2)
is_present(10)
# # 2
def is_even_or_not(n):
    if n == 0:
        print("Invalid")
    else:
        sum = 0
        for i in n:
            sum+=i
        if sum % 2 == 0:
            print("even")
        else:
            print("Not even")
is_even_or_not([10, 20, 30])
is_even_or_not([20,3])

# #  3
def num_btw(a,b): 
    if a == 0 or b == 0:
        print("Invalid")
    else:
        num_list=[1,4,6,19,17]
        for i in num_list:
            if a < i and i < b:
                print(i)
num_btw(10,20)

# Sum of list elements Given a list of numbers, find the sum of all elements.
def sum(n):
    sum = 0
    for i in n:
        sum+=i
    print(sum)
sum([1,2,3,4,5])

# Even or odd sum .Check if the sum of all numbers in a list is even or odd.
def num(n):
    for i in n:
        if i % 2 == 0:
            print(i)
num([2,5,7,10])
        
# 4. Numbers between two values Question: Print all elements in a list between a and b.
# Input: List = [8,1,0,19,11,28,3,5], a = 10, b = 20
def num(a,b,c):
    if a == 0 or b == 0:
        print("invalid")
    else:
        for i in c:
            if a < i and i < b:
                print(i)
num(10,20,[8,1,0,19,11,28,3,5])

# 5. Maximum and minimum in list Question: Find the largest and smallest numbers in a list.
# Input: [4, 7, 1, 9, 12]
def max_min(lis):
    mini = min(lis)
    maxi = max(lis)
    print(mini)
    print(maxi)
max_min([2,5,7])







        
        



