# # 1
# a=5
# b=10
# a,b=b,a
# print("a=",a)
# print("b=",b)
# # 2
# temp=a
# a=b
# b=temp
# print("a=",a)
# print("b=",b)
# # 3
# a,b=10,5
# a=a+b
# b=a-b
# a=a-b
# print("a=",a)
# print("b=",b)


def sec(n,m):
    count = 0
    li = []
    fi = []
    for i in n:
        li.append(i)
    # print(li)
    for i in range(0,len(li)):
        if li[i] in m:
            count+=1
            fi.append(li[i])
            
    print(count)
    print(fi)
sec("this is island",'is')
