# Python3 program to find all LCS of two strings in
# sorted order.
MAX=100
lcslen = 0
 
# dp matrix to store result of sub calls for lcs
dp=[[-1 for i in range(MAX)] for i in range(MAX)]
 
# A memoization based function that returns LCS of
# str1[i..len1-1] and str2[j..len2-1]
def lcs(str1, str2, len1, len2, i, j):
 
    # base condition
    if (i == len1 or j == len2):
        dp[i][j] = 0
        return dp[i][j]
 
    # if lcs has been computed
    if (dp[i][j] != -1):
        return dp[i][j]
 
    ret = 0
 
    # if characters are same return previous + 1 else
    # max of two sequences after removing i'th and j'th
    # char one by one
    if (str1[i] == str2[j]):
        ret = 1 + lcs(str1, str2, len1, len2, i + 1, j + 1)
    else:
        ret = max(lcs(str1, str2, len1, len2, i + 1, j),
                  lcs(str1, str2, len1, len2, i, j + 1))
    dp[i][j] = ret
    return ret
 
# Function to print all routes common sub-sequences of
# length lcslen
def printAll(str1, str2, len1, len2,data, indx1, indx2, currlcs):
     
    # if currlcs is equal to lcslen then print
    if (currlcs == lcslen):
        print("".join(data[:currlcs]))
        return
 
    # if we are done with all the characters of both string
    if (indx1 == len1 or indx2 == len2):
        return
 
    # here we have to print all sub-sequences lexicographically,
    # that's why we start from 'a'to'z' if this character is
    # present in both of them then append it in data[] and same
    # remaining part
    for ch in range(ord('a'),ord('z') + 1):
 
        # done is a flag to tell that we have printed all the
        # subsequences corresponding to current character
        done = False
 
        for i in range(indx1,len1):
            # if character ch is present in str1 then check if
            # it is present in str2
            if (chr(ch)==str1[i]):
              for j in range(indx2, len2):
 
                # if ch is present in both of them and
                # remaining length is equal to remaining
                # lcs length then add ch in sub-sequence
                if (chr(ch) == str2[j] and dp[i][j] == lcslen-currlcs):
                  data[currlcs] = chr(ch)
                  printAll(str1, str2, len1, len2, data, i + 1, j + 1, currlcs + 1)
                  done = True
                  break
 
            # If we found LCS beginning with current character.
            if (done):
                break
 
# This function prints all LCS of str1 and str2
# in lexicographic order.
def prinlAllLCSSorted(str1, str2):
    global lcslen
    # Find lengths of both strings
    len1,len2 = len(str1),len(str2)
 
    lcslen = lcs(str1, str2, len1, len2, 0, 0)
 
    # Print all LCS using recursive backtracking
    # data[] is used to store individual LCS.
    data = ['a' for i in range(MAX)]
    printAll(str1, str2, len1, len2, data, 0, 0, 0)
 
# Driver program to run the case
if __name__ == '__main__':
    str1 = "abcabcaa"
    str2 = "acbacba"
    prinlAllLCSSorted(str1, str2)
 
