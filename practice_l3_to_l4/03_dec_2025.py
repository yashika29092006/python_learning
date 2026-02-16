def average(n):
    sum = 0
    avg = 0
    count = 0
    if len(n) == 0:
        print("Array is empty")
        return
    else:
        for i in n:
            sum+=i
            avg = sum /len(n)
        for j in n:
            if j > avg :
                count+=1
    print(count)
average([10,20,30,40,50])
average([5,5,5,5])
average([])

def rem_dup(n):
    res = ""
    if n == "":
        print("string is empty")
    for i in n:
        if i not in res:
            res+=i
    print(res)
rem_dup('programming')
rem_dup("")

def find_long(n):
    res = ""
    s = n.split(" ")
    big = s[0]
    if n == "":
        print("your input str is empty")
    else:
        for i in s:
            if len(i) > len(big):
                big = i
        print(big)
find_long("Python makes enjoyable programming")   
find_long("")

def find(n):
    m = 500
    je = 3000
    t = 1500
    p = 10
    res = 0
    for i in n:
        s = int(i.split(" ")[1])
        k = i.split(" ")[0]
        # print(n)
        for j in k:
            if j == "M":
                res += m * s
            elif j == "J":
                res += je * s
            elif j == "T":
                res += t * s
            elif j == "P":
                res += p * s
    print(res)
find(["M 3", "J 1", "T 2"])
find(["P 5", "M 1"])

# def find(n,m):
#     o = []
#     for i in range(0,len(n)):
#         mo =int(m[i].split("/")[1])
#         # print(mo)
#         if mo <= 6:
#             o.append(n[i])
#     print(o)
# find(
#     ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", "Gita", "Hari"],
#     ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05", "15/06", "01/12"]
# )

