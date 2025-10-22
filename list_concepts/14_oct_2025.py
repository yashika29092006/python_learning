# 1. A manager wants to know how many employees worked more than 8 hours in a day.  
# The List contains the hours of each employee worked in their shift. 
  
# count_overtime([9, 7, 8, 10, 6, 9])  
# count_overtime([8, 8, 9, 10, 7])

def count(n):
    counts = 0
    for i in n:
        if i > 8:
            counts+=1
    print(counts)
count([9, 7, 8, 10, 6, 9])

# morning sums
def total_cost(n):
    total=0
    for i in n:
        total+=i
    print(total)
total_cost([200,100,50])

# 2. A librarian keeps a list of pages read each day. Find how many total pages were read on even-numbered days only.
# even_day_pages([10, 20, 15, 25, 30, 35])
# even_day_pages([5, 10, 20, 25])
# def even_day_pages(n):

# numbers = [100,200,500,200]
# total = sum(numbers)
# print("Total =", total)

def even(n):
    total = sum(n)
    for i in range(1,total+1):
        if i % 2 == 0:
            print(i)
even([10,20,15,25,30,35])


