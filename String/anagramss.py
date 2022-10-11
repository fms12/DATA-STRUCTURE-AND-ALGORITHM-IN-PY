# function to check if two strings are
# anagram or not
def check(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("strings are anagrams.")
    else:
        print("strings aren't anagrams.")        
         
# driver code 
s1 ="bisgc"
s2 ="hjbnejt"
check(s1, s2)
