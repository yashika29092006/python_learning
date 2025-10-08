# def num(a,b):
#     for i in range (a,b+1):
#         print(i)
# num(10,20)

# def count(a,b,n):
#     total=0
#     for i in range(a,b+1):
#         if i % 2 == 0:
#             total=total+1
#     print(total)
#     if n == 0:
#         print("invalid")

# count(10,20,2)
# count(10,15,2)
# count(10,10,2)
# count(10,20,0)

# def count(a,b,n):
#     total = 0
#     if n > 0:
#         for i in range(a,b+1):
#             if i % 2 == 0:
#                 total=total+1
#         print(total)
#     else:
#         print("invalid")
# count(10,20,2)
# count(10,15,2)
# count(10,10,2)
# count(10,20,0)
# count(10,20,-1)

def steps(a):
    if a < 1000:
        print('you dont have any points')
    else:
        if a >= 1000 and a <5000:
            b = (a // 1000)*5
            print(b)
        elif a >= 5000:
            d=(a // 1000)*5
            bonus=(a//5000)*20
            total=d+bonus
            print(total)
steps(4000)
steps(2000)
steps(6000)
steps(13000)
steps(20000)
steps(500)



            






    