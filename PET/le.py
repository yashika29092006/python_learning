#  Question 1
# A cinema charges:
# ₹150 for ages under 18
# # ₹250 for ages 18–60
# # ₹100 for ages above 60
def num(n):
    if n >=0 and n < 18:
        print("150")
    elif n >= 18 and n <= 60:
        print("250")
    elif n > 60:
        print("100")
    else:
        print("invalid")
num(-1)
num(66)

# Question 2
# Stadium ticket rules:
# age < 12 → ₹50
# age 12–59 → ₹120
# age ≥ 60 → ₹80
# If age is even, ₹5 discount.
def num(n):
    if n<=0:
        print("invalid")
    else:
        if n > 0:
            if n > 12:
                a = 50
            elif n >=12 and n <=59:
                a = 120
            elif n >= 60:
                a = 80
            else:
                print("invalid")
            if n % 2 == 0:
                a-=5
            print(a)
num(-1)
num(18)

# A shopkeeper has n mangoes.
# Each basket holds 5 mangoes.
# Find:
# Full baskets
# Leftover mangoes
def num(n):
    full=n//5
    print('Full baskets',full)
    left=n%5
    print('Leftover mangoes',left)
num(23)

# A child has n candies and eats one candy per day.
# Print how many are left each day.
def num(n):
    for i in range(1,n+1):
        n-=1
        print('day',i,'left',n)
num(4)

# An employee gets bonus on sales:
# ≥100 units → 10% bonus
# 50–99 units → 5% bonus
# <50 → no bonus
# Input: Salary and sales
# Output: Bonus and Total Salary
def num(n,m):
    if m >= 100:
        bonus=n*0.10
        total=n+bonus
    elif m >= 50 and m <= 99:
        bonus=n*0.05
        total=n+bonus
    elif m < 50:
        bonus=0
        total=n+bonus
    print(int(bonus))
    print(total)
num(40000, 30)

# Earnings of a Salesperson:
# ≤ ₹5000 → 5% commission
# ₹5001–₹10000 → 10%
# ₹10000 → 15%
# 7000 → 700  
# 12000 → 1800  
# 11000 → 1650
def num(n):
    if n <= 5000:
        f=n*0.05
    elif n>=5001 and n<10000:
        f=n*0.10
    elif n >= 10000:
        f=n*0.15
    print(int(f))
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
        t=n*0.10
    elif n >= 50 and n <= 100:
        t=n*0.05
    elif n < 50:
        print("no discount")
    d=n-t
    print(int(d))
num(200)
num(80)

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
    elif n >10 and n < 30:
        print(n*12)
    elif n >= 30:
        print(n*10)    
num(15)
num(35)
num(10)

# Lily’s Birthday Gifts:
# Odd birthdays → 1 toy
# Even birthdays → money (₹10, ₹20, ₹30, …)
# 10
# 5
# 150.00
def num(n):
    toy=0
    money=0
    amount=10
    for i in range(1,n+1):
        if i % 2 != 0:
            toy+=1
        else:
            money += amount
            amount += 10
    print(toy)
    print(money)
num(10)

# bharath sir
# Write a function to print all numbers from a to b using a loop.
def print_numbers(a, b):
    # write your code here
    for i in range(a,b+1):
        print(i)
print_numbers(1, 5)
print_numbers(3, 8)
print_numbers(10, 12)

# Write a function to print all numbers from b to a in reverse order using a loop.
def print_reverse(b, a):
    for i in range(b,a-1,-1):
        print(i)
print_reverse(10, 5)
print_reverse(7, 1)
print_reverse(20, 15)

# Write a function to print all even numbers between a and b using a loop.
def print_even(a, b):
    # write your code here
    for i in range(a,b+1,1):
        if i % 2 == 0:
            print(i)
print_even(1, 10)
print_even(4, 12)
print_even(7, 15)

# Write a function to print all numbers between a and b that are divisible by a given number n.
def print_divisible(a, b, n):
    # write your code here
    for i in range (a,b+1):
        if i % n == 0:
            print(i)
print_divisible(1, 20, 3)
print_divisible(10, 30, 5)
print_divisible(5, 25, 7)

# # Write a function to print all odd numbers between a and b in reverse order using a loop.
def print_odd_reverse(a, b):
    # write your code here
    for i in range (b,a-1,-1):
        if i % 2 != 0:
            print(i)
print_odd_reverse(1, 10)
print_odd_reverse(5, 15)
print_odd_reverse(10, 20)

# Write a function to count how many odd numbers are between a and b.
def count_odd(a, b):
    # write your code here
    count=0
    for i in range(a,b+1):
        if i % 2 != 0:
            count+=1
    print(count)
count_odd(1, 10)
count_odd(5, 20)
count_odd(10, 15)

# # Write a function to count how many numbers are divisible by a given number between a and b.
def count_divisible(a, b, n):
    # write your code here
    count=0
    for i in range(a,b+1):
        if i % n == 0:
            count+=1
    print(count)
count_divisible(1, 10, 2)
count_divisible(5, 25, 3)
count_divisible(10, 50, 5)

# # Write a function to find the sum of all numbers from a to b using a loop.
def sum_range(a, b):
    # write your code here
    sum = 0
    for i in range (a,b+1):
        sum=sum+i
    print(sum)
sum_range(1, 5)
sum_range(3, 7)
sum_range(10, 12)

# Write a function to find the sum of numbers from 1 to n.
def sum_to_n(n):
    # write your code here
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)
sum_to_n(5)
sum_to_n(10)
sum_to_n(3)

# Write a function to find the factorial of a given number using a loop.
def factorial(n):
    # write your code here
    i = 1
    fact = 1
    while i <= n:
        fact*=i
        i+=1
    print(fact)
factorial(5)
factorial(3)
factorial(7)

# # Write a function to calculate taxi fare based on the following rates:
# First 10 km → ₹15/km
# Next 20 km → ₹12/km
# Beyond 30 km → ₹10/km
def taxi_fare(distance):
    # write your code here
    if distance <= 10:
        print(distance*15)
    elif distance > 10 and distance < 30:
        print(distance*12)
    elif distance >= 30:
        print(distance*10)
taxi_fare(10)
taxi_fare(15)
taxi_fare(35)

# Write a function to calculate total reward for a given number of steps.
#  For every 1000 steps → ₹5
#  Every 5000th step → bonus ₹20
def total_reward(steps):
    # write your code here
    if steps < 5000:
        a=(steps//1000)*5
        print(a)
    elif steps >= 5000:
        b=(steps//1000)*5
        bonus=(steps//5000)*20
        total=b+bonus
        print(total)

total_reward(4000)
total_reward(6000)
total_reward(10000)

def steps(a):
    if a < 1000:
        print('you dont have any points')
    else:
        if a >= 1000 and a <5000:
            b = (a // 1000)*5
            print(b)
        elif a >= 5000:
            d=(a // 1000)*5
            bonus=(a//5000)*20
            total=d+bonus
            print(total)
steps(4000)
steps(2000)
steps(6000)
steps(13000)
steps(20000)
steps(500)