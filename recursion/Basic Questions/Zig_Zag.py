
def print_zigzag(n):
    if n == 0:
        return
    print(n, end=" ")
    print_zigzag(n-1)
    print(n, end=" ")
    print_zigzag(n-1)
    print(n, end=" ")

n = int(input("Enter the number:"))
print_zigzag(n)
