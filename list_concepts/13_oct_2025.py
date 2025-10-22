#traversing 

numbers = [10,20,30,40,50]

# for i in range(0,len(numbers),+1):
    # print(numbers[i])
    
# empty-list
def add_numbers(n):
    #start
    #declare an empty list
    result = []
    for i in range(1,n+1,+1):
        result.append(i)
    print(result)
    #stop
    
add_numbers(3)
add_numbers(5)
foo = [10,20,30,40,50,60,70,80,90,100]

print(foo[1])
print(foo[2])
print(foo[-1])
print(foo[-2])
print(foo[-10])
print(len(foo))
(foo.append(110))
(foo.append(120))
print(foo)
print(foo[11])

##
print(foo[3:7])
print(foo[3:4])
##
print(foo[-7:-2])
##
print(foo[3:])
print(foo[:7])
