def find(n):
    for i in n:
        if i > 100:
            return i
print(find([50,120,90,300,150]))
print(find([200,80,60,180]))

# Given an array of integers, move all zeros to the end without changing the order of the non-zero elements.
# Example Input:
#  [0, 1, 0, 3, 12]
# Example Output:
#  [1, 3, 12, 0, 0]

def num(n):
    zero = 0
    new =[]
    for i in n:
        if i != 0:
            new.append(i)
        else:
            zero+=1
    for j in range(zero):
        new.append(0)
    return new
print(num([0, 1, 0, 3, 12]))

# Find Leader Elements in List
# An element is leader if it is greater than all elements       to its right.
# Example:
#  List: [10, 22, 12, 3, 0, 6]
#  Output leaders → 22, 12, 6

# Find Second Largest Number
# Write a Python program to find the second largest number in a list without using max() or sort().
#  Example:
#  Input → [10, 40, 30, 20, 50]
#  Output → 40
nums = [1, 2, 3, 2, 2, 4]
target = 2
count = 0
for i in range(0,len(nums)):
    if nums[i] == target:
        count += 1
print(count)

s1 = "cat"
s2 = "cat"
for i in range(len(s1)):
    if s1[i] != s2[i]:
        print("diff")
    else:

        print("Same")

# Given a list of words, print the words that start with a vowel.

# Assume all words are in lower case.

# words = ["apple", "banana", "orange", "grape"]

# Output: 

# apple
# orange

# def print_no_vowel(words):
#     for i in words:
#         if words[0] == 'a' or words[0] == 'e' or words[0] == 'i' or words[0] == 'o' or words[0] == 'u':
#             print(i)
def print_no_vowel(words):
    for word in words:  # directly iterate over elements, not indices
        if word[0] in 'aeiou':  # check if first character is a vowel
            print(word)
words = ["apple", "banana", "orange", "grape"]
print_no_vowel(words)

# You are given two lists:

# One list shows the gender of each student ('M' for male, 'F' for female).

# The other list shows their marks in the same order.

# Write a Python program to:

# Find the average marks of male students.

# Find the average marks of female students.

# Print "Male <average>" if male students have the higher average, or "Female <average>" if female students have the higher average.

def find_higher_average(gen_list, marks_list):
    male_count = 0
    female_count = 0
    male_avg =0
    female_avg = 0
    male_sum = 0
    female_sum = 0
    for i in range(0,len(gen_list)):
        if gen_list[i] == 'M':
            male_sum += marks_list[i]
            male_count+=1
        else:
            female_sum+=marks_list[i]
            female_count+=1
    male_avg=male_sum/male_count
    female_avg=female_sum/female_count
    if male_avg > female_avg:
        print(male_avg)
    else:
        print(female_avg)
    	
find_higher_average(['M','F','M','F','M','F','M'],
                    [81.5, 70.0, 98.5, 60.0, 75.0, 50.0, 85.0])
find_higher_average(['M','F','M','F','M','F','M'],
                    [59.5, 80.0, 61.0, 79.0, 60.5, 81.0, 60.0])



#  max
def birthday(n):
    count = 0
    max = n[0]
    for i in range(0,len(n)):
        if n[i] >= max:
            max=n[i]
    for j in n:
        if j>=max:
            count+=1
    print(count)
birthday([4,4,3,1])