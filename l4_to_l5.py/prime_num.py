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

def prime(start,end):
    for i in range(start,end+1):
        if i >1:
            value = True
            for j in range(2,i):
                if i % j == 0:
                    value = False
                    break
            if value:
                print(i,end =" ")
prime(10,20)
