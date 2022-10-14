# Program for finding the multiplication_of_two_numbers(a, b)

def multiplication_of_two_numbers(a, b):
    if b == 1:  # base case
        return a  # checks if b == 1 than it returns a
    else:
        # adding a and calling the function again
        return a + multiplication_of_two_numbers(a, b-1)  # recursive call


a = int(input("Enter the first number:"))  # Taking input form user
b = int(input("Enter the second number:"))  # Taking input form user
print(multiplication_of_two_numbers(a, b))  # calling the function
