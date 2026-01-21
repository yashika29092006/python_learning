def bubble_sort(arr):
    if len(arr) == 0:
        return "invalid"
    else:
        swapped = True
        while swapped:
            swapped = False
            for i in range(0,len(arr)-1,+1):
                if arr[i] > arr[i+1]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                    swapped = True
        print(arr)
bubble_sort([40,10,30,20,60])

def fibo(n):
    a,b=0,1
    li = []
    for i in range(0,n):
        li.append(a)
        a,b = b,a+b
    return li
print(fibo(5))








