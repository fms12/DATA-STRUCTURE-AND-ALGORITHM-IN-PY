# hint think about the binary no 

def subset(arr):
    subst=pow(2,len(arr)) # here to the power of the array because all these are 2power n form so it times to run the loop 
    for i in range(subst):
            dec=i
            s=[]
            for j in range(len(arr)):
                r = dec % 2  # it's binary form first do the module and get the reminder 
                dec = dec // 2  # here short the no so it is divided by the two
                if( r== 0):
                    s.append("-")
                else:
                    s.append(arr[len(arr) - 1 - j]) # here reverse the array 
            s.reverse()  # here we reverse the array to get original output
            print("\t".join(map(str,s)))
            
        
n=int(input())    
arr=[]
for i in range(n):
    arr.append(int(input()))

subset(arr)

# ////////////////////////////////////////..................................... OUTPUT............................///////////////////////////////////////////////

-	-	-
-	-	30
-	20	-
-	20	30
10	-	-
10	-	30
10	20	-
10	20	30
