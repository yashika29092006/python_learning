# Level3 :
# 1.Write a Python program that splits a sentence into words and finds the longest word in it.
# Sample Input:

# Data science evolves every year
# Sample Output:

# Longest word: science

# def find_long(n):
#     s = n.split(" ")
#     # print(s)
#     res = s[0]
#     for i in s:
#         if len(i) > len(res):
#             res = i
#     print(res)
# find_long("Data science evolves every year")            

# 2. Write a Python program to find the word that has maximum number of vowels from the given sentence
# Sample Input:
# Learning Python is interesting
# Sample Output:

# interesting

def find_max_vow(n):
    s = n.split(" ")
    vow = "aeiouAEIOU"
    l = []
    # print(s)
    for i in range(0, len(s)):
        count = 0
        for j in s[i]:
            if j in vow:
                count +=1
        l.append(count)
    max = l[0]
    for k in l:
        if k > max:
            max = k
    # print(max)
    print(s[i])



find_max_vow("Learning Python is interesting")
        
# 3. Write a python program to find the words that has more than 4 characters
# Sample Input:
# This is a python program
# Sample Output:
# python
# program
# def find(n):
#     s = n.split(" ")
#     for i in s:
#         if len(i) > 4:
#             print(i)
# find("This is a python program")
