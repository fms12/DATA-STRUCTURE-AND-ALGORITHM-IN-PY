def multiplication_of_two_numbers(a, b):
    if b == 1:
        return a
    else:
        return a + multiplication_of_two_numbers(a, b-1)

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print(multiplication_of_two_numbers(a, b))
