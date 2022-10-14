n = int(input())
sp = n-1
st = 1
for i in range(n):
    for j in range(sp):
        print(end='	')
    for j in range(st):
        print('*', end=' ')
    print()
    sp -= 1
    st += 1

# skipcq
"""
Output
                *
            *	*
        *	*	*
    *	*	*	*
*	*	*	*	*
"""
