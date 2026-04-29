# Print all numbers divisible by 5 between 0 to 100 using while loop

# for i in range(0,101):
#     if i % 5 == 0:
#         print(i)


# Write a program in Python that asks the user for a number and then prints its multiplication table from 1 to 10 using a while loop.

# def print_table(num):
#     i = 1
#     while i <=10:
#         print(num,"X",i,"=",num * i)
#         i+=1
# print_table(5)

# Find the sum of all numbers from 1 to 5 (both inclusive) using a while loop.

# def sumi(n):
#     sum = 0
#     i = 1
#     while i <= n:
#         sum= sum + i
#         i+=1
#     print(sum)
# sumi(5)

# separate number

# def separate(n):
#     a = n % 10
#     print(a)
#     b = n // 100
#     print(b)
#     c = n
#     print(c)
# separate(567)

# palidrome

# def pali(s):
#     b = ""
#     for i in range(len(s)-1,-1,-1):
#         b+=s[i]
#     # print(b)
#     if s == b:
#         print(True)
#     else:
#         print(False)
# pali("level")

# def iterate(s,e):
#     for i in range(e):
#         print(s+i)
# iterate(25,5)


# reverse a word

# def reverse(s):
#     word = ""
#     res = ""
#     for i in s:
#         if i != " ":
#             word+=i
#         else:
#             res = word + " " + res
#             word=""

#     res = word + " " +res
#     print(res)
# reverse("iron man is flying")

# zero

# def zero(n):
#     count = 0
#     b = []
#     for i in n:
#         if i == 0:
#             count+=1
#         elif count == 1:
#             b.append(i)
#         elif count > 1:
#             break

#     print(b)
# zero([1,2,0,3,4,5,0,6,7])


# def prime(start, end):
#     for i in range(start, end + 1):
#         if i > 1:
#             value = True
#             for j in range(2, i):
#                 if i % j == 0:
#                     value = False
#                     break
#             if value:
#                 print(i, end=" ")


# prime(10, 20)

# prime num , fibo , factorual, second largest , algorithms , permunation , matrix , pattern , coimbations , gcd and lcm , anagram,panagram

# def prime(n):
#     for i in range(0,n+1):
#         if i > 1:
#             value = True
#             for j in range(2,i):
#                 if i % j == 0:
#                     value = False
#                     break
#             if value:
#                 print(i,end=" ")
# prime(10)

# def convert_railway(n):
#     s = n.split(":")
#     print(s)
#     result = ""
#     for i in s:
#         if int(i) > 12 :

# convert_railway("12:12:00AM")

# def fibonacci(n):
#     if n == 1:
#         return 0
#     elif n == 2 or n == 3:
#         return 1
#     elif n > 3:
#         return fibonacci(n-1) + fibonacci(n-2)

# def fibo(n):
#     print(fibonacci(n))

# fibo(5)


# def split_digits(n):
#     divisor = 1

#     # Find highest divisor (100, 1000, etc.)
#     while n // divisor >= 10:
#         divisor *= 10

#     result = []

#     # Extract digits
#     while divisor > 0:
#         digit = n // divisor
#         result.append(digit)
#         n = n % divisor
#         divisor //= 10

#     print(result)


# split_digits(132)

# def find_idx(n,m):
#     for i in range(0,len(n)):
#         for j in range(i+1,len(n)):
#             if n[i]+n[j] == m:
#                 print(i,j)
#                 return
# find_idx([5,7,8,9,10],15)


# def is_prime(n):
#     if n <= 1:
#         print("not a prime")
#     else:
#         value = True
#         for i in range(2,n):
#             if n % i == 0:
#                 value = False
#         if value:
#             print("Prime")
#         else:
#             print("Not Prime")
# is_prime(5)

# def con_prime(n):
#     for i in range(2,n+1):
#         value = True
#         for j in range(2,i):
#             if i % j == 0:
#                 value = False
#                 break
#         if value:
#             print(i , end=" ")
# con_prime(10)

# def ran_prime(s,e):
#     for i in range(s,e+1):
#         if i > 1:
#             value = True
#             for j in range(2,i):
#                 if i % j == 0:
#                     value = False
#                     break
#             if value:
#                 print(i,end=" ")
# ran_prime(0,10)

# def sec_lar(n):
#     max = n[0]
#     for i in n:
#         if i > max:
#             max = i
#     # print(max)
#     sec = n[0]
#     for j in n:
#         if j != max and j > sec:
#             sec = j
#     print(sec)

# sec_lar([2,3,4,5,6,7])


# def sec_lar(n):
#     first = ""
#     second = ""

#     for i in n:
#         if len(i) > len(first) :
#             second = first
#             first = i
#         elif len(i) > len(second) and i != first:
#             second = i
#     print(second)
# sec_lar(["yashika","kamalesh","Hari"])


# def matrix(n):
#     for i in n:
#         for j in i:
#             print(j)
# matrix([[10,35,11],[47,17,31]])
# def matrix(n):
#     rows = len(n)
#     # print(rows)
#     cols = len(n[0])
#     # print(cols)

#     for j in range(cols):
#         print (j)
#         for i in range(rows):
#             print(n[i][j],end=" ")
#         print()


# matrix([[10, 35, 11], [47, 17, 31]])

# def row_add(n):
#     count = 0
#     for i in n:
#         for j in i:
#             count+=j
#         print(count)
#         count = 0
# row_add([[1,2,3],
#          [4,5,6]])


# def col_add(n):
#     count = 0
#     row = len(n)
#     cols = len(n[0])
#     for i in range(cols):
#         for j in range(row):
#             a = n[i] + n[j]
#         print(a)
# col_add([[1,2,3],[4,5,6]])
