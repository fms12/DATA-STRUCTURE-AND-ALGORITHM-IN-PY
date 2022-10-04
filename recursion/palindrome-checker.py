def check(first, last):
    if(first >= last): 
        return True
    if(wordInput[first] != wordInput[last]): 
        return False 
    return check(first+1, last-1)

wordInput = input()
if(check(0, len(wordInput)-1)):
    print("Palindrome")
else:
    print("Not Palindrome")
