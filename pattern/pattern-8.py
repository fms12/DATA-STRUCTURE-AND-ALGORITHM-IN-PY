# Pyramid pattern

#     1
#    123
#   12345
#  1234567
# 123456789

n = int(input("Enter value : "))
for i in range(n):
    # Two internal loops - one will create spaces
    for j in range(n - i - 1):
        print(' ', end='')
    # This one will print numbers in the format of 2n + 1
    # As the pattern has odd number in each row
    for k in range(2 * i + 1):
        print(k + 1, end='')
    print()
