# level 1

# odd or even
n=int(input("Enter the number :"))
if n % 2== 0:
    print("Even")
else:
    print("odd")

# mark grading
n=int(input("enter your mark"))
if n >=90 and n<=100:
    print("a")
elif n >=75:
    print("b")
elif n >= 50:
    print("c")
else:
    print("fail")

# days by using match case
n=int(input("enter the number:"))
match n:
    case 1:
        print("MON")
    case 2:
        print("TUE")
    case 3:
        print("WED")
    case 4:
        print("THUR")
    case 5:
        print("FRI")
    case 6:
        print("SAT")
    case 7:
        print("SUN")
    case _:
        print("Invalid input")

# while loop 
n= int(input("enter the number"))
i=1
sum=0
while i <=n:
    sum+=i
    i+=1
print(sum)

#  tables using forloop 2*2=4(n , loop , n*l)
n=int(input("enter the number:"))
b = 1
a=10
for i in range (b,a+1,+1):
    print(n,"x",i,"=",n*i)

# level 2
# palindrome
n=(input("enter the number:"))
if n==n[::-1]:
    print("p")
else:
    print("not")

# calculator
n=int(input("Enter the 1:"))
m=int(input("enter the 2:"))
o=input("enter the operator")
if o=='+':
    print(n+m)
elif o=='-':
    print(n-m)
elif o=='*':
    print(n*m)
elif o=='/':
    print(n/m)
else:
    print("invalid")

# match month
n=int(input("enter the number:"))
match n:
    case 1:
        print("JAN")
    case 2:
        print("FEB")
    case 3:
        print("MAR")
    case 4:
        print("Apr")
    case 5:
        print("MAy")
    case 6:
        print("JUN")
    case 7:
        print("JUL")
    case 8:
        print("AUG")
    case 9:
        print("SEP")
    case 10:
        print("OCT")
    case 11:
        print("NOv")
    case 12:
        print("DEC")
    case _:
        print("Invalid")

#  reverse number using while
n = int(input("Enter the number: "))
a = 0

while n > 0:
    a = a * 10 + n % 10
    n = n // 10

print("Reversed number:", a)

a = int(input("Enter the first number: "))
b = a // 10
c = a % 10
m = b + c
j = b * c
if m + j == a:
    print ("Great")
else:
    print("Not Great")

n=int(input("Enter the number:"))
if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print("Not a prime")
            break
    else:
        print("prime")
else:
    print("Invalid")

# prime number
n=int(input("enter the number:"))
m=int(input("enter the second num:"))
for j in range(n,m,1):
    if j > 1:
        for i in range(2,j):
            if j % i == 0:
                break
        else:
            print(j , end =" ")

# 1. If / Else
# User oru integer input kuduppan.
# Number positive ah irundha "Positive" print pannu.
# Zero ah irundha "Zero" print pannu.
# Negative ah irundha "Negative" print pannu.

def num(n):
    if n > 0:
        print("p")
    elif n < 0:
        print("N")
    elif n == 0:
        print("zer")
num(4)
num(0)
num(-1)

