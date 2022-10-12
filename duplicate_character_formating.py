# Problem: Take a string and write a recursive funtion which returns a string in which all duplicate consecutive characters are seperated by a *.Print thhe value returned.

# Sample Input: Hello

# Sample Output: Hel*lo

#Source Code:

def DuplicateChar(s):
    if(len(s)<=1):
        return s
    ros = DuplicateChar(s[1:])
    if(s[0]==ros[0]):
        return s[0] + "*" + ros
    return s[0]+ros

s=input("Enter the string:")

print(DuplicateChar(s))
