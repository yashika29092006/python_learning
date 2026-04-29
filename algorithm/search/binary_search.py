def binary(arr,key):
    left = 0
    right =len(arr)-1
    while left <= right:
        center= (left+right)//2
        if arr[center] == key:
            return True
        elif arr[center] < key:
            left = center +1
        elif arr[center] > key:
            right = center - 1
    return -1
print(binary([10,20,30,40,50,60,70,80],20))


def bin(arr,key):
    l = 0
    r = len(arr)-1
    while l <= r:
        c = (l+r)//2
        if arr[c] == key:
            return True
        elif arr[c]<key:
            l = c +1
        elif arr[c] > key:
            r = c -1
    return -1
print(bin([10, 20, 30, 40, 50, 60, 70, 80], 20))
