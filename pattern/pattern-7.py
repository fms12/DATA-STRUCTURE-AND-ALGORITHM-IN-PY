# Right triangle pattern

#     1
#    12
#   123
#  1234
# 12345

n = int(input("Enter value: "))
for i in range(n):
    #Two internal loops - first will create spaces
    for j in range(1, n - i):
        print(" ", end="")
        #second will print number
    for k in range(1, i + 2):
        print(k, end='')
    print()