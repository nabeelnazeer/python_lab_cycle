#function to rea three sides of triangle
def read_sides(side_1, side_2, side_3):
  print("side 1 = ",side_1," ","side 2 = ",side_2," ","side_3 = ",side_3)
#function to find the areas of triangle
def area_of(x,y,z):
  import math
  sum= x+y+z
  s= sum/2
  d=s*(s-x)*(s-y)*(s-z)
  area= math.sqrt(d)
  return (area)
#function to print total area enclosed
def total_area(t1,t2):
  total_area= t1+t2
  print("the total area enclosed by the triangles = ", total_area)
#function to find percentage of area enclosed of each tringle
def percentage_of(m,q,w):
  total=q+w
  ratio=m/total
  per=ratio*100
  return (round(per, 2)) 

#inputing sides of two triangle
print("sides of triangle 1 :")
p= int (input("enter side 1 = "))
q= int (input("enter side 2 = "))
r= int (input("enter side 3 = "))
read_sides(p, q, r)
a= int (input("enter side 1 = "))
b= int (input("enter side 2 = "))
c= int (input("enter side 3 = "))
print("sides of triangle 2 : ")
read_sides(a, b, c)
#finding area of the two triangles
area_1=area_of(p, q, r)
print("area of triangle 1 = ", area_1)
area_2=area_of(a, b, c)
print("area of triangle 2 = ", area_2)
#total area
total_area(area_1, area_2)
#percentage
p1=percentage_of(area_1, area_1,area_2)
print("percentage enclosed by triangle 1 = ", p1,"%")
p2= percentage_of(area_2,area_1,area_2)
print("percentage enclosed by triangle 2 = ", p2,"%")

