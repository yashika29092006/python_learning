def arr(n):
    min = n[0][0]
    max = n[0][0]
    for row in n:
        for el in row:
            if el > max:
                max = el
            if el < min:
                min=el
    print("max = ",max)
    print("min = ",min)
arr([[2,4,5],
     [6,7,8],
     [9,8,7]])
