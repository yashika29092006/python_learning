def sub_array(n):
    res = []
    for i in range(0,len(n)):
        for j in range(i,len(n)):
            temp = n[i:j+1]
            print(temp)
            sums = sum(temp)
            res.append(sums)
            print(sums)
            print(res)
    # print(max(res))
sub_array([1,2,3])