#Program for printing the zigzag of a number
def print_zigzag(n):
    if n == 0: #base case
        return
    print(n, end=" ") #printing the number one by one
    print_zigzag(n-1) #recursive call
    print(n, end=" ") #printing the number one by one
    print_zigzag(n-1) #recursive call
    print(n, end=" ") #printing the number one by one

n = int(input("Enter the number:")) #Taking input form user
print_zigzag(n) #calling the function
