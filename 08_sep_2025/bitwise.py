# and operator


a=2
b=3
c=4
print(a & b  & c)     

a=1000
b=11
print(a  & b)

a=7
b=5
print(a  &  b)

# OR operator


a=5
b=4
print(a  | b)
print(7 | 5) 


# not operator

a=84
print("not=",~a)

# xor operator
a=2
b=3
print(a^b)

a=2
b=3
c=4
print(a^b^c)

# floor-division
print (5//2)

# left shift
x=5
print("x=",x<<1)

# right swift
x=4
print("x=",x>>2)

a, b = 10, 5
print("Before Swapping")
print("a value is", a)
print("b value is", b)


a = a + b
b = a - b
a = a - b

print("After Swapping")
print("a value is", a)
print("b value is", b)

p=int(input("enter the value"))
r=float(input("enter the value"))
n=int(input("enter the value"))
t=int(input("enter the value"))
a=p*(1+r/n)**(n*t)
ci=a-p
print(a)
print(ci)
