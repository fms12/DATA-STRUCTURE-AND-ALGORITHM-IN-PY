QUESTION:
  
#1. Here are a few sets of inputs and outputs for your reference
#Input1 -> 1
#Output1 -> 1 1 1

#Input2 -> 2
#Output2 -> 2 1 1 1 2 1 1 1 2

#Input2 -> 3
#Output3 -> 3 2 1 1 1 2 1 1 1 2 3 2 1 1 1 2 1 1 1 2 3
#
#2. Figure out the pattern and complete the recursive function pzz to achieve the above for any positive number n.

PROGRAM:
  def zig(n):
    if(n==0):
        return
    print(n,end=' ')
    zig(n-1)
    print(n,end=' ')
    zig(n-1)
    print(n,end=' ')

    

n=int(input())
zig(n)
