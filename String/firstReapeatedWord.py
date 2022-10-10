
# Python program to find first repeated word in a string
def solve(s):
 
    mp = {} # to store occurrences of word
    t = ""
    ans = ""
     
    # traversing from back makes sure that we get the word which repeats first as ans
    for i in range(len(s) - 1,-1,-1):
       
        # if char present , then add that in temp word string t
        if(s[i] != ' '):
            t += s[i]
         
        # if space is there then this word t needs to stored in map
        else:
         
            # if that string t has occurred previously then it is a possible ans
            if(t in mp):
                ans = t
            else:
                mp[t] = 1
             
            # set t as empty for again new word
            t = ""
             
    # first word like "he" needs to be mapped
    if(t in mp):
        ans=t
                         
    if(ans!=""):
 
        # reverse ans string as it has characters in reverse order
        ans = ans[::-1]
        print(ans)
    else:
        print("No Repetition")
 
# driver code
u = "Ravi had been saying that he had been there"
v = "Ravi had been saying that"
w = "he had had he"
solve(u)
solve(v)
solve(w)
