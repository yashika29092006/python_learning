#  Earnings of a Salesperson:
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

# Lily’s Birthday Gifts:
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
