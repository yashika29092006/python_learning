def k_value(s,k):
    r=""
    for i in range(0,len(s),k):
        r+=s[i]
    print(r)
k_value("abcdefg",2)

def check(n):
    b = ""
    for i in n:
        count = 0
        if i not in b:
            for j in n:
                if i == j:
                    count+=1
                    b+=i
            print(i,"->",count)
check("kamalesh")

def check(n):
    b = ""
    for i in n:
        count = 0
        if i not in b:
            for j in n:
                if i == j:
                    count+=1
                    b+=i
            print(i,"->",count)
check("mississippi")

# Between Two Zeros
# list = [1,2,3,0,4,5,6,0,7,8]

def zero(n):
    res = []
    count = 0
    for i in n:
        if i == 0:
            count+=1
        elif count == 1:
            res.append(i)
    print(res)
zero([1,2,3,0,4,5,6,0,7,8])

def is_check(n):
    sum= 0
    for i in range(0,len(n),len(n)-1):
        sum=sum+n[i]
    print(sum)   

is_check([1,2,3,5])

# Second Largest Number
# Find the second largest number in a list without using sort().
# Example:
# Input: [4, 9, 1, 7, 3]
# Output: 7

def sec_lar(n):
    max = n[0]
    for i in n:
        if i > max:
            max = i
    sec_lar = None
    for j in n:
        if j != max:
            if sec_lar is None or j > sec_lar:
                sec_lar = j

    print(sec_lar)
sec_lar([5,3,4,5])

# Unique Elements in Order
# Remove duplicates but maintain the original order.
# Example:
# Input: [1,2,3,1,2,4]
# Output: [1,2,3,4]

# def unique(n):
#     a = []
#     for i in n:
#         if i not in a:
#             a.append(i)
#     print(a)
# unique([1,2,3,1,2,4])

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
#                 return
#     if count == 0:
#         print(True)
#     else:
#         print(False)
# bal("(()())")
# bal("())(")
# bal("((())")

# Replace elements at even index with their square (0th, 2nd, 4th...)

# Input:
# [3, 2, 5, 4, 6, 7]

# Output:
# [9, 2, 25, 4, 36, 7]

# def rep(n):
#     res =[]    
#     for i in range(0,len(n)):
#         if i % 2 == 0:
#             res.append(n[i]**2)
#         else:
#             res.append(n[i])
#     print(res)
# rep([3, 2, 5, 4, 6, 7])

# Reverse a string except first 2 and last 2 characters

# Input: "fastapi"

# First 2 → fa
# Last 2 → pi
# Middle → sta → reversed → ats

# Output:
# faatspi

# def rev(n):
#     a = n[:2]
#     mid = ""
#     b = ""
#     for i in range(len(n)-3,1,-1):
#         mid = mid + n[i]
#     for j in range(len(n)-2,len(n)):
#         b = b + n[j]
#     print(a+mid+b)
# rev("fastapi")

def compare_lists(A, B):
    result = []
    for i in range(len(A)):
        s = A[i] + B[i]
        if s % 2 == 0:
            result.append("T")
        else:
            result.append("F")
    print(result)

compare_lists([1, 2, 3, 4], [1, 1, 6, 5])

# def find_small(s):
#     sentence = s.split()
#     s = sentence[0]
#     for i in sentence:
#         if len(i) < len(s):
#             s = i
#     print(s)
# find_small("Python is super powerful")
def long(s):
    sent = s[0]
    for i in s:
        if len(i) > len(sent):
            sent = i
    print(sent)
long(["apple", "banana", "kiwi", "strawberry"])

# def ann(n):
#     res = ""
#     for i in n:
#         if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
#             res+="M"
#         elif i in "qwertyuiopasdfghjklzxcvbnm":
#             res+="N"
#         elif i in "124567890":
#             res+="D"
#         else:
#             res+="O"
#     print(res)
# ann("Ab9$Z")
    
# def sec_lar(n):
#     max = n[0]
#     for i in n:
#         if i >max:
#             max = i
#     sec = None
#     for j in n:
#         if j != max:
#             if sec is None or j > sec:
#                 sec = i
#     print(sec)
# sec_lar([8, 3, 1, 6, 4])

# def arr(n)





        
def find_first_occurence(arr, value):
    index = 0
    for i in range(0, len(arr)):
        if arr[i] == value:
            index = i
            break
    print(index)
find_first_occurence([9, 7, 4, 1, 7, 0], 7)