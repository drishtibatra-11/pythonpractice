#Write a lambda function to find volume of cone.
volume_of_cone = lambda r, h: (1/3) * 3.14159 * r**2 * h
height = float(input("Enter height of the cone: "))
radius = float(input("Enter radius of the cone: "))
print(volume_of_cone(radius, height))