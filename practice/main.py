# count vowels
def count_vow(n):
    count = 0
    x= 'aeiouAEIOU'
    for i in n:
        if i in x:
            count+=1
    print(count)
count_vow("Python Programming")

# print even num in list
def print_even(n):
    new = []
    for i in n:
        if i % 2 == 0:
            new.append(i)
            # print(i)
    print(new)
print_even([1,2,5,4,6,7])

# reverse the string
# def rev_string(n):
#     b = ""
#     for i in range(len(n)-1,-1,-1):
#         b+=n[i]
#     print(b)
# rev_string("apple")

# remove duplicates
def rem_dup(n):
    new = []
    for i in n:
        if i not in new:
            new.append(i)
    print(new)
rem_dup([1,2,3,3,4])
 
# find pal
def lar(n):
    a = ""
    for i in range(len(n)-1,-1,-1):
        # print(n[i])
        a=a+n[i]
    # print(a)
    if a == n:
        return "pal" 
    else:
        return "not pal" 
print(lar("madam"))  


# common
def find(n,m):
    b = []
    for i in n:
        if i in m:
            b.append(i)
    x = set(b)
    y = list(x)
    print(y)
find([2,3,4,4],[3,4,4])

# find short and long
def find(n):
    short = n[0]
    long = n[0]
    for i in n:
        if len(i)<len(short):
            short = i
        elif len(i)>len(long):
            long = i
    print(short)
    print(long)

find(["cat","elephant","lion"])

# find max
def maxim(n):
    maxi = - 100
    for i in n:
        if i > maxi:
            maxi = i
    print(maxi)
maxim([2,9,3,4,6,8])

# first ch and last ch
def find(n):
    print(n[0],n[1])
find("Python")

# sep by space
def sep(n):
    count = 1
    for i in n:
        if i == " ":
            count+=1
    print(count)
sep("Python is a programmming language is a good")

# repl space into -
def sep(n):
    r = ""
    for i in n:
        if i == " ":
            r+="-"
        else:
            r+=i
    print(r)        
sep("Python is a programmming language is a good")


# count vow
# def vow(n):
#     count = 0
#     x='aeiouAEIOU'
#     for i in n:
#         if i in x:
#             count+=1
#     print(count)
# vow("Python")

# # find occ
# def find(n,m):
#     count = 0
#     for i in n:
#         if i in m:
#             count+=1
#     print(count)
# find("Yashika","a")

# # list (input)[2,4,6,8] output [2,6,12,20]
# def find(n):
#     r = []
#     sum = 0
#     for i in n:
#         sum+=i
#         r.append(sum)
#     print(r)
# find([2,4,6,8])

# acro
# def find(n):
#     result = n[0]
#     for i in range(1,len(n)):
#         if n[i] == " ":
#             result+=n[i+1]
#     print(result)
# find("Indian Navy police")
    
# gcd
# def gcd(a,b):
#     while b != 0:
#         a,b=b,a%b
#     print(a)
# gcd(12,18)

# lcm
# def lcm(a,b):
#     great=max(a,b)
#     while True:
#         if great % a == 0 and great % b == 0:
#             return great
#         great+=1
# print(lcm(4,6))

# prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n*0.5)):
#         if n % 2 == 0:
#             return False
#     return True
# print(is_prime(7))   

# def rev(n):
#     a = n[0]+n[1]
#     mid = ""
#     b = ""
#     for i in range(len(n)-3,1,-1):
#         a = a + n[i]
#     for j in range(len(n)-2,len(n)):
#         a = a + n[j]
#     # print(a+mid+b)
#     print(a)
# rev("fastapi")

# def merge(n,m):
#     res = []
#     for i in range(0,len(n)) :
#         temp = n[i]+" "+m[i]
#         print(temp)
#         res.append(temp)
#     print(res)       
# merge(["red", "blue"], ["car", "pen"])

list ="hello world python"
result  = ""
b = " "
# hi = '-'
for i in list:
    if i not in b:
        result+=i
    else:
        result+="-"
print(result)

