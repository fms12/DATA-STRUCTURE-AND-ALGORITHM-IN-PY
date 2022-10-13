# Given a string, compute recursively a new string where all 'x' chars have been removed.

def removex(string):
    if(len(string)==0):
        return string
    smalcase = removex(string[1:])
    if (string[0]=='x'):
        return ""+ smalcase
    else:
        return string[0] + smalcase


string = input()
print(removex(string))
