def geometric_sum(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)  
number=int(input("Enter the number"))
print(geometric_sum(number))
