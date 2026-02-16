# 4. Print numbers where product of digits is odd.
# Given numbers, keep only those whose digit-product is odd.
#  Input: [13, 22, 51, 87]
#  Output: 13 51

# def odd(n):
#     for i in n:
#         count = []
#         c = i // 2
#         d = i % 2
#     print(c,d)  
# odd([13, 22, 51, 87])

# Words Ending in "ing"
# Input:
# ["playing", "run", "walking", "see", "coding"]
# Expected Output:
# ["playing", "walking", "coding"]

# def end(n):
#     c =[]
#     for el in n:
#         if el[-1] in "g" and el[-2] in 'n' and el[-3] in 'i':
#             c.append(el)    
#     print(c) 
# end(["playing", "run", "walking", "see","coingu", "coding"])

# Rearrange by Length
# Given a list of words, rearrange them so shorter words come first.
#  (Don't use sort() or sorted())
# Input:
#  ["banana", "cat", "watermelon", "apple"]
# Output:
#  ["cat", "apple", "banana", "watermelon"]
# def sort(n):
#     c = []
#     first = 0
#     for i in range(0,len(n)):
#         if len(n[i]) > first:
#             c.append(n[i])
#             first = len(n[i])
#             # c.append(n[i])
#     print(c)
# sort(["banana", "cat", "watermelon", "apple"])

# 1.Print characters that are uppercase
# Question:
#  Given a string, print only the uppercase characters.
#  Input: "HeLLoWorld"
#  Output: H L L W
# 2.Print numbers ending with digit 7
# Input: [17, 23, 47, 59, 70]
#  Output: 17 47

# def upper(n):
#     for el in n:
#         if el in "QWERTYUIOPASDFGHJKLZXCVBNM":
#             print(el)
# upper("HeLLoWorld")

# def end_7(n):
#     final = []
#     for i in n:
#         c = i % 10
#         if c == 7:
#             final.append(i)
#     print(final)
# end_7([17, 23, 47, 59, 70])

# a list of students
# a list of scores (same length)
#  Return the names of students whose name has more than 3 vowels AND whose score is above average score.
#  Use nested loops (one to count vowels, one to compute average).
# Input:
#  students = ["Aravind", "Bala", "Eeshwar", "Louis", "Gita"]
#  scores = [85, 70, 92, 88, 60]
# Output:
#  ["Aravind", "Eeshwar", "Louis"]
# def find(n,m):
#     sum = 0
#     result = []
#     x = []
#     for el in m:
#         x = []
#         sum+=el
#         avg = int(sum /len(m))
#     for i in range(0,len(n)):
#         count = 0
#         for j in n[i]:
#             if j in "AaEeIiOoUu":
#                 count+=1
#         if count == 3 and m[i] > avg:
#             result.append(n[i])
#     print(result)
# find(["Aravind", "Bala", "Eeshwar", "Louis", "Gita"],[85, 70, 92, 88, 60])


# Given a list and a target value, return all indices where the target appears.
#  Example: [1, 2, 3, 2, 4, 2] → target 2 → indices [1, 3, 5].
# def find(n,m):
#     c = []
#     for i in range(0,len(n)):
#         if n[i] == m:
#             c.append(i)
#     print(c)
# find([1, 2, 3, 2, 4, 2],2)       


# 8. Filter numbers that contain digit '0' in the end.
# # Input: [10, 101, 2005, 340, 89]
# #  Output: 10 340

# def find_zero(n):
#     for i in n:
#         c = i % 10
#         if c == 0:
#             print(i)
# find_zero([10, 101, 2005, 340, 89])

# 5. Print words that have more consonants than vowels.
# Input: ["apple", "tree", "rhythm", "code"]
#  Output: rhythm
# def const(n):

#     for i in n:
#         vow = 0
#         con = 0
#         for j in i:
#             if j in "aeiou":
#                 vow+=1
#             else:
#                 con+=1
#         if con > vow:
#             print(i)
         
# const(["apple", "tree", "rhythm", "code"])

# 4. Print numbers where product of digits is odd.
# Given numbers, keep only those whose digit-product is odd.
#  Input: [13, 22, 51, 87]
#  Output: 13 51
# def product(n):
#     for i in n:
#         c = i // 10
#         d = i % 10
#         e = c * d
#         if e % 2 != 0:
#             print(i)
# product([13, 22, 51, 87])

# 6. Keep numbers that increase from left to right (digit-wise).
# Example: 123 (1<2<3 → valid), 212 (invalid).
#  Input: [123, 2345, 98, 457, 566]
#  Output: 123 2345 457



def book(n,m):
    if len(n) == 0:
        print(-1)
    else:
        count = 0
        for i in range(0,len(n)):
            if m >=n[i] and m <n[i-1]:
                count= i+1
        print(count)
book([98, 75, 60, 50, 40, 25], 55)

def first(n,m):
    index = -1
    for i in range(0,len(n)):
        if n[i] == m :
            index = i
            break
    # print(-1)
    print(index)
    
first( [9, 7, 4, 1, 7, 0], 7)

def rev(n):
    o = ""
    for i in range(1,len(n),2):
        o =n[i]+o
    print(o)
        
rev("python")
rev("helloworld")

def even(n):
    sum = 0
    for el in n:
        if el % 2 == 0:
            sum +=el
    print(sum)
even([1, 2, 3, 4, 5, 6])

def odd_ind(n):
    res = []
    for i in range(0,len(n)):
        if i % 2 != 0:
            res.append(0)
        else:
            res.append(n[i])
    print(res)
odd_ind( [4, 1, 2, 3, 5] )

def find(name,m,p,c):
    topper= ""
    high = 0
    total = 0
    student = 0
    for i in range(0,len(name)):
        if m[i] > 90 and p[i] >90 and c[i] >90:
            student = 1
            total = m[i]+p[i]+c[i]
            if total > high:
                high = total
                topper+=name[i]
            # print(topper)
    if student == 1:
        print(topper)
    else:
        print("not found")
find(["jason", "priya", "madhan", "syed"], 
              [91, 92, 81, 75],
              [91, 89, 100, 90],
              [91, 95, 100, 90])

find(["Ameer", "Bobby", "Clara", "Divya", "Elvin", "Fazil", "Geeta", "Hari", "Ila", "Jay"],
[85, 88, 89, 90, 86, 87, 84, 83, 89, 88],
[84, 87, 88, 89, 85, 86, 83, 82, 88, 87],
[86, 85, 84, 83, 87, 88, 82, 81, 85, 86])

def inc(n):
    res = []
    for i in n:
        s = str(i)
        is_inc= 1
        for j in range(len(s)-1):
            # print(s[j])
            if s[j]>s[j+1]:
                is_inc = 0
                break
        if is_inc == 1:
            res.append(i)
    print(res)
inc([123, 2345, 98, 457, 566])

def unique(n):
    for i in n:
        b = ""
        # for j in i:
        if i not in b:
            b = b+i
    print(b)
unique(["apple", "cat", "moon", "dog"])
    
def sort(n):
    res = []
    # for i in n:
    s = n[0]
    for j in n:
        if len(n)<len(s):
            s = j
    res.append(s)
    n.remove(s)
    print(res)
sort(["banana", "cat", "watermelon", "apple"])
