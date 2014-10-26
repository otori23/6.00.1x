# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in 
# the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5
# For problems such as these, do not include raw_input statements or 
# define the variable s in any way. Our automated testing wil

s = 'azcbobobegghakl'
vowels = ("a", "e", "i", "o", "u")
numVowels = 0
for oneChar in s:
    if oneChar in vowels:
        numVowels += 1
print("Number of vowels: " + str(numVowels))