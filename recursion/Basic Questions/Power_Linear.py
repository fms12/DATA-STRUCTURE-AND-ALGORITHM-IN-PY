# Program for finding the power of a number

def power_of_a_linear(x, n):
    if n == 0:  # base case
        return 1  # checks if n == 0 than it returns 1 so x dosen't get multiplied by 0

    # x gets multiplied everytime when the function is called and n does not become 0    
    return x * power_of_a_linear(x, n-1)  # recursive call


x = int(input("Enter the number:"))  # Taking input of a number form user
n = int(input("Enter the power:"))  # Taking input of power from user
print(power_of_a_linear(x, n))  # calling the function
