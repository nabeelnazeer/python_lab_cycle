#function to read the number
def read_num(num):
    print("the entered number is ",num)

#function to check happy number
def check(num):
    sum = 0
    for i in range(0,100):
        while num != 0:
            r = num % 10
            sum = sum + r*r
            num = num // 10
        if sum == 1:
            return 1
        else:
            num = sum
            sum = 0
    return 0

#function to find happy numbers in a range
def happy(m,n):
    happy_numbers = []
    for i in range(m, n+1):
        if check(i) == 1:
            happy_numbers.append(i)
    return happy_numbers

#calling
num = int(input("enter the number: "))
read_num(num)
result = check(num)
if result == 1:
    print("happy number")
else:
    print("sad number")
    
m = int(input("enter the lower limit: "))
n = int(input("enter the upper limit: "))
h_num1 = happy(m, n)
print(h_num1)
