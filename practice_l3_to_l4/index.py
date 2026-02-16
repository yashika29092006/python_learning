# 1️⃣ Find the sum of all even-indexed elements

# Example:
# [4, 7, 1, 9, 3]
# Even indices → 0,2,4 → 4 + 1 + 3 = 8

# def ind(n):
#     sum = 0
#     for i in range(0,len(n)):
#         if i % 2 == 0:
#             sum+=n[i]
#     print(sum)
# ind([4, 7, 1, 9, 3])

# n = [11, 22, 33]
# print(n[0],n[1],n[2])

# Find the largest number using index
# def maxi(n):
#     max=n[0]
#     for i in n:
#         if i > max:
#             max = i
#     print(max)
# maxi([3,8,2,5,9])

# 5️⃣ Count how many elements are greater than the element at index 0

# Example:
# [4, 6, 2, 9, 1]

# Compare everything with index 0 → value 4.
# Count how many are > 4 → (6,9) → 2

# def count(n):
#     f = n[0]
#     count = 0
#     for i in range(0,len(n)):
#         if n[i] > f:
#             count+=1
#     print(count)
# count([4, 6, 2, 9, 1])
        
# 6️⃣ Print elements at every 2nd index (0,2,4,6...)

# Example:
# ["a","b","c","d","e"]
# Output → a, c, e
# def ind(n):
#     for i in range(0,len(n)):
#         if i % 2 == 0:
#             print(n[i])
# ind(["a","b","c","d","e"])       

# 8️⃣ Compare adjacent elements using index

# Example:
# [3,7,2,9]

# Compare:

# 3 and 7

# 7 and 2

# 2 and 9

# Print larger each time

# def adj(n):
#     for i in range(0,len(n)):
#         for j in range(i+1,len(n)):
#             print(n[i],"and",n[j])
# adj([3,7,2,9])

# def num(a,b):
#     for i in range(0,len(a)):
#         if a[i]==b:
#             print(i)
# num([1,3,5,6],3)

# 🔟 Find the index of the smallest element

# Example:
# [9, 1, 5, 3] → smallest = 1 → index = 1

# def index(a):
#     s = a[0]
#     for i in range(0,len(a)):
#         if a[i] < s:
#             s = a[i]
#             print(i)
# index([9, 1, 5, 3])       


# def index(n,m):
#     count = 0
#     m =[]
#     for i in range(0,len(n)):
#         if n[i] == m:
#             count+=1
#         elif count == 1:
#             m.append(i)
#     print(m)
# # index([5,4,0,9,8,7,0,3,2])    
# index([1, 7, 4, 3, 7, 9, 2, 7],7)

# 2.Find the indices of numbers between the first 7 and second 7..Input:
# [1, 7, 4, 3, 7, 9, 2, 7]
# # Output:
# Given an array arr containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.
# Note: If no such array is possible then, return [-1].
# Examples:
# Input: arr = [1, 2, 3, 7, 5], target = 12 Output: [2, 4] Explanation: The sum of elements from 2nd to 4th position is 12.


# Given an array arr containing only non-negative integers, your task is to find a continuous subarray 
# (a contiguous sequence of elements) whose sum equals a specified value target.
#  You need to return the 1-based indices of the leftmost and rightmost elements of this subarray.
#  You need to find the first subarray whose sum is equal to the target.
# Note: If no such array is possible then, return [-1].
# Examples:
# Input: arr = [1, 2, 3, 7, 5], target = 12 Output: [2, 4] Explanation: The sum of elements from 2nd to 4th position is 12.

def find(n,m):
    # b = []
    for i in range(0,len(n)):
        c = 0
        for  j in range(i,len(n)):
            c+=n[j]
            if c == m:
                print([i+1,j+1])
                return
            if c > m:
                break
    print([-1])
find([1, 2, 3, 7, 5],12)
  

def add_first_last(arr):
    first = 0
    last = 0
    for value in arr:
        if first == 0:
            first = value   
        last = value       
    print(first + last)
add_first_last([1, 2, 3, 7, 5])

# ✅ 1. Students Above Average
# Problem

# You are given two lists:

# names → list of student names

# marks → corresponding marks

# Your task:

# ✔ First calculate the average of all marks
# ✔ Print the names of students whose marks are greater than the average
# ✔ If none are above average, print "No student found"

# Example

# Input:
# names = ["Ravi", "Kumar", "Sita"]
# marks = [50, 40, 90]

# Average = (50+40+90)/3 = 60
# Above avg = only "Sita"

# Output:
# Sita

# def li(n,m):
#     b=[]
#     sum = 0
#     for i in m:
#         sum+=i
#     avg = sum/len(m)
#     for j in m:
#         if j > avg:
#             b.append(j)

#     print(name)
# li(["Ravi", "Kumar", "Sita"],[50, 40, 90])






# def counts(a,b):
#     c = ""
#     count = 0
#     for i in range(0,len(b)):
#         count += b[i]
#     e = count / len(b)
#     for j in range(0,len(b)):
#         if b[j] > e:
#             c = a[j]
#     print(c)
# counts(["Ravi", "Kumar", "Sita"],[50, 40, 90])


# 2. Count Occurrences of a Number
# Problem
# Given:
# A list of integers
# A target number
# Find how many times the number appears.
# Do NOT use count().
# Example
# Input: [4, 2, 4, 5, 4], 4
# Output: 3

# def num(n,m):
#     for i in range(0,len(n)):
#         if n[i] == m:
#             print(i)
# num([4, 2, 4, 5, 4], 4)
    
# ✅ 3. Characters in Odd Positions (Reverse Output)
# Problem
# Given a string:
# ✔ Consider positions starting from 1
# ✔ Pick characters in odd positions only
# ✔ Print them in reverse order
# Example
# Input: "program"
# Positions → p(1), o(3), r(5), a(7)
# Reverse → a r o p
# Output:
# arop

# def num(n):
#     rev = ""
#     for i in range(0,len(n),2):
#         print(n[i])
# num("program")

# 4. Replace Multiples of 3 with -1
# Problem
# Given an integer list:
# ✔ If the element is divisible by 3 → replace with -1
# ✔ Others remain same.Example
# Input: [3,1,6,4,9,2]
# Output: [-1,1,-1,4,-1,2]
# def rep(n):
#     b = []
#     for i in n:
#         if i % 3 == 0:
#             b.append(-1)
#         else:
#             b.append(i)
#     print(b)
# rep([3,1,6,4,9,2])

# ✅ 5. Find the Maximum Even Number
# Example
# Input: [3,9,7]
# Output: -1
# Input: [2,10,4]
# Output: 10
    # def maxi(n):
    #     a=n[0]
    #     for i in n:
    #         if i > a:
    #             a = i
    #     if a % 2 == 0:
    #         print(a)
    #     else:
    #         print(-1)
    # maxi([2,10,4])

# ✅ 6. Find Second Highest Number (NO Sorting)
# Example
# Input: [4,1,7,3,2]
# Output: 4
# def sec(n):
#     a = n[0]
#     for i in n:
#         if i > a:
#             a = i
#     s = a
#     for i in n:
#         if i != s:
#             print(i)
#             break
# sec([4,1,7,3,2])

# ✅ 8. Last Occurrence of a Number
# Input: [1, 4, 7, 4, 9], value = 4
# Output: 3

# def num(n,m):
#     li = []
#     for i in range(0,len(n)):
#         if n[i] == m:
#             li.append(i)
#     print(li[-1])
# num([1, 4, 7, 4, 9],4)

# 9. Reverse Words Starting With Vowels
# Input: "apple bat orange cat"
# Output: "elppa bat egnaro cat"
# def vow(n):
#     b = []
#     c = n.split()
#     x = "aeiou"
#     for i in c:
#         # if i == x:
#         if i[0] in  x:
#             rev = ""
#             for j in i:
#                 rev = j + rev
#             b.append(rev)
#         else:
#             b.append(i)
#     print(" ".join(b))
# vow("apple bat orange cat")

# # ✅ 10. Check Digits Count == Letters Count
# # Input: "a1b2c3" → letters=3, digits=3 → True
# # Input: "ab12" → letters=2, digits=2 → True
# # Input: "a1b23" → letters=2, digits=3 → False

# # def cou(n):
# #     l = 0
# #     li="abc"
# #     d = 0
# #     di = "123"
# #     for i in n:
# #         if i == li:
# #             l+=1
# #         elif i == di:
# #             d+=1
# #     if l == d:
# #         print(True)
# #     else:
# #         print(False)
# # cou("a1b2c3")

# # merge two list
# # def num(n,m):
# #     new = []
# #     for i,j in zip(n,m):
# #         new.append(n)
# #         new.append(m)
# #     print(new)
# # num([1,2,3,4],['a','b','c'])

# def rot(n,m):
#     a = len(n)
#     m = m %  a
#     rotate = n[a-m:]+ n[:a-m]
#     print(rotate)
# rot([10,20,30,40,50],2)

# a = [1,2,3,4]
# result = []

# for i in range(len(a)):
#     s = 0
#     temp = []
#     for j in range(i, len(a)):
#         temp.append(a[j])
#         s += a[j]
#         if s % 2 == 0:
#             result.append(temp[:])

# print(result)


# def add(n):
#     sum = 0
#     for i in range(0,len(n),len(n)-1):
#         sum+=n[i]
#     print(sum)
# add([1,2,3,4,5])





# def concat(a,b):
#     rev = "" 
#     res = ""
#     result =[]
#     for i in range(len(b)-1,-1,-1):
#         rev+=b[i]
#     # print(rev)
#     for i in range(0,len(a)):
#         res+=a[i]
#         res+b[i]
#     print(res)
# concat("Abc","Xyz")


def born_in_first_half(names,birthdates):
    #Write your code here
    li = []
    birth = []
    name = []
    v = ""
    for i in range(0, len(birthdates)):
        y =(birthdates[i].split("/"))
        # print(y)
        for j in range(len(y)):
            # li.append(int(i[1]))
            li.append(int(y[j-1]))
            break
    # print(li)

    for k in li:
        if k >=1 and k <=6:
            birth.append(k)
            g = name.append(names[i])
        
    #         print(li[i])
    #         birth.append(i)
            # name.append(names[i])

    print(birth)
    print(g)

    # print(v)
born_in_first_half(["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"], ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"])          
            
def born_in_first_half(names,birthdates):
    name_list = []
    for i in range(len(birthdates)):
        day = int(birthdates[i].split('/')[0])
        month = int(birthdates[i].split('/')[1])
        if month > 0 and month < 7:
            name_list.append(names[i])
    print(name_list)
born_in_first_half(["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"], ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"])

def born_in_first_half(names, birthdates):
    li = []      # months list
    name = []    # final names list

    # Extract month from each birthdate
    for i in range(len(birthdates)):
        y = birthdates[i].split("/")   # ["dd", "mm"]
        li.append(int(y[1]))           # take the month (y[1])

    # Check month and add corresponding name
    for i in range(len(li)):
        if 1 <= li[i] <= 6:            # month between 1 and 6
            name.append(names[i])      # add the matching name

    print(name)

born_in_first_half(
    ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"],
    ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]
)
