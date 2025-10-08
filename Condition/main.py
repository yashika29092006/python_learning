# condition Statement
x=5
y=3
print("Condition is",x > y)
print("condition is",x < y)
print("condition is",x == y)
print("condition is",x >= y)
print("condition is",x <= y)
print("condition is",x!=y)

# even or odd
a=int(input("Enter the number :"))
if a%2==0:
    print("Even")
else:
    print("odd")

# leap year 
n=int(input("Enter the year :"))
if n % 4 == 0:
    print("Leap year")
else:
    print("Not a Leap year")

# Number is divisible by 3 or 5
n = int (input ("Enter the number :"))
if n % 3 == 0 or n % 5 == 0:
    print("Divisible")
else:
    print("Not Divisible")

#21st Century Or not
n = int (input ("Enter the year :"))
if n >= 2001 and n <= 2100:
    print("21st century")
else:
    print("Not in 21st century")