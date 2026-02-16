# - Vowel Extractor  
#   Write a program to extract only the vowels from a given word and store them in a list.  
#   Print the list at the end.

# ```python
# Input: word = "education"
# Output: ['e', 'u', 'a', 'i', 'o']

def is_vowels(n):
    new = []
    if len(n) == 0 :
        print("invalid")
    else:
        for i in n:
            if i in "aeiouAeiou":
                new.append(i)
        print(new)
is_vowels("education")

# - Find Word with Maximum Vowels
#   Given a list of words, find which word has the highest number of vowels and print that word.

# ```python
# Input: words = ["cat", "eagle", "umbrella", "sky"]
# Output: umbrella
# ```

def words(a):
    b = ['a','e','i','o','u']
    c =[]
    for i in a:
        if i not in b:
            i = max(a)
    print(i)
words(["cat", "eagle", "umbrella", "sky"])
# - Given an array of integers, count how many numbers are even and how many are odd.

# ```python
# Example Input: [1, 2, 3, 4, 5, 6, 7]
# Example Output: { even: 3, odd: 4 }

def count_even_or_odd(n):
    even = 0
    odd = 0
    dict = {}
    for i in n:
        if i % 2 == 0:
            even+=1
        elif i % 2 != 0:
            odd+=1
    dict["even"] = even
    dict["odd"] = odd
    return dict       
print(count_even_or_odd([1, 2, 3, 4, 5, 6, 7]))

# - Given an array of integers and a target element, find the indices of its first and last occurrence.
#   (Bonus point: Try to return the output in a dictionary format)

# ```python
# Example: numbers = [5, 2, 3, 5, 7, 5, 8] key= 5
# Example Output: { firstIndex: 0, lastIndex: 5 }
def find_occurrence(n,m):
    first = -1
    last = -1
    for i in range(0,len(n)):
        if n[i] == m:
            if first == 0:
                first =i
            last =i
    return {"firstIndex": first, "lastIndex": last}
print(find_occurrence([5, 2, 3, 5, 7, 5, 8],5))        

# - Combine Two Lists Alternately
#   Write a Python program to combine two lists by picking elements alternately.
#   (Assume both lists are of the same length.)

# ```python
# Input:
# list1 = [10, 20, 30]
# list2 = [1, 2, 3]
# Output: [10, 1, 20, 2, 30, 3]
def combine_list(n,m):
    new=[]
    for i in range(0,len(n)):
        new.append(n[i])
        new.append(m[i])
    print(new)
combine_list([10, 20, 30],[1, 2, 3])
