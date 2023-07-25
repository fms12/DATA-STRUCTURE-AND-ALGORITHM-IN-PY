def desending(s):
    if(len(s) == 1 and s != 'π'):
        return s
    elif(len(s) == 1 and s == 'π'):
        return '3.14'

    res = desending(s[1:])
    if(s[0]=='p' and s[1]=='i'):
        return '3.14'+res[1:]
    elif (s[0] == 'π'):
        return '3.14' + res
    else:
        return s[0]+res

if __name__ == "__main__":
    s = input()
    print(desending(s))
# INPUT
# xpipippixx, xπpπx
# OUTPUT
# x3.143.14p3.14xx
