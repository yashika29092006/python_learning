# a = int(input("enter the number : "))
# if a > 0:
#     print("Positive")
# elif a < 0:
#     print("Negative")
# elif a == 0:
#     print("zero")
# else:
#     print("Invalid")

# using function

# def number(a):
#     if a>0:
#         print("The number is positive")
#     elif a==0:
#         print("the number is zero")
#     else:
#         print("The number is negative" )
# number (8)
# number (-7)
# number (0)

#  e-comm

x = int(input("Enter amount: "))
y = int(input("Enter 1 for True (member), 0 for False (non-member): "))

if y == 1:
    print("Reward points earned:", x/10)
elif y == 0:
    print("No reward points (non-member)")
else:
    print("Invalid input")
