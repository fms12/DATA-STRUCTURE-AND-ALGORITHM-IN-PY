class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
#         initializing length in s and t
        if ls > lt:
#     checking whether ls is greater than lt
            return False
        i = j = 0
#   initializing i and j with 0
        while i < ls and j < lt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == ls
#       if i and ls are equal it returns true
