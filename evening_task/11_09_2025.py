# task 1 --- Bharath sir
# Tara and Jyoti were given one number each. She has to find whether the sum of the two numbers is divisible by 5 or not . If yes then print 1 else print 0
tara=int(input("enter the value 1 : "))
jyothi=int(input("enter the value 2 : "))
n=tara+jyothi
if n % 5 == 0:
    print("1")
else:
    print("0")


# task 2
# Given a number N, print yes if the number is a multiple of 7 else print no.
n = int(input("enter the number : "))
if n % 7 == 0:
    print("yes")
else:
    print("no")

# task 3 ---- Sathiya Sir
# A food delivery app gives free delivery if the order amount is above ₹500. If the order is less than or equal to ₹500, a delivery charge of ₹50 is added. Write a program that takes the order amount from the user. Print whether delivery is free or charged and prints the total amount as well. 

n = int(input("Enter the amount you ordered : "))
if n > 500:
    print("free")
else :
    print("charged",n+50)

# task 4 
# Find the Grades from the user input for the marks.
# Let "X" be marks obtained through input.
# Write a program to check if the mark falls in the below mentioned range.
# A -> 100 to 80
# B -> 60 to 79
# C -> 50 to 59
# D -> 40 to 49
# lesser than 40 - Fail
# Sample Input:
# 77
# Sample output:
# B (edited) 
# A -> 100 to 80
# B -> 60 to 79
# C -> 50 to 59
# D -> 40 to 49



x = int(input("Enter your marks: "))
if x >= 80:
    print("Your Grade is A")
elif x >= 60:
    print("Your Grade is B")
elif x >= 50:
    print("Your Grade is C")
elif x >= 40:
    print("Your Grade is D")
else :
    print("Your Grade is E")

# Task 5 
# Given 3 sides, check if they can form a triangle (sum of two sides > third).
# Sample Input:
# 3
# 4
# 5
# Sample Output:
# YES
# Ref:
# 3 + 4 = 7 which is greater than the third side 5


a = int(input("Enter the first Number : "))
b = int(input ("Enter the second Number :"))
c = int(input("Enter the third number :"))
d = a + b 
if d > c:
    print("YES")
else:
    print("No")

# Task 6 
# Get an Input age from the user and classify based on the following criteria:
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


x = int(input("Enter your age: "))
if x >= 60:
    print("senior")
elif x >= 20:
    print("Adult")
elif x >= 13:
    print("Teen")
else :
    print("Child")



mark = int(input("Enter your marks: "))
match mark:
    case m if m >= 80 & m <= 100:
        print("Your Grade is A")
    case m if m >=60:
        print("Your Grade is B")
    case m if m >=50:
        print("Your Grade is C")
    case m if m >=40:
        print("Your Grade is D")
    case m if m < 40 :
        print("Your Grade is E")
    case _:
        print("Invalid")


mark = int(input("Enter your marks: "))
match mark:
    case m if 80 <= m <= 100:
        print("Your Grade is A")
    case m if 60 <= m < 80:
        print("Your Grade is B")
    case m if 50 <= m < 60:
        print("Your Grade is C")
    case m if 40 <= m < 50:
        print("Your Grade is D")
    case m if 0 <= m < 40:
        print("Your Grade is E")
    case _:
        print("Invalid input")

# print vowels or not using match case
v = input("enter the vowel :")
match v:
    case 'a'|'A'|'e'|'E'|'i'|'I'|'o'|'O'|'u'|'U':
        print("VOWELS")
    case _:
        print("Constant")



# age problem
age=int(input("enter your age"))
if age >0 and age <5:
    print("FREE")
elif age >= 5 and age <=12:
    print("10")
elif age >=13 and age <= 64:
    print("20")
elif age >=65:
    print("15")
else:
    print("invalid")


# print month using match case
monthNumber=int(input("enter the number between (1-12) : "))
match monthNumber:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("may")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("october")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid")