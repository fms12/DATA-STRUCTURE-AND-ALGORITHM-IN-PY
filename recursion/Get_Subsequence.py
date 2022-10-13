# get subsquence 
def gss(n):
    if(len(n)==0):
        ans = []
        ans.append('')
        return ans
    res = n[1:]
    ros= gss(res)
    mres = []
    for i in ros:
        mres.append(""+i)
    for j in ros:
        mres.append(n[0]+j)
    return mres


n = input()
print(gss(n))


"""
OUTPUT:
  abc
INPUT:
  ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
"""
