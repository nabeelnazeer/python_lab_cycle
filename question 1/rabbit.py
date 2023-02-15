n=int (input("enter months : "))
a=0
b=1
print("months"+"           "+"rabbits")
print(" ",b,"            ",b)
for i in range(2,n+1):
  c=a+b
  a=b
  b=c
  print(" ",i,"            ",c)