#FUNCTION FOR READING EMPLOYEE NAME
def name_of(name):
  print("Employee name = "+""*3,name)
#FUNCTION TO READ EMPLOYEE CODE
def code_of(code):
  print("code = "+""*3,code)
#FUNCTION TO PRINT BASIC PAY
def basic_print(bp):
  print("Basic pay :"+""*3,bp)
#FUNCTION TO CALACULATE GROSS SALARY
def gross_of(bp,da,hra,ma):
  
  gs= bp+da+hra+ma
  return (gs)
#FUNCTION TO FIND DEDUCTION
def deduct(pt,pf,it):
  d= pt+pf+it
  return (d)
#FUNCTION TO FIND THE NET SALARY
def net_salary(gs,d):
  net_salary= gs-d
  return (net_salary)
  #taking important inputs from the user 
name= str (input("enter name of employee  :  "))            
code= str (input("enter the employee code :  "))
#inputting the basic salary of employee
bp= int (input("enter the basic salary of the employee  :  "))
#conditional branching
if bp<10000:
  da=0.05*bp                                             
  hra=0.025*bp
  ma=500
  gs=gross_of(bp,da,hra,ma)
  pt=20
  pf=0.08*bp
  d= deduct(pt,pf,0)
  ns=net_salary(gs,d)
elif bp<30000:
  da=0.075*bp
  hra=0.05*bp
  ma=2500
  gs=gross_of(bp,da,hra,ma)
  pt=60
  pf=0.08*bp
  d= deduct(pt,pf,0)
  ns=net_salary(gs,d)
elif bp<50000:
  da=0.11*bp
  hra=0.075*bp
  ma=5000
  gs=gross_of(bp,da,hra,ma)
  pt=60
  pf=0.11*bp
  it=0.11*bp
  d= deduct(pt,pf,it)
  ns=net_salary(gs,d)
else:
  da=0.25*bp
  hra=0.11*bp
  ma=7000
  gs=gross_of(bp,da,hra,ma)
  pt=60
  pf=0.11*bp
  it=0.11*bp
  d= deduct(pt,pf,it)
  ns=net_salary(gs,d)
print("***************PAY SLIP*****************")
name_of(name)
code_of(code)
print("-----------payments/benefits-------------")
print("basic pay           :              ", bp)
print("gross pay           :              ", gs)
print("______________deductions_________________")
print("deduction           :              ",  d)
print("______________net salary_________________")
print("net salary          :              ", ns)