# 9.Given 2 numbers a and b (a < b). Print all the
# numbers between a and b.
a = 5, b = 8
5
6
7
8

def num(a,b):
    i=a
    while i <= b:
        print(i)
        i+=1
num(1,5)

# 8.Print the N terms in reverse. 
# n = 5, output 5 4 3 2 1
def num(n):
    i=1
    while i <= n:
        print(n)
        n-=1
num(5)

# 7.Write a program to generate the first 'n' terms of the following series 1, 4, 9, 16, 25,...

def num(n):
    i=1
    if n <=0:
        print("invalid input")
    else:
        while i <=n:
            print(i**2)
            i+=1
num(-1)

# 6.Implement a calculator program where we have operators (it can be ‘+’, ‘/’, ‘*’, ‘-’) and two numbers number1 and number2. Based on the character the program should add, subtract, multiply and divide accordingly.
# Eg if operator = ‘+’, number1=10, number=25 print 35.

def num(a,b,c):
    match c:
        case '+':
            print(a+b)
        case '-':
            print(a-b)
        case '*':
            print(a*b)
        case '/':
            print(a/b)
        case _:
            print("Invalid input")
num(2,4,'+')
        
# 5.Given three numbers a, b, c print the maximum number amongst the three.
# a =10, b = 30, c = 5
# print 30

def num(a,b,c):
    if a > b and a >c:
        print(a)
    elif b >a and b >c:
        print(b)
    else:
        print(c)
num(10,20,30)

# Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.
def num(n,l,r):
    if n > l and n < r:
        print("Yes")
    else:
        print("no")
num(3,2,6)

# 4.You are designing a program to determine the outcome of a cricket match based on the Duckworth-Lewis 
# method due to rain interruptions. 

# If the team score is greater than or equal to target score, print "Team wins by DL method" 
# If team score is less than target score but overs left is greater than 0, print "Match to be continued" 
# If team score is less than target score and overs left is 0, print "Team loses by DL method"

def num(team, target, overs):
    if team >= target:
        print("Team wins by DL method")
    elif team <= target and overs > 0:
        print("Match to be continued")
    else:
        print("Team loses by DL method")
num(170,200,2)

# # 3.Given a number print if it’s even number or not
# num = 2, print even
# num = 5, print not even

def num(n):
    if n % 2 ==0:
        print("even")
    else:
        print("odd")
num(5)
num(2)


# leap year
def num(n):
    if n % 100 != 0 or n % 400 == 0 and n % 4 == 0:
        print("yes")
    else:
        print("no")
num(2000)
num(1900)
num(2020)

# 35.  Let "N" be a positive integer. Write a program to check whether this number is divisible by 3 or 5. 
# Print "Divisible" if it is divisible by either 3 or 5, and "Not Divisible" otherwise.

def num(a):
    if a % 3 == 0 and a % 5 == 0:
        print("Divisible")
    else:
        print("Not")
num(3)
num(15)

# century btw 2001 and 2100
def num(n):
    if n >= 2001 and n <= 2100:
        print("21st century")
    else:
        print("Not")
num(2025)
num(1999)

# 33.Get an Input age from the user and classify based on the following criteria:
# Child (<13),
# Teen (13–19),
# Adult (20–59),
# Senior (60-100).
# Sample Input:
# 28
# Sample Output:
# Adult
# Sample Input 1:
# 14
# Sample Output 2:
# Teen

def num(n):
    if n <=100 and n >=60:
        print("S")
    elif n < 60 and n >=20:
        print("A")
    elif n < 20 and n >=13:
        print("T")
    elif n < 13:
        print("c")
num(100)
num(12)
num(60)

# Given 3 sides, check if they can form a triangle (sum of two sides > third).
def num(a,b,c):
    d=a+b
    if d > c:
        print("yes")
    else:
        print("no")
num(3,4,5)

# 31.Write a program to check if the mark falls in the below mentioned range.
# A -> 100 to 80
# B -> 60 to 79
# C -> 50 to 59
# D -> 40 to 49
# lesser than 40 - Fail
# Sample Input:
# 77
# Sample output:
# B (edited) 

def num(n):
    if n < 0 or n >100:
        print("Invalid")
    else:
        if n <= 100 and n >= 80:
            print("A")
        elif n >=60 and n<80:
            print("b")
        elif n >=50 and n<40:
            print("c")
        elif n >=40 and n<50:
            print("d")
        else:
            print("fail")
num(101)
num(-1)
num(60)
num(38)

#  while loop
# 28. Find the sum of all numbers from 1 to 5 (both inclusive) using a while loop.
def num(n):
    i=1
    sum=0
    while i <= n:
        sum+=i
        i+=1
    print(sum)
num(5)


# 27. Write a program in Python that asks the user for a number and then prints its multiplication table from 1 to 10 using a while loop.
def num(n):
    i = 1
    b=10
    while i <= b:
        print(n,'x',i,'=',n*i)
        i+=1
num(5)
num(6)

# 26. Print all numbers divisible by 5 between 0 to 100 using while loop
def num(n):
    i=1
    if n <=0:
        print("invalid")
    else:

        while i <= n:
            if i % 5 == 0:
                print(i)
            i+=1
num(100)


# for loop
# Find the factorial of a number N using a for loop.
def num(n):
    i=1
    fact=1
    while i <= n:
        fact*=i
        i+=1
    print(fact)
num(5)
num(6)

def num(n):
    a=1
    fact=1
    for i in range (a,n+1):
        fact*=i
    print(fact)
num(5)


# Print the multiplication table of 2 (from 2 × 1 up to 2 × 10) using a for loop.
def num(n):
    for i in range(1,10+1):
        print(n,'x',i,'=',n*i)
num(5)

# Find the sum of all even numbers up to N using a for loop.
def num(n):
    sum=0
    for i in range(2,n+1):
        if i % 2 == 0:
            sum+=i
    print(sum)
num(20)

# Find the sum of all numbers from 1 to 5 (both inclusive) using a for loop.
def num(n):
    sum=0
    for i in range(1,5+1):
        sum+=i
    print(sum)
num(5)

# Using a for loop, print all even numbers between 1 and 20.
def num(a,b):
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i)
num(1,20)

# Using a for loop, Print all even numbers between 1 and 5.
def num(a,b):
    for i in range(a,b+1):
        if i % 2==0:
            print(i)
num(1,5)

# Using a for loop, Print numbers from 1 to 5 using a for loop
def num(a,b):
    for i in range(a,b+1):
        print(i)
num(1,5)

#  24.Input a number N and print all powers of 2 up to 2^N using a while loop.Example: N = 4 → 2, 4, 8, 16(while loop)
def num(n):
    i=1
    while i <= n:
        print(2**i)
        i+=1
num(4)

def num(n):
    if n<=0:
        print("invalid")
    else:
        for i in range(1,n+1):
            print(2**i)
num(-1)

# 23. Write a program that prints the squares of numbers from 1 to 10 using a while loop. Output should look like: 1, 4, 9, 16, …, 100
def num(n):
    i=1
    while i <=n:
        print(i**2)
        i+=1
num(10)

def num(n):
    for i in range (1,n+1):
        print(i**2)
num(10)

# Function to calculate waiting time
def waiting_time(N, X):
    if N == 1:
        print(0)
    else:
        print((N - 1) * X)

# Get input from user
N = int(input("Enter number of cars: "))
X = int(input("Enter time per car: "))

# Print result
print("Waiting time of last person:", waiting_time(N, X))

# Print the integers in a single line separate by space.
def num(a,b,c):
    print(a,b,c,)
num(1,2,3)

# 20.A food delivery app gives free delivery if the order amount is above ₹500. 
# If the order is less than or equal to ₹500, a delivery charge of ₹50 is added. 
# Write a program that takes the order amount from the user. 
# Print whether delivery is free or charged and prints the total amount as well.

def num(n):
    if n >=500:
        print("free")
    elif n<=500 :
        print("charged",n+50)
num(550)
num(450)

# 2. Print the sum of all even numbers between a and b. if a = 5, and b = 10 then it should print 24.
# Explanation: Between 5 and 10 there is 6, 8 and 10 and their sum is 24
def num(a,b):
    i = a
    sum=0
    while a <= b:
        if a % 2 == 0:
            sum+=a
        a+=1
    print(sum)
num(5,10)

#  reverse number using while
def num(n):
    rev = 0
    while n > 0:
        rev=rev*10 + n % 10
        n=n//10
    print(rev)
num(123)
num(456)

# palindrome
def num(n):
    if n == n[::-1]:
        print("pal")
    else:
        print("not")
num("66")
num("689")

def num(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    if temp == rev:
        print("pali")
    else:
        print("not")

num(66)  # pali
num(73)  # not

# prime num
n=int(input("enter the num"))
if n > 0:
    for i in range (2,n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("prime")
else:
    print("invalid")

n=int(input("enter the start num:"))
m=int(input("enter the sec num:"))
for j in range(n,m+1):
    if j > 1:
        for i in range(2,j):
            if j % i == 0:
                break
        else:
            print(j,end=" ")

# 1st
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

# 2. If / Elif
# User oru integer input kuduppan (1–12).
# Month number kuduppan.
# 1 → "January", 2 → "February", … up to 12 → "December".
# Input 1–12 illa na "Invalid month" print pannu.

def num(n):
    if n == 1:
        print("m")
    elif n == 2:
        print("t")
    elif n==3:
        print("w")
    elif n == 4:
        print("th")
    elif n == 5:
        print("fr")
    elif n==6:
        print("sat")
    elif n==7:
        print("sun")
    else:
        print("invalid")
num(3)
num(-1)

# User oru character input kuduppan (vowel or consonant).
# If letter is one of a, e, i, o, u (uppercase or lowercase) → "Vowel"
# Else if it’s alphabet but not vowel → "Consonant"
# Else → "Not a letter"
def num(n):
    match n:
        case 'a' | 'A' |'e'|'E'|'i'|'I'|'o'|'O'|'u'|'U':
            print("Vowels")
        case _:
            print("not")
num('A')
num('Z')

# 4. While Loop
# User oru integer input kuduppan (n).
# While loop use pannitu reverse of the number print pannu.
#  Example: n = 1234 → print 4321

def num(n):
    i =1
    rev=0
    while i <=n:
        rev=rev*10+n%10
        n //=10
    print(rev)
num(123)

# factorial
def num(n):
    i=1
    fact=1
    while i <= n:
        fact*=i
        i+=1
    print(fact)
num(5)
def num(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
num(5)

def num(n):
    i=0
    a,b=0,1
    while i < n:
        print(a,end=" ")
        a,b=b,a+b
        i+=1
n=int(input("enter"))    
if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print("not")
            break
    else:
        print("prime")


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
    
