import math
#parent class having methods PrintArea and PrintVolume
class ThreeDShapes:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    #method to print area based on type of bject calling the method    
    def PrintArea(self):
        if isinstance(self, cylinder):
            self.lateralarea =  2*math.pi*self.radius*self.height
            self.basearea = math.pi*self.radius**2
            self.totalarea = 2*self.basearea + self.lateralarea
            print("lateral area = ", round(self.lateralarea, 2))
            print("base area = ", round(self.basearea, 2))
            print("total area = ", round(self.totalarea, 2))
        elif isinstance(self, sphere):
            self.surfacearea = 4*math.pi*self.radius**2
            print("surface area of sphere is : ",round(self.surfacearea, 2))



    #method to print volume based on type   
    def PrintVlolume(self):
        if isinstance(self, cylinder):
            self.volume = math.pi*self.radius**2*self.height
            print("the volume of the cylinder is : ", round(self.volume, 2))

        if isinstance(self, sphere):
            n = 4/3
            self.volume = n*math.pi*self.radius**3
            print("the volume of sphere is : ", round(self.volume, 2))    
           
class cylinder(ThreeDShapes):
    def __init__(self, radius, height):
        super().__init__(radius,height)

class sphere(ThreeDShapes):
    def __init__(self, radius, height):
        super().__init__(radius, height)
#inputs from the user
cyl_radius = float(input("enter the radius for cylinder : "))
cyl_height = float(input("enter the height for the cylinder : "))

obj1 = cylinder(cyl_radius,cyl_height)
obj1.PrintArea()
obj1.PrintVlolume()
sph_radius = float(input("enter the radius for sphere : "))
obj2 = sphere(sph_radius,0)
obj2.PrintArea()
obj2.PrintVlolume()        




