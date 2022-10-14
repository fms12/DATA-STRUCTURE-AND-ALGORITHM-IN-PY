def isAnagram(s1, s2):
    # If both strings don't use the same letters with the same frequencies,  
    # then it's not an anagram, else it is.
    counter = {}
    
    for char in s1:
        counter[char] = counter.get(char, 0) + 1
        
    for char in s2:
        counter[char] = counter.get(char, 0) - 1
        
    # If s2 is an anagram of s1, then all the values of our counter should be 0.
    return all(val == 0 for val in counter.values())


print(isAnagram('anagram', 'nagaram'))  # True
print(isAnagram('rat', 'car'))  # False
