def tower_of_hanoi(n, source, target, aux):
    if n == 1:
        print("Move disk 1 from source", source, "to target", target)
        return
    tower_of_hanoi(n-1, source, aux, target)
    print("Move disk", n, "from source", source, "to target", target)
    tower_of_hanoi(n-1, aux, target, source)

n = int(input("Enter the number of disks:"))
tower_of_hanoi(n, 'A', 'B', 'C')