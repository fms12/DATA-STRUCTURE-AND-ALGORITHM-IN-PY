number=int(input("Enter the number :"))
to_String=str(number)
count=0
for i,element in enumerate(to_String):
    if to_String[i] == "0":
        count=count+1
print(count)     
