# Question 1:
# Write a Python program to check if a given string is a Pangram or not.
# A Pangram is a sentence that contains every letter of the English alphabet (a–z) at least once. 
# The check should be case-insensitive, meaning both uppercase and lowercase letters are treated the same.

# Test Case 1:
# Input:The quick brown fox jumps over the lazy dog
# Output:True

# Explanation:
# The input string contains all the letters from ‘a’ to ‘z’, so it is a Pangram.

# Test Case 2:
# Input: The quick brown fox jumps over the dog
# Output: False

# Explanation:
# The input string is missing some letters (‘l’, ‘z’, and ‘y’), so it is not a Pangram.


def panagram(n):
    count = 0
    x = 'abcdefchijklmnopqrstuvwxyz '
    for i in x:
        if i in n:
            return True
        else:
            return False
print(panagram("the quick brown fox jumps over the lazy dog"))
print(panagram("the quick brown fox jumps over the dog"))



# Question 2: 

# Write a Python program to check whether a given sentence is a palindrome sentence or not.
# A palindrome sentence is one that reads the same forward and backward after processing.

# Test Case 1:
# Input: Too hot to hoot
# Output: True

# Test Case 2:
# Input: Abc 012 10cbA
# Output: True
def pali(n):
    a=''
    b=n.lower()
    for i in range(0,len(b)):
        if b[i] not in " ":
            a+=b[i]
    # print(a)
    for j in range(len(a)-1,-1,-1):
        # print(a[j])
        if a[j] == b:
            return True
        else:
            return False

#     for i in range(len(n)-1,-1,-1):
#         # if n[i] in n:
#             a=a+n[i]
#     print(a)
# #         else:
# #             return False
print(pali("Too hot to hoot"))
# print(pali("Abc 012 10cbA"))
# print(pali("abc"))



    