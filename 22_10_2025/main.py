# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.
# You must:
# - Solve it using an inbuilt function (split()).
# - Solve it without using any inbuilt split functions — by using loops and conditions.
# Given:
# sentence = "Emma-is-a-data-scientist"
# Expected Output:
# Emma
# is
# a
# data
# scientist
 
# using inbuilt function
def split(sentence):
    final = sentence.split("-")
    for i in final:
        print(i)
split("Emma-is-a-data-scientist")

# without using inbuilt function
def sent(sentence):
    temp= " "
    for i in sentence:
        if i != "-":
            temp += i
        else:
            print(temp)
            temp = " "
    print(temp)
sent("Emma-is-a-data-scientist")

# 2. Write a Python program to reverse a given string in two ways:
# - Using an inbuilt function or slicing
# - Without using any inbuilt functions/Slicing
# Given:
# str1 = "Python"
# Expected Output:
# nohtyP

# using inbuilt function
def reverse(sentence):
    final=sentence[::-1]
    print(final)
reverse("Python")

# without using inbuilt function
def reverse(sentence):
    temp = " "
    for i in sentence:
        temp = i+temp
    print(temp)
reverse("Python")


# 3. Write a Python program to count the number of consonants in a given string.
# Input:
# Hello World
# Output:
# Number of consonants: 7

def consonants(sentence):
    count = 0
    for i in sentence:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U' and  i != " ":
            count+=1
    print("Number of consonants: ",count)
consonants("Hello World")

# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome

# using inbuilt function
def remove_spaces(sentence):
    final=sentence.split(" ")
    for i in final:
        print(i,end='')
remove_spaces("Python is awesome")

# without using inbuilt function
def remove_spaces(sentence):
    temp = ""
    for i in sentence:
        if i != " ":
            temp += i
    print(temp)
remove_spaces("Python is awesome")

# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong

def is_strong_password_or_not(password):
        if len(password) >= 8 :
            for i in password:
                  if i == "!" or i == "@" or i == "#" or i == "$" or i == "%" or i == "^" or i == "&" or i == "*":
                        return "Password is strong"
            else:
                return "Password is not strong"
        else:
            return "Please enter atleast 8 character"
print(is_strong_password_or_not("Yashika$1234"))






 