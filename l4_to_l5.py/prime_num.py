# def prime(n):
#     if n > 2:
#         for i in range(2,n):
#             if n % i == 0:
#                 print("not")
#                 break
#             else:
#                 print("prime")
#                 break
# prime(4)

# method
# def prime(n):
#     if n < 2:
#         print("invalid")
#     else:
#         value = True
#         for i in range(2,n):
#             if n % i == 0:
#                 value = False
#         if value:
#             print("prime")
#         else:
#             print("not")
# prime(5)

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

# def prime(start,end):
#     for i in range(start,end+1):
#         if i >1:
#             value = True
#             for j in range(2,i):
#                 if i % j == 0:
#                     value = False
#                     break
#             if value:
#                 print(i,end =" ")
# prime(10,20)


def rev(b):
    rev = 0
    while b > 0:
        l = b % 10
        rev = rev * 10 + l
        b = b //10
    print(rev)

rev(123)

def sum(n):
    total = 0
    while n != 0:
        total += n % 10 
        n //= 10
    print(total)
sum(123)

def ana(o,u):
    if len(o) != len(u):
        return False
    count = {}
    for i in o:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    
    for j in u:
        if j not in count:
            return False
        count[j]-=1
    print(count)
    for key in count:
        if count[key] != 0:
            return False
    return True
print(ana("listens","silent"))

def min(n):
    mini = n[0]
    maxi = n[0]
    for i in n:
        if i < mini:
            mini = i
        elif i > maxi:
            maxi = i
    print(mini,maxi)
min([1,2,3,4])
