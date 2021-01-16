n=int(input())
sp=n
st=1
for i in range(n):
    for j in  range(1,st):
        print(end='	')
    for j in range(sp):
        print('*',end='	')
    print()
    sp-=1
    st+=1
    
    
    >>>>>>>>>>>>>>>>>>>>>> output >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    *	*	*	*	*	
      *	*	*	*	
        *	*	*	
          *	*	
            *
