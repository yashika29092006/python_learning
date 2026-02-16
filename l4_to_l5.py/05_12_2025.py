# def convert_railway(n):
#     s = n.split(":")
#     print(s)
#     result = ""
#     for i in s:
#         if int(i) > 12 :
            
# convert_railway("12:12:00AM")

# bubble sort
a = [4,3,2,7,1]
for i in range(len(a)):
    for j in range((len(a)-i)-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
