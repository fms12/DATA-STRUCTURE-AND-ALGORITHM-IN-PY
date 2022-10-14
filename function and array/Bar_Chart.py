def bar(arr):
    height = max(arr)
    for i in range(height):
        for _, arr_value in enumerate(arr):
            if (arr_value >= height-i):
                print("*", end='\t')
            else:
                print(end='\t')
        print()


n = input()
arr = [int(i) for i in input().split()]
print(bar(arr))


# skipcq
"""
Output
i can do like  also  that we can start the first loop form 7 and end with 1
so there is no need to be a (height-i) is here only to reduce value
and check until the same value encouter anf print the star. else print
the space

5
3 1 0 7 5


i 7         *
  6         *
  5         *	 *
  4         *	 *
  3   *			*	 *
  2   *			*	 *
  1   *	*		*	 *
      3 1 0 7  5
      j
"""
