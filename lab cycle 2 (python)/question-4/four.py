
import random

class Box:
  def __init__(b,*arg):
    if len(arg) == 1:
      b.Length_ = arg[0]
      b.Breadth_ = arg[0]
      b.Height_ = arg[0]
    elif len(arg) == 2:
      b.Length_ = arg[0]
      b.Breadth_ = arg[0]
      b.Height_ = arg[1]
    else:
      b.Length_ = arg[0]
      b.Breadth_ = arg[1]
      b.Height_ = arg[2]
  def area(b):
    b.Area_ = b.Length_*b.Breadth_
    return b.Area_

  def volume(b):
    b.Volume_ = b.Length_*b.Breadth_*b.Height_
    return b.Volume_
  
  def areaDisplay(b):
    print("Area = ",b.Area_)
 
  def volumeDisplay(b):
    print("Volume =  ",b.Volume_,"\n")

ratio = []

cubeDimension = []
cubeDimension.append(random.randint(1,1000))
print("Cube Prism\nDimension" , end = " ")
print(cubeDimension)

cubePrism = Box(cubeDimension[0])
AreaC=cubePrism.area()
VolumeC=cubePrism.volume()
cubePrism.areaDisplay()
cubePrism.volumeDisplay()

ratio.append((VolumeC/AreaC))

squareDimension = []
for i in range(2):
  squareDimension.append(random.randint(1,1000))
print("Square Prism\nDimension" , end = " ")
print(squareDimension)

squarePrism = Box(squareDimension[0],squareDimension[1])
AreaS=squarePrism.area()
VolumeS=squarePrism.volume()
squarePrism.areaDisplay()
squarePrism.volumeDisplay()

ratio.append((VolumeS/AreaS))

recatangleDimension = []
for i in range(3):
  recatangleDimension.append(random.randint(1,1000))

print("Rectangular Prism\nDimension" , end = " ")
print(recatangleDimension)
recatanglePrism = Box(recatangleDimension[0],recatangleDimension[1],recatangleDimension[2])
AreaR =recatanglePrism.area()
VolumeR =recatanglePrism.volume()
recatanglePrism.areaDisplay()
recatanglePrism.volumeDisplay()

ratio.append((VolumeR/AreaR))
index = ratio.index(max(ratio))

if index == 0:
  print("Cube Prism has Maximum Volume : Area Ratio - ", end=" ")
  print(cubeDimension)
elif index == 1:
  print("Square Prism has Maximum Volume : Area Ratio  - " , end=" ")
  print(squareDimension)
else:
  print("Rectangular Prism has Maximum Volume : Area Ratio  - ", end=" ")
  print(recatangleDimension)