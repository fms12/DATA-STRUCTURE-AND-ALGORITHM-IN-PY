def stringtoInt(str):
    if(len(str) == 1):
        return ord(str[0]) - ord('0')

    y = stringtoInt(str[1:])

    x = ord(str[0]) - ord('0')

    x = x*(10**(len(str)-1)) + y

    return x

str = "12345"
print(stringtoInt(str))