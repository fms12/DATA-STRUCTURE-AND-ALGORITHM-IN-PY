# Program for finding the path using tower_of_hanoi
def tower_of_hanoi(n, source, target, aux):
    if n == 1:  # base case
        # prints the path to the target disk which starts from disk 1
        print("Move disk 1 from source", source, "to target", target)
        return
    tower_of_hanoi(n-1, source, aux, target)  # recursive call

    # prints the path to the target disk which starts form disk n
    print("Move disk", n, "from source", source, "to target", target)
    tower_of_hanoi(n-1, aux, target, source)  # recursive call


n = int(input("Enter the number of disks:"))  # Taking input form user
tower_of_hanoi(n, 'A', 'B', 'C')  # calling the function
