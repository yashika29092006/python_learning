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






# x = 12  # 1100 in binary
# y = 5   # 0101 in binary

# while x > 1:
#     x = x >> 1  # Right shift x by 1
#     y = y << 1 
#     print(x)
#     print(y)
num = 15  # 1111 in binary
shift_count = 0

for i in range(4):
    if num & 1:
        shift_count += 1
    num = num >> 1
    print(num)