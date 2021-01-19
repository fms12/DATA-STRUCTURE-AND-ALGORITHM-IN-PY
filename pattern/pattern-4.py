n=int(input())
sp=n//2
st=1
for i in range(n):
    for j in  range(sp):
        print(end='	')
    for j in range(st):
        print('*',end='	')
    if i<n//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2
    print()
    
    >>>>>>>>>>>>>>>>  output >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    
    
    		*	
 	  *	*	*	
      *	  *	*	*    *	
	  *	*	*	
		*	
