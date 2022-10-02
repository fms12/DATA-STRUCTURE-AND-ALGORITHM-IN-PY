#Program for printing the multiplication table of a number

def multiplicationTable(n, i=1):
    if i == 11: #base case if n == 11 than it returns
        return
    print(n, 'x', i, '=', n*i) #printing the multiplication table one by one
    multiplicationTable(n, i+1) #recursive call

n = int(input("Enter the number:")) #Taking input form user
multiplicationTable(n) #calling the function
