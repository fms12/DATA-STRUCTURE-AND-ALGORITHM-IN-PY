def desending(s):
    if(len(s) == 1):
        return s
    res = desending(s[1:])
    if(s[0]=='p' and s[1]=='i'):
        return '3.14'+res[1:]
    else:
        return s[0]+res    
s = input()
print(desending(s))

#INPUT
# xpipippixx
# OUTPUT
# x3.143.14p3.14xx
