start =1 
end = 5
sum=0
while start <= end:
    sum= sum + start
    start = start+1
print(sum)


n = int(input("Enter :"))
i = 1
f = 1
while i <= n:
    f *= i
    i += 1
print(f)




n= int (input("enter"))
i=1
while i <= n:
    term=i**2+1
    print(term)
    i+=1

n=int(input("enter"))
m=int(input('enter'))
while m<=n:
    print(m)
    m+=1

n=int(input("enter"))
a=1
while a<= n:
    print(a**3)
    a+=1


start = int(input("Enter the starting number: "))
count = int(input("Enter how many numbers to print: "))

i = 0
while i < count:
    print(start + i, end=" ")
    i += 1

num = int(input("Enter number: "))
rev = 0
while num > 0:
    rev = rev*10 + num%10
    num //= 10
print("Reversed =", rev)


num = int(input("Enter number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Digits =", count)

num = int(input("Enter number: "))
temp = num
rev = 0
while num > 0:
    rev = rev*10 + num%10
    num //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print("Sum =", total)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print("HCF =", a)

N = int(input("Enter N: "))
i = 1
total = 0
while i <= N:
    total += i
    i += 1
print("Sum =", total)

n=int(input("enter"))
i=1
f=1
while i<=n:
    f*=i
    i+=1
print(f)


