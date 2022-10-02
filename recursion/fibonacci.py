def fib(n):
  if n<=1:
    return n
  else:
    return fib(n-1) + fib(n-2)

count = int(input("Enter the limit: "))

if count<=0:
  print("Enter a number greater than 0")
else:
  for i in range(count):
    print(fib(i),end=" ")
