#volume of cone ny lamba function.
import math
volume=lambda r,h: (1/3)*math.pi*r**2*h
r=float(input("enter radius: "))
h=float(input("enter height: "))
print("volume of cone: ",volume(r,h))