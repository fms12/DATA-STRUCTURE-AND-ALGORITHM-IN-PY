#Program for finding the path using tower_of_hanoi
def tower_of_hanoi(n, source, target, aux):
    if n == 1: #base case
        print("Move disk 1 from source", source, "to target", target) #prints the path to the target disk which starts from disk 1
        return
    tower_of_hanoi(n-1, source, aux, target) #recursive call
    print("Move disk", n, "from source", source, "to target", target) #prints the path to the target disk which starts form disk n
    tower_of_hanoi(n-1, aux, target, source) #recursive call

n = int(input("Enter the number of disks:")) #Taking input form user
tower_of_hanoi(n, 'A', 'B', 'C') #calling the function