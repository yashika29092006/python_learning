# # count len of num 
# def count(n):
#     count = 0
#     while n > 0:
#         n = n // 10
#         count+=1
#     print(count)
# count(123)

# # print after 0 and before 0
def count(n):
    count = 0
    li = []
    for i in n:
        if i == 0:
            count+=1
            # li.append(i)
        elif count == 1:
            li.append(i)
    print(li)
count([1,2,4,0,3,4,5,0,5,7])

# # find long word
# def long(n):
#     a = n[0]
#     for i in n:
#         if len(i) > len(a):
#             a = i
#     print(a)
# long(['cat','Elephant','gundu'])

# # remove dupi char
# def uniq(n):
#     b = ""
#     for i in n:
#         if i not in b:
#             b+=i
#     print(b)
# uniq('programming')

# # subarray
# def sub_combination(n,m):
#     count = 0
#     for i in range(0,len(n)):
#         for j in range(i, len(n)):
#             var = n[i:j+1]
#             # print(var)
#             if var == m:
#                 count+=1
#     print(count)
# sub_combination("ababab",'aba')

# # remove second string
# def second(n,m):
#     print(n.replace(m,""))
# second('programming','gramm')

# def sec(n,m):
#     y = ""
#     i =  0
#     while i < len(n):
#         if n[i:i+len(m)]==m:
#             i= i + len(m)
#         else:
#             y += n[i]
#             i+=1
# sec('programming','gramm')

# # mug 
# def cart(n):
#     mug = 500
#     jeans = 3000
#     ts = 1500
#     pen = 10
#     res = 0
#     # s = n.split()
#     for i in range(0,len(n)):
#         q =int(n[i].split(" ")[1])
#         if n[i][0] == "M":
#                 res += mug * q
#         elif n[i][0] == "J":
#                 res += jeans*q
#         elif n[i][0] == "T":
#                 res += ts * q
#         elif n[i][0] == "P":
#                 res += pen * q
#     print(res)
# cart(["M 3", "J 1", "T 2"])
# cart(["P 5", "M 1"])

# def birthday(n,k):
#     # m = []
#     l = []
#     for i in range(0,len(k)):
#         date = int(k[i].split("/")[1])
#         # m.append(int(k[i].split("/")[1]))
#         # print(date)
#     # print(m)
#     # for i in range(0,len(m)):
#         if date > 0 and date <= 6:
#             l.append(n[i])
#     print(l)  
          
# birthday(["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"],
#     ["05/1", "19/7", "23/3", "30/6", "11/11", "02/5", "15/6", "01/12"])


# # sat or unsat
# def sat(n):
#     count = 0
#     m = str(n)
#     b = ""
#     # print(m[0])
#     for i in range(0,len(m)):
#         if m[i] not in b:
#             b+=m[i]
#         # print(b)
#             count +=1
#     if count == 2:
#             print("sat")
#     else:
#             print("unsa")

# sat(132)
# sat(1311)

# # sec lar
# def sec(n):
#     f =n[0]
#     for i in n:
#         if i > f:
#             f = i
#     # print(f)
#     s = n[0]
#     for j in n:
#         if j != f and j > s:
#             s = j
#     print(s)
# sec([1,2,3,4,5])  

# Write a function find_first_occurence(arr, value) that prints the index of the first occurrence of a given value in the array.
#  If the value is not found, prints -1. (Do this without using any library function). If its an empty array, the output will be -1.
# Input = [9, 7, 4, 1, 7, 0], 7
# # output
# 1
# def con(n,m):
#     for i in range(0,len(n)):
#         if n[i] == m:
#            print(i)
#            break
#     else:
#         print(-1)
# con([9, 7, 4, 1, 7, 0], 3)

# marks
# def marks(n, m, p, c, v):
#     for i in range(0, len(n)):
#         if v == 'physics':
#             if p[i] == max(p):
#                 print(n[i])
#         elif v == 'chemistry':
#             if c[i] == max(c):
#                 print(n[i])
#         elif v == 'maths':
#             if m[i] == max(m):
#                 print(n[i])


# marks(
#     ["Arun", "Bala", "Cathy", "Divya"],
#     [88, 92, 76, 90],
#     [81, 89, 95, 70],
#     [90, 87, 85, 91],
#     'physics'
# )


# def vowel(n):
#     b = ""
#     for i in n:
#         if i not in 'aeiou':
#             b+=i
#     print(b)
# vowel('apple')

# find avg and print above value
# def find(n):
#     avg = 0
#     sum = 0
#     for i in n:
#         sum+=i
#         avg = int(sum /len(n))
#     # print(avg)
#     for j in n:
#         if j > avg:
#             print(j)
# find([10,20,30,40,50])


# def find_ind(n):
#     x = len(n)
#     for i in range(0,len(n)):
#         if i % 2 == 1:
#             print(n[x//2])
# find_ind([1,2,3,4,5,6])

# def y(list_of_list):
#     for i in list_of_list:
#         b = []
#         for k in i:
#             if k not in b:
#                 b.append(k)
#         for l in b:
#             print(l, end=" ")
#         print()

# y([
#     [1, 2, 2, 3],
#     [4, 4, 5, 4],
#     [7, 8, 8, 7, 9]
# ])

# def tic(n):
#     for i in range(0,len(n)):
#         for j in n[i]:
#             if n[i][0] == n[i][1] == n[i][2] == "X":
#                 return "X"
#             elif n[i][0] == n[i][1] == n[i][2] == "O":
#                 return "O"   
# print(tic([
#     ["X", "X", "O"],
#     ["O", "O", "O"],
#     ["", "", ""]
# ]) ) 
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

def lcm(a, b):
    big = a if a > b else b

    while True:
        if big % a == 0 and big % b == 0:
            print(big)
            break
        big = big + 1
# print(lcm(12,18))
lcm(12,18)