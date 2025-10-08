#  Question 1
# A cinema charges:
# ₹150 for ages under 18
# ₹250 for ages 18–60
# ₹100 for ages above 60

def num(n):
    if n < 18:
        print(150)
    elif n <= 60:
        print(250)
    else:
        print(100)
num(19)
num(66)
num(2)
# Question 2
# Stadium ticket rules:
# age < 12 → ₹50
# age 12–59 → ₹120
# age ≥ 60 → ₹80
# If age is even, ₹5 discount.
def num(n):
    if  n > 0 and n < 12 :
        t=50
    elif n <= 59:
        t=120
    elif n <= 60 and n <= 100:
        t=80
    else:
        print("invalid")
    if n % 2 == 0:
        t-=5
    print(t)
num(55)
num(6)

# A shopkeeper has n mangoes.
# Each basket holds 5 mangoes.
# Find:
# Full baskets
# Leftover mangoes
def num(n):
    full=n//5
    print(full)
    left=n%5
    print(left)
num(23)
num(45)
# A child has n candies and eats one candy per day.
# Print how many are left each day.
def num(n):
    for i in range(1,n+1):
        l=n-i
        print('day',i,'=',l,'left')
num(4)

# An employee gets bonus on sales:
# ≥100 units → 10% bonus
# 50–99 units → 5% bonus
# <50 → no bonus
# Input: Salary and sales
# Output: Bonus and Total Salary
def num(n,m):
    if m >= 100:
        print(n // 10)
        print(int(n*1.10))
    elif m >=50 or m <=99:
        print(n//10)
        print(n*1.05)
    elif m < 50:
        print(n)
num(40000,103)
num(40000,99)

# Earnings of a Salesperson:
# ≤ ₹5000 → 5% commission
# ₹5001–₹10000 → 10%
# ₹10000 → 15%
# 7000 → 700  
# 12000 → 1800  
# 11000 → 1650
def num(n):
    if n <=5000:
        c=n*0.05
    elif n <10000 and n >=5001:
        c=n*0.10
    elif n >= 10000:
        c=n*0.15
    print(int(c))
num(7000)
num(12000)
num(11000)

# Question 7
# Shopping Discount:
# Price > 100 → 10% off
# Price 50–100 → 5% off
# Price <50 → no discount
# 200 → 180  
# 80 → 76  
# 40 → 40  
# 150 → 135
def num(n):
    if n > 100:
        d=(n*0.10)
    elif n >= 50:
        d=(n*0.5)
    elif n < 50:
        d=0
    f=n-d
    print(int(f))
num(200)
num(80)
num(40)
num(150)

# Taxi Charges:
# First 10 km → ₹15/km
# Next 20 km → ₹12/km
# Beyond 30 km → ₹10/km
# 15 → 180  
# 35 → 350  
# 10 → 150
def num(n):
    if n <= 10:
        print(n*15)
    elif n <=20:
        print(n*12)
    else:
        print(n*10)
num(15)
num(35)
num(10)
num(31)

# # Lily’s Birthday Gifts:
# Odd birthdays → 1 toy
# Even birthdays → money (₹10, ₹20, ₹30, …)
# 10
# 5
# 150.00
def lily_gifts(n):
    toys = 0
    money = 0
    amount = 10

    for i in range(1, n + 1):
        if i % 2 != 0:
            toys += 1
        else:
            money += amount
            amount += 10

    print(toys)
    print(money)
lily_gifts(10)
