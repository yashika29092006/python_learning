a=int(input("enter the year:"))
if a % 100 != 0 and a % 4 ==0 or a % 400 == 0:
    print("Y")
else:
    print("N")

a= 5
b=10
sum=0
while a <= b:
    if a % 2 == 0:
        sum+=a
    a+=1
print(sum)

# 3. Write a program that calculates the shipping cost for an e-commerce product based
# on weight. If the weight is less than or equal to 5 kg, the shipping cost is $10; if the
# weight is more than 5 kg but less than or equal to 20 kg, the cost is $20; for more than
# 20 kg, the cost is $50. Please add 5% tax to the end shipping cost.
# ● Input: The weight of the product in kilograms.
# ● Output: The shipping cost (edited)

n = int(input("enter the weight:"))
if n <= 5:
    print(10*1.05)
elif n <=20:
    print(20*1.05)
else:
    print(50*1.05)

# 4. The newly appointed Vice-Chancellor of Anna University wanted to create an automated
# grading system for the students to check their grades. When a student enters the marks, the
# grading system displays the corresponding grade. Now, write a program to display the grade if
# marks are entered. Marks scored Grade 100 S 90 - 99 A 80 - 89 B 70 - 79 C 60 - 69 D 50 - 59 E
# < 50 F
# Input Format:
# The input consists of one integer which corresponds to the marks scored by the student.
# Output Format:
# The output consists of any one of the following grades S, A, B, C, D, E, or F.
# If a student's mark is greater than 100, print Invalid input

n=int(input("Enter the marks:"))
if n >0:
    if n ==100:
        print("Grade S")
    elif n >=90:
        print("grade a")
    elif n >=80:
        print("grade b")
    elif n >=70:
        print("grade c")
    elif n >=60:
        print("grade d")
    elif n >=50:
        print("grade e")
    elif n<50:
        print("f")
else:
    print("Invalid")

m=input("enter the food(p for pizza,b for burger,s for sandwich :)")
n=int(input("enter the quantity:"))
if n < 0 or m=='p''b''s':
    print("Invalid")
else:
    if m =='p':
        print(200*1.05*n)
    elif m=='b':
        print(100*1.05*n)
    elif m=='s':
        print(50*1.05*n)







    