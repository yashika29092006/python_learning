# 1
a=5
b=10
a,b=b,a
print("a=",a)
print("b=",b)
# 2
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)
# 3
a,b=10,5
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)
