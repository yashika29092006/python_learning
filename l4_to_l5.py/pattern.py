# basic

# def basic(n,m):
#     for i in range(n):
#         for j in range(m):
#             print("*",end="")
#         print()
# basic(3,3)

# right angle
# def right(r,c):
#     for i in range(r,c):
#         for j in range(i):
#             print("*",end="")
#         print()
# right(1,4)

# for i in range(1, 4):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# def num(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print()
# num(5)

# def num(n):
#     for i in range(1,n+1):
#         space = n - i
#         star = i
#         print(" " * space + " *" * star)
# num(3)

def num(n):
    for i in range(1,n+1):
        space = n - i
        star = i
        print(" *"*star+" "*space)
    for i in range(n-1,0,-1):
        space = n - i
        star =  i
        print(" *"*star+" "*space)
num(3)

# def num(n):
#     if n > 2:
#         for i in range(1,n+1):
#             if i == 1 or i == n:
#                 print("*"*n)
#             else:
#                 print("*"+" "*(n-2)+"*")
# num(4)

def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==j or i+j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
pattern(3)

# def pattern(n):
#     for i in range(n):
#         print(" "*i+str(n-i))
# pattern(5)

# def pattern(n):
#     for i in range(n):
#         for j in range(n):
#             if i == j or i +j == n-1:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
# pattern(3)
# def num(n):
#     for i in range(1,n+1):
#         space = n - i
#         star = i
#         print("  "*space+" *"*star )
#     for i in range(n-1,0,-1):
#         space = n - i
#         star =  i
#         print("  "*space+" *"*star)
# # num(3)


# matrix = [
#     [1, 3, 2],
#     [4, 6, 5],
#     [7, 9, 8]
# ]
# for i in matrix:
#     temp=i[0]
#     print(i)
#     print(i[0])
#     for j in i:
#         if j>temp:
#             temp=j
#     # print(temp)

# word="python is aisre is"
# point="is"
# count=0
# for i in range(len(word)-1):
#     if point[0]==word[i] and point[1]==word[i+1]:
#         count+=1
# print(count)

# s = word.split(" ")
# for i in s:
#     if i in point:
#         count+=1
# print(count)
# def num(n):
#     for i in range(1,n+1):
#         space = n - i
#         star = i
#         print(" " * space + " *" * star)
# num(3)

def pattern(n):
    for i in range(1,n+1):
            space = n -i
            star = i
            print( " "*space+" *"*star)
pattern(3)

