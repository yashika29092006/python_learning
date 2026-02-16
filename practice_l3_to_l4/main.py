# Between Two Zeros
# list = [1,2,3,0,4,5,6,0,7,8]

# def btw_two_zero(n):
#     li =[]
#     res =[]
#     for i in range(0,len(n),1):
#         if n[i]==0:
#             li.append(i)
#     first = li[0]
#     second = li[1]
#     for j in range(first+1,second):
#         res.append(n[j])
#     print(res)
# btw_two_zero([1,2,3,0,4,5,6,0,7,8])

# Input: A list containing exactly two zeros.
# Print all the numbers between those two zeros (no slicing, no nested loops).

# Second Largest Number
# Find the second largest number in a list without using sort().
# Example:
# Input: [4, 9, 1, 7, 3]
# Output: 7

# def sec_lar(n):
#     max = n[0]
#     for i in n:
#         if i > max:
#             max = i
#     print(max)

#     second_largest = n[0]
#     for  max_1 in n:
#         if max_1 != max and max_1 > second_largest:
#             second_largest = max_1
#     print(second_largest)
# sec_lar(2,3,2,4,5,3,9)

#     max = max1 =n[0]
#     for i in n:
#         if i > max:
#             max1= max
#             max = i
#         elif i > max1 and i!= max:
#             max1 = i
#     print(max1)

# sec_lar([5,4,3,2,1])

# Unique Elements in Order
# Remove duplicates but maintain the original order.
# Example:
# Input: [1,2,3,1,2,4]
# Output: [1,2,3,4]

# def dupi(n):
#     x = []
#     for i in n:
#         if i not in x:
#             x.append(i)
#     print(x)
# dupi([1,2,3,1,2,4])


# Count Frequency
# Print how many times each element appears in a list (without using collections.Counter).
# Example:
# Input: [2,2,3,4,3,3]
# Output:
# 2 -> 2 times
# 3 -> 3 times
# 4 -> 1 time
# def counts(a):
#     b = []
#     for i in a:
#         count = 0
#         if i not in b:
#             for j in a:
#                 if i == j:
#                     count +=1
#                     b.append(i)
#             print(i,"->", count)
# counts([1,2,1,3,2,3,1,4])

# numbers = [2,3,2,4,3,5,5,3]
# num = ""
# for i in numbers:
#         count = 0 
#         for j in numbers:
#             if i == j:
#                 count+=1
#         print(count)


# Balanced Parentheses
# Print True if opening and closing parentheses match, else False.
# Example:
# Input: "(()())"
# Output: True
# Input: "())("
# Output: False
# def bal(n):
#     count = 0
#     for i in n:
#         if i == "(":
#             count+=1
#         elif i == ")":
#             count-=1
#             if count < 0:
#                 print(False)
#                 break
#     if count == 0:
#         print(True)
# bal("(()())")
# bal("())(")

# Count Words Without Split
# Count the number of words in a sentence without using .split().
# Example:
# Input: "I love Python"
# Output: 3
def word(n):
    count = 1
    for i in n:
        if i == " ":
            count+=1
    print(count)
word("I love Python")


# Most Frequent Character
# Find the character that appears the most.
# Example:
# Input: "success"
# Output: s (appears 3 times)

# def most(n):
#     m = []
#     for i in n:
#         count = 0
#         if i not in m:
#             for j in n:
#                 if i == j:
#                     count+=1
#                     m.append(i)
#             # print(i,"-->",count)
# most("success")

# sec lar
# def sec(n):
#     max = n[0]
#     for i in n:
#         if i > max:
#             max = i
#     secl=n[0]
#     for j in n:
#         if j != max and j > secl:
#             secl = j 
#     print(secl) 
# sec([1,2,3,4,5])

# Longest Consecutive Sequence
# Input: [100, 4, 200, 1, 3, 2]
#  Output: 4 (Sequence: 1, 2, 3, 4)

# def zero(n):
#     count = 0
#     m = []
#     for i in n:
#         if i == 0:
#             count+=1
#         elif i != 0:
#             m.append(i)
#     for j in range(0,count):
#         m.append(0)
#     print(m)
# zero([1,2,3,0,5,6,0,9,8])

# def pal(n):
#     for i in range(len(n)-2,0,-1):
#         print(n[i])
# pal("hello")

# def acr(n):
#     res = n[0]
#     for i in range(0,len(n)):
#         if n[i] == ' ':
#             res+=n[i+1]
#     print(res)
# acr("Indian Army Police")

# def rep(n):
#     li = [None]*len(n)
#     for i in range(0,len(n)):
#         # key = n[i]
#         if n[i] % 2 == 0:
#             n[i] = n[i]/2
#         li[i] = n[i]
#     print(li)
# rep([1,2,3,4,5,6])

# def com(n,m):
#     new =[]
#     for i in range(0,len(n)):
#         for j in range(0,len(m)):
#             if n[i] == m:
#                 new.append(m)
#     print(new)
# com([1,2,3,4,5],1)

# def middle_element(lst):
#     n = len(lst)
#     if n == 0:
#         return None  # empty list check
#     elif n % 2 == 1:
#         return lst[n // 2]  # odd length → single middle element
#     else:
#         return (lst[n // 2 - 1], lst[n // 2])  # even length → two middles

# # Example
# print(middle_element([10, 20, 30, 40, 50]))  # Output: 30
# print(middle_element([1, 2, 3, 4]))          # Output: (2, 3)



def gcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b) // gcd(a,b)


print(lcm(12,18))

# def mid(n):
#     x=len(n)
#     if x == 0:
#         return None
#     elif x % 2 == 1:
#         return n[x // 2]
#     else:
#         return n[x//2-1],n[x//2]
# print(mid([10, 20, 30, 40, 50]))
# print(mid([1, 2, 3, 4]))

# def mid(lst):
#     n = len(lst)
#     if n == 0:
#         print(None)
#     elif n % 2 == 1:
#         print(lst[n//2])
#     else:
#         print(lst[n//2-1],lst[n//2])
# mid([10, 20, 30, 40, 50])
# mid([1, 2, 3, 4])

# def rotate_list(lst, k):
#     k = k % len(lst)
#     return lst[-k:] + lst[:-k]

# print(rotate_list([1, 2, 3, 4, 5], 2))

# def rot(n,k):
#     k = k % len(n)
#     print(n[-k:]+n[:-k]) 
# rotate_list([1, 2, 3, 4, 5], 2)  
# def highest_marks(names, maths, physics, chemistry):
#     y=[]
#     a=[]
#     result =[]
#     final =""
#     for i in range(0,len(names)):
#         if maths[i] > 90 and  physics[i] >90 and chemistry[i]>90 :
#             print(names[i])

    
    # print(final)
    # print(x)
    # print(a)
    # for i in range(0,len(x)):
    #     count =0
    #     for  j in range(0,len(y)):
    #         if i == j:
    #             result.append(y[j])
    #     for k in range
    # for h in result:
    #     final+=h
        
    # for i in x:
    #     if i in y and i in a:
    #         result.append(i)
    #     print(final)
            
    # print("No student found")
# highest_marks(["jason", "priya", "madhan", "syed"],
#               [91, 92, 81, 75],
#               [91, 89, 100, 90],
#               [91, 95, 100, 90])
# highest_marks(["Ameer", "Bobby", "Clara", "Divya", "Elvin", "Fazil", "Geeta", "Hari", "Ila", "Jay"],
# [85, 88, 89, 90, 86, 87, 84, 83, 89, 88],
# [84, 87, 88, 89, 85, 86, 83, 82, 88, 87],
# [86, 85, 84, 83, 87, 88, 82, 81, 85, 86])        
        
# - Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2,
#   Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
# ```python
# INPUT: s1 = "Abc", s2 = "Xyz"
# OUTPUT: "AzbycX"

def concat(a,b):
    rev = "" 
    res = ""
    result =[]
    for i in range(len(b)-1,-1,-1):
        rev+=b[i]
    # print(rev)
    for i in range(0,len(a)):
        rev+=a[i]
        rev+b[i]
    print(res)
concat("Abc","Xyz")
            
     
            
    
            
            

        


      
