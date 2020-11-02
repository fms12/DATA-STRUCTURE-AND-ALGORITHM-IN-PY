dict={}
str=intput("enter the string"):
for i in str:
  if i in dict:
    dict[i]+=1
  else:
    dict[i]=1
for key,value in dict.item():
  print(key,value)
  
