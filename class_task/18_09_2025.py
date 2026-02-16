# Level 3:
# Find the smallest word in a sentence.
# Input: "Python is super powerful"
# Output: is
# 2. A list is strictly increasing if every next element is greater than the previous one.
# Example:
# [1,3,5,9] → True
# [2,2,5] → False (because 2 is NOT less than 2)
# [10,5,6] → False (because 5 < 10)
# 3. Reverse characters only at even index positions Indices: 0,2,4,6,...
# Input: "abcdefg" Even positioned letters: a, c, e, g → reverse → g, e, c, a
# Final Output: "gbecdfa"
# 4. Replace characters at odd indexes with *.
# Example: "hello" → "h*l*o" (edited) 
# :+1::+1::skin-tone-2:
# 27

def find_small(s):
    long = ""
    current = ""
    for i in s:
        if i != " ":
            current+=i
            # print(current)
        else:
            if len(long) < len(current):
                current = long
            current = ""
    if len(long) < len(current):
        long = current
    print(long)
find_small("Python is super powerful")

# 1
def find_small(s):
    sentence = s.split()
    s = sentence[0]
    for i in sentence:
        if len(i) < len(s):
            s = i
    print(s)
find_small("Python is super powerful")

# 2
def greater(value):
    x = value[0]
    y = [x]
    # print(y)
    for i in range(1,len(value)):
        if value[i] > x:
            y.append(value[i])
            x = value[i]
            print(True)
            break
        else:
            print(False)
            break
greater([1,3,5,9])
greater([2,2,5])
greater([10,5,6])

# 3
# def even(s):
#     x = ""
#     y= ""
#     result = ""
#     for i in range(0,len(s),2):
#         x = s[i]+x
#     # print(x)
#     for k in range(1,len(s),2):
#         y +=s[k]
#     # print(y)
#     for j in x:
#         result+=j
#         result+=y
#     print(result)
#         # break
# even("abcdefg")

def even_replace(s):
    even = ""
    result = ""
    e_index = 0

    for i in range(0, len(s), 2):
        even = s[i] + even

    for i in range(0,len(s)):
        if i % 2 == 0:
            result += even[e_index]
            e_index += 1
        else:
            result += s[i]

    print(result)

even_replace("abcdefg")

#4
def replace(n):
    result = ""
    for i in range(0,len(n)):
        if i % 2 != 0:
            result+="*"
        else:
            result+=n[i]
    print(result)
replace("hello")
        

    
def find_first_occurence(arr, value):
    index = -1
    for i in range(0, len(arr)):
        if arr[i] == value:
            index = i
            break
    print(index)
find_first_occurence([9, 7, 4, 1, 7, 0], 7)

def first(a,b):
    for i in range(0,len(a)):
        if a[i] == b:
            print(i)
            return
    print(-1)
first([1,2,3,4,5],5)





