def selection_sort(n):
    y = len(n)
    for i in range(0,y):
        min_idx=i
        for j in range(i+1,y):
            if n[j] < n[min_idx]:
                min_idx = j

        temp = n[min_idx]
        n[min_idx] = n[i]
        n[i] = temp
    return n
print(selection_sort([65,35,75,98,100]))

# time complexity = O(n^2)

def selection(n):
    m = len(n)
    for i in range(0,m-1):
        idx = i
        for j in range(i+1,m):
            if n[idx] > n[j]:
                idx = j
        n[i],n[idx] = n[idx],n[i]
    return n
print(selection([65,35,75,98,100]))


