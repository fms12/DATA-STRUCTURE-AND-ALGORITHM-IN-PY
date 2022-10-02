# Python program to print diamond star pattern 

def pattern(n):
   i = 1
   while i<n:
      print(" "*(n-i) + "* " * i)
      i+=1 

   i = n
   while i>=1:
      print(" "*(n-i) + "* " * i)
      i-=1

pattern(5)

# Output
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *