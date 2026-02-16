# def find(n):
#     count = 0
#     word = {}
#     new = []
#     for i in n:
#         if i in word.keys():
#             word[i]=word[i]+1
#         else:
#             word[i]=1
#     # print(word)
#     for j in word.values():
#         new.append(j)
#         # max = 0
#         # if j >= max:
#         #     max = j
#     max=0
#     for k in new:
#         if k >= max:
#             max = k
#     print(max) 
# find("success")
# find("python")

# def first(n):
#     x = n[0]
#     for i in range(1,len(n)):
#         if n[i] == ' ':
#             x=x+n[i+1]
#     print(x.upper())
# first("indian army uni")

# def sent(n):
#     x=n.split(" ")
#     # print(x)
#     y = x[0]
#     flag = None
#     for i in range(1,len(x)):
#         if x[i] == ' ':
#             flag=i+1
#             y+=n[flag].upper()
#         elif x[i]!=flag:
#             print(n[i]) 
#     print(y)
# sent("welcome to india")

# def sent(n):
#     words = n.split(" ")         
#     camel_case = ""             
#     for word in words:
#         camel_case += word.capitalize() 
#     print(camel_case)

# sent("welcome to india")
  

# def vowel(n):
#     vowel_co=0
#     con_co=0
#     x='aeiou'
#     for i in n:
#         if i in x:
#             vowel_co+=1
#         else:
#             con_co+=1
#     print("vowel ",vowel_co,"constant ",con_co)
# vowel("Python is a programming language")
# vowel("Yashika")

# Given a list of words, print the words that start with a vowel.

# Assume all words are in lower case.

# words = ["apple", "banana", "orange", "grape"]

# Output: 

# apple
# orange
# 
# def vowel(n):
#     # x='aeiou'
#     for i in n:
#         if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u' :
#             print(i)
# vowel(["apple","banana","orange","cake"])

# def bracket(n):
#     count = 0
#     for i in n:
#         if i == '(':
#             count+=1
#         elif i == ')':
#             count -= 1
#             if count < 0:
#                 print("False")
#                 break
#     if count == 0:
#         print(True)
# bracket("(())")
# bracket("())(")     

# Write a program to read a list of integers containing exactly two zeros.
# Your task is to print all the numbers that appear between these two zeros, without using slicing or nested loops.

# If there is no closing zero after the first one, print -1.

# Example 1:

# Input: [1, 2, 0, 3, 4, 5, 0, 6, 7] Output: [3, 4, 5]

# Explanation:

# The first 0 occurs at index 2 and the second 0 occurs at index 6.
# The numbers between them are 3, 4, and 5.

# Example 2:

# Input: [0, 10, 20,0, 30] Output: [10,20]
# def zero (n):
#     li=[]
#     result =[]
#     for i in range(0,len(n)):
#         if n[i]== 0:
#             li.append(i)
#     # print(li)
#     start=li[0]
#     end=li[1]
#     for j in range(start+1,end):
#         result.append(n[j])
#     print(result)
# zero([1,2,3,0,4,5,6,0,9,8])

# def even(n):
#     sum=0
#     for i in n:
#         if i % 2 == 0:
#             sum+=i
#     print(sum)
# even([2, 7, 4, 9, 12])
def print_capital_words(sentence):
    words = sentence.split(" ")  # split the sentence into words
    for word in words:
        if len(word) > 0:  # to avoid empty strings
            first_char = word[0]
            if 'A' <= first_char <= 'Z':  # check if capital
                print(word)

# Test
print_capital_words("Today we met Rahul and Priya in Chennai")


