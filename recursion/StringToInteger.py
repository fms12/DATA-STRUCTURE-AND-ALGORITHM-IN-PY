# Convert String to Intgers By recursion
# eg:'123' to 123

def desending(s):
    if(len(s)==1):
        return ord(s[0]) - 48
    res = desending(s[1:])
    ros = ord(s[0])- 48
    j = ros*(10**(len(s)-1))+res
    return j


s = input()
print(desending(s))
