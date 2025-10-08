#  1st Problem

n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
o = n + m
if o % 2 == 0:
    print("Even")
else:
    print("odd")

# 2nd problem

a = int(input("Enter the first number: "))
b = a // 10
c = a % 10
m = b + c
j = b * c
if m + j == a:
    print ("Great")
else:
    print("Not Great")

#3 problem
a = input("Enter your a residential (or)  commercial : ")
b = int(input("Enter the units : "))
if a == 'residential':
    if b >= 0  and b <= 100:
        print( b * 3 ,"rupees")
    elif b >=101 and b <= 200:
        print(b * 5,"rupees")
    else:
        print(b * 7,"rupees")
else:
    if a == 'commercial':
        if b >=0 and b<=100:
            print(b * 5,"rupees")
        elif b >=101 and b<=200:
            print(b * 7,"rupees")
        else:
            print(b * 10,"rupees")
    
# 4th problem
a = int (input("Enter the distance : "))
b = 50
if a >=0 and a <=5:
    print(b)
elif a > 6 and a < 15:
    print(a * 8)
elif a >= 15:
    print(a * 6)
else:
    print("Invalid")

# 5th problem
a = int(input("Enter the first value : "))
b = int(input ("Enter the second value :"))
c = int(input("Enter the third value: " ))
if a == b == c:
    print("Equilateral")
elif a != b == c or a == b !=c or c == a != b:
    print("Isosceles ")
elif a != b != c:
    print("scalene")
else:
    print("Invalid")

# 6th problem
a = int(input("Enter the number: "))
if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0:
    print("Fizz")
else:
    print(a,"this number is does'nt divisible by 3 or 5")

# 7th problem
a = input("Enter the Stream (Science/Commerce/Arts) : ")
match a:
    case 'Science':
        b = input ("Enter the Sub choice (Medical or Engineering): ")
        match b:
            case 'Medical':
                print("You Chose Science - Medical")
            case 'Engineering':
                print("You Chose Science - Engineering")
            case _:
                print("Invalid Sub Choice")
    case 'Commerce':
        c = input("Enter the Sub choice (CA or B.Com): ")
        match c:
            case 'CA':
                print("You Chose Commerce - CA")
            case 'B.com':
                print("You chose Commerce - B.Com")
            case _:
                print("Invalid Sub Choice")
    case 'Arts':
        d = input("Enter the Sub Choice (Literature or History: ")
        match d:
            case 'Literature':
                print("You Chose Arts - Literature")
            case 'History':
                print("You Chose Arts - History:")
            case _:
                print("Invalid Sub Choice")
    case _:
        print("Invalid Stream")

# 8th problem
a = int (input("Enter the Show time in 24 hours format: "))
if a >= 9 and a <= 12:
    print("Morning Show")
elif a > 12 and a <= 16:
    print("Matinee Show")
elif a > 16 and a <= 20:
    print("Evening Show")
elif a > 20:
    print("Night Show")
else:
    print("Invalid Show time")

# 9th problem
a = int(input("Enter the A value in Kilometer : "))
b = int(input("enter the number 1 for (meter) 2 for (Centimeter) 3 for (millimeter) 4 for (miles): "))
match b:
    case 1:
        print(a * 1000)
    case 2:
        print(a * 100000)
    case 3:
        print(a * 1000000)
    case 4:
        print(a * 0.621371)
    case _:
        print("Invalid")
    
# 10th problem
a = input("Enter your payment mode( UPI / Card / NetBanking / COD ): ")
match a:
    case 'UPI':
        print("You selected UPI payment")
    case 'Card':
        print("You selected Debit/Credit Card payment")
    case 'NetBanking':
        print( "You selected Net Banking")
    case 'COD':
        print("You selected Cash on Delivery")
    case _:
        print("Invalid Payment Mode")


