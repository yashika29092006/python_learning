def subs(val,sub):
    count = 0
    for i in range(len(val)-len(sub)+1):
        match = True
        for j in range(len(sub)):
            if val[i+j] != sub[j]:
                match = False
                break
        if match :
            count+=1
    print(count)
subs("this is islisand","is")


