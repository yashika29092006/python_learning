

# - Write a function that merges two lists by taking elements alternately.

# ```python
# Input: x= [1, 2, 3] y= ['a', 'b', 'c']
# Output: [1, 'a', 2, 'b', 3, 'c']

# def merge(n,m):
#     result = []
#     for i in range(0,len(n)):
#         result.append(n[i])
#         result.append(m[i])
#     print(result)
# merge([1, 2, 3],['a', 'b', 'c'])   

# # - Write a Program that Keep Words That Start and End With the Same Letter

# # ```python
# # Case-insensitive matching.
# # Example:
# #  Input: ["level", "Apple", "mana", "cool"]
# #  Output: ["level", "mana"]

# def check_fir_las(n):
#     result = []
#     for i in n:
#         if i[0] == i[-1]:
#             result.append(i)
#     print(result)
# check_fir_las(["level", "Apple", "mana", "cool"])

# def find(names,birthday):
#     result = []
#     for i in range(len(birthday)):
#         month = int(birthday[i].split("/")[1])
#         if month in [1,2,3,4,5,6]:
#             result.append(names[i])
#     print(result)
# find(["hari","yashika","kamalesh","azhagan"],["01/05","02/09","03/08","04/06"])

# def check(n,m):
#     count = 0
#     if len(n) == len(m):
#         for i in range(0,len(n)):
#             if n[i] not in m[i]:
#                 count+=1
#         if count == 1:
#             print("yes")
#         else:
#             print("no")
#     else:
#         print("invalid")
# check("apple","apble")

# - Given a list of names, print only the ones that contain “a” or “A”.

# ```python
# Input: ["Meera", "John", "Kavi", "Sona"]
# Output: Meera Kavi Sona
# Explanation: These names include the letter 'a'

# def find(n):
#     y = "aA"
#     new =[]
#     for el in n:
#         if "aA" in el:
#             new.append(n)
#     print(new)
# find(["Meera", "John", "Kavi", "Sona"])


# - Given a list of strings , For Each word, Check whether the length of the element is odd and the middle letter of that word must be a vowel , print the words line by line

# ```python
# # test case 1
# Input: ["cat", "read", "room", "hello", "sky"]
# Output: cat

# def middle(n):
#     y = "aeiou"
#     for i in n:
#         count = 0
#         if len(i) % 2 != 0:
#             count +=1
#         mid_index = count // 2
#         p = 0
#         for j in i:
#             if p == mid_index:
#                 char = j
#             p+=1
#         if char in y:
#             print(i)
        
         
            
                
# middle(["cat,read","room","cream"])

# def find(n):
#     for i in n:
#         if len(i) % 2 != 0:
#             middle = len(i) // 2
#             if i[middle] in "aeiou":
#                 print(i)
# find(["cat", "read", "room", "hello", "sky"])

# def find(n):
#     rev = 0
#     while n > 0:
#         rev = rev * 10 + n % 10
#         n//=10
#     print(rev)
# find(123)

# def con_vow(n):
#     for i in n:
#         con = 0
#         vow = 0
#         for j in i:
#             if j in "aeiou":
#                 vow+=1
#             else:
#                 con+=1 
#         if con == vow:
#             print(i)
# con_vow(["room","kamal","yashikaa","ooss"])

