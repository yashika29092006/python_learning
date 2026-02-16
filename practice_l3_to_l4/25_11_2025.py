# Print only Uppercase
def upper(n):
    for i in range(0,len(n)):
        if (n[i][0]) in "QWERTYUIOPASDFGHJKLZXCVBNM":
            print(n[i])
upper(["Apple","ball","Cat","dog"])

# Filter only 4 digit and endwith even
def filter(n):
    for i in range(0,len(n)):
        # print(i)
        result = []
        if n[i] > 1000 and n[i] < 9999:
            if n[i] % 2 == 0:
                result.append(n[i])
    print(result)
filter([2481,3572,602,7890,4212])

# print only lower case
def lower(m):
    result = ""
    for i in m:
        if i in "qwertyuiopasdfghjklzxcvbnm":
            result+=i
    print(result)
lower("PyTHonProGRam")

# Print only First ch and Last ch Same
def first_last(n):
    for i in range(0,len(n)):
        if n[i][0] == n[i][-1]:
            print(n[i])
first_last(["Apple","tat","Anna"])

# - Given two equal-length arrays maths and science,
#   return the indexes of students who scored > 80 in both subjects.

# ```python
# #test case 1
# Input:
# maths [92, 45, 81], science [88, 90, 70]

# Output: [0]
def high(n,m):
    res = []
    for i in range(0,len(n)):
        if n[i] > 80 and m[i]>80:
            print(i)
high([92, 70, 81],[88, 90, 70])

# - You are given a list containing integers, floats and strings.
# Create a new list containing only the float values using one loop.
# ```python
# Example:
# Input: [10, 3.5, "hello", 8.2, 6]
# Output: [3.5, 8.2]
def check_float(n):
    for i in n:
        if type(i) == float:
            print(i)
check_float([10, 3.5, "hello", 8.2, 6])


# - Given two strings, S_1 and S_2, determine if S_2 is a rotation of S_1.
#   For example, "waterbottle" is a rotation of "erbottlewat".
#   Assume both strings have the same number of characters. Print True or False.

# ```python
# # test case 1
# Input: s1 = "ABCDE", s2 = "CDEAB"
# Output: True

# # test case 2
# Input: s1 = "ABCDE", s2 = "ACDEB"
# Output: False
# def find(n):
def compare_strings(left,right):
    #start
    if len(left) == 0 or len(right) == 0:
        print("Invalid input")
    else:
        final = left
        output = False
        for i in range(0,len(left),+1):
            temp = final[1:] + final[0]
            final = temp
            if final == right:
                output = True
        print(output)
    #stop
compare_strings("ABCDE","CDEAB")

def find_one_zero(n):
    # c =  str(n)
    for j in n:
        c = str(j)
        count = 0
    # print(type(c))
        for i in c:
            if i == '0':
            # print(i)
                count+=1
            # count = 0
            # print(count)
        if count == 1:
            print(j)

find_one_zero([101,120,340,3001])

# Keep Words With No Repeated Letters
# Task:
#  Filter to keep words where all characters are unique.
# Input:
#  ["hello", "world", "python", "sky", "loop"]
#  Output:
#  ["world", "python", "sky"]
def no_repeat(n):
    res =[]
    for i in n:
        s = ""
        for j in i:
            if j not in s:
                s+=j
        if len(s) == len(i):
            res.append(i)
    print(res)
no_repeat(["hello", "world", "python", "sky", "loop","ate"])

# 9. Keep words where uppercase letters are more than lowercase.
# Input: ["HeLLo", "WORLD", "python", "ApP"]
#  Output: WORLD ApP
def only_upper(n):
    b  = "qwertyuiopasdfghjklzxcvbnm"
    for i in n:
        lower = 0
        upper = 0
        for j in i:
            if j in b:
                lower+=1
            else:
                upper+=1
        if upper > lower:
            print(i)
only_upper(["HeLLo", "WORLD", "python", "ApP"])

# 4. Print numbers where product of digits is odd.
# Given numbers, keep only those whose digit-product is odd.
#  Input: [13, 22, 51, 87]
#  Output: 13 51
def separate(n):
    for i in n:
        c = i % 10
        d = i // 10
        if c % 2 != 0 and d % 2 != 0:
            print(i)
separate([13, 22, 51, 87])