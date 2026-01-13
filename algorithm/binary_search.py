def binary(arr,key):
    left = 0
    right = len(arr) -1
    while left <= right:
        center = (left + right) // 2
        if arr[center] == key:
            return True
        elif arr[center] < key:
            left = center + 1
        else:
            right = center - 1
    return -1

    # calling function
lists = [10,20,30,40,50,60,70]
y = 20
result = binary(lists,y)

if result != -1:
    print("Found")
else:
    print("Not Found")

# method 2 
def binary(arr,key):
    left = 0
    right = len(arr) -1
    while left <= right:
        center = (left + right) // 2
        if arr[center] == key:
            return True
        elif arr[center] < key:#go to right side
            left = center + 1
        elif arr[center] > key:#go to left side
            right = center - 1
    return -1
print(binary([10,20,30,40,50,60,70],20))



