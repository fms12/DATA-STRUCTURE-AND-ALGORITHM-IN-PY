count=0
# initializing count with zero
def count_digit(num):
    global count
    if (num >0):
        if(num%10==0):
            count +=1
        count_digit(num // 10)
    return count
n=int(input("Enter a number:"))
# taking input
print("The number of Zeros in the Given number is:",count_digit(n))
