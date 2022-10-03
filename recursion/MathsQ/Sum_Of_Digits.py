number=int(input("Enter the number: "))
to_String=str(number)
summation=0
for n in range(len(to_String)):
    summation=summation+int(to_String[n])
print(summation)
