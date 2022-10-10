def factorial(n): 
      
    #checking for 1 and 0 factorial value
    if n in (1,0):
        return 1
      
    else:
          
        return (n * factorial(n - 1)) 
  
num = int(input("Enter the number to find factorial ")) 
print("number : ",num)
print("Factorial : ",factorial(num))
