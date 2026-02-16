# amount=int(input("enter the amount"))
# if amount >= 1000:
#     discount= amount * 0.10
#     x=amount-discount
#     print(amount-discount)

# elif amount >=500 and amount <=1000:
#     discount= amount * 0.5
#     x=amount-discount
#     print(x)
# elif amount<500:
#     print(amount)






# # x = 12  # 1100 in binary
# # y = 5   # 0101 in binary

# while x > 1:
#     x = x >> 1  # Right shift x by 1
#     y = y << 1 
#     print(x)
#     print(y)
# num = 15  # 1111 in binary
# shift_count = 0

# for i in range(4):
#     if num & 1:
#         shift_count += 1
#     num = num >> 1
#     print(num)

# def born_in_first_half(names, birthdates):
#     li = []      # months list
#     name = []    # final names list

#     # Extract month from each birthdate
#     for i in range(len(birthdates)):
#         y = birthdates[i].split("/")   # ["dd", "mm"]
#         li.append(int(y[1]))           # take the month (y[1])
#     print(y)
#     # Check month and add corresponding name
#     for i in range(len(li)):
#         if 1 <= li[i] <= 6:            # month between 1 and 6
#             name.append(names[i])      # add the matching name

#     print(name)

# born_in_first_half(
#     ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"],
#     ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]
# )

def hash(s):
    new = {}
    for i in s:
        if i in new:
            return True 
        else:
            new[i] = 1
    return False

print(hash("apple"))

def hash(s):
    new = {}
    for i in s:
        if i in new:
            new[i] += 1
        else:
            new[i] = 1
    # print(new)
    for j in new.values():
        print(j)
        if j > 1:
            return "True"
        else:
            return "False"

print(hash("apple"))

