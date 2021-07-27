def duplicate(s):
    if(len(s) <= 1):
        return s
    res= s[1:]
    ros = duplicate(res)
    if(s[0]==ros[0]):
        return ros
    return s[0]+ros

s = input()
print(duplicate(s))
