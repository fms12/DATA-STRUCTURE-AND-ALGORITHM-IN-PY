def power_logarithmic(x, n):
    if n == 0:
        return 1
    power = power_logarithmic(x, n//2)
    if n % 2 == 0:
        return power * power
    else:
        return x * power * power

x = int(input("Enter the  number:"))
n = int(input("Enter the power:"))
print(power_logarithmic(x, n))

