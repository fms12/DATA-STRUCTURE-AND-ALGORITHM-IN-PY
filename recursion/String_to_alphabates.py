
# We are given a hashmap which maps all the letters with number. 
# Given 1 is mapped with A, 2 is mapped with B.....26 is mapped with Z. 
# Given a number, you have to print all the possible strings.
# Sample Input: 123
# Sample OutPut:ABC
  
def stringtoalpha(string,out):
    if(len(string)== 0):
        print(out)
        return 
    
    singleDigitNumber = ord(string[0]) - ord('0')
    ch = singleDigitNumber + ord('A') - 1
    stringtoalpha(string[1:],out+chr(ch))
string = input()
stringtoalpha(string,'')
