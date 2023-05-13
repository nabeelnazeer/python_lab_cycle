#function for checking whether four digit or not
def valid(num):
  i=0
  while num!=0:
    r=num%10
    i=i+1
    num=num//10
  return (i)
#function for finding sum of digits
def add_digits(digits):
  sum=0
  while digits!=0:
    rem=digits%10
    sum=sum+rem
    digits= digits//10
  return (sum)
#function for reversing digits  
def rverse_digits(digits):
  rev=0
  while digits!=0:
    rem=digits%10
    rev=rev*10+rem
    digits=digits//10
  return (rev)
#function for finding difference 
def difference(digits):
  even=1
  odd=1
  while digits>0:
    rem=digits%10
    #to get last digit
    odd=odd*rem
    digits=digits//10
    rem=digits%10
    #to get second digit
    even=even*rem
    digits=digits//10
  diff= even-odd
  return(diff)
#inputing number from user
n= int(input("enter a number = "))
i=valid(n)
#taking sum of the four digits
sum=0
if i==4:
  sum= add_digits(n)
  print("sum of digits = ", sum)
else:
  print("invalid input please try again")
#reversing the digits
if i==4:
  rev= rverse_digits(n)
  print("reverse of number entered = ", rev)
#getting the difference
if i==4:
  diff= difference(n)
  print("difference  = ", diff)



