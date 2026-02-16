# ### LISTS

# - You are given a list of integers and a target number.
#   Your task is to identify two different elements in the list whose sum equals the target.
#   Return the indices of those two elements.

# ```python
# Input:
# # nums = [2, 7, 11, 15]
# # target = 9
# Output:
# # [0,1]

# Input:
# # nums = [3,2,4], target = 6
# Output:
# # [1,2]

def find(n,m):
    for i in range(0,len(n)):
        for j in range(i+1,len(n)):
            if n[i]+n[j] == m:
                print(i,j)
find([2,3,4],6)

# - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# ```python
# Input: nums = [1,2,3,1]
# Output: True

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True

# Input:  nums = [1,2,3,4]
# Output: False


def nums(a):
    for i in a:
        b = []
        count = 0
        if i not in b :
            for j in a:
                if i == j:
                    count+=1
        if count >= 2:
            print(True)
            break
        else:
            print(False)
            break
                    # b+=i
            # print(i,count)
nums([1,2,3,1])
nums([1,1,1,3,3,4,3,2,4,2])
nums([1,2,3,4])
# nums([1,2,3,4])
        