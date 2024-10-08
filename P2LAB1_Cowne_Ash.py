# Ash Cowne
# 10/8/2024
# P2LAB1
# Get the radius from user then caculate the diameter, circumference, and area of a circle.

#Import math libary
import math

# Get radius from user.
radius = float(input("What is the radius of the circle? "));
print("")

# Caculations.
diameter = radius * 2
circumference = 2 * radius * math.pi
radius = math.pi * radius**2

# Display

print(f"Tfe diameter of the circle is {round(diameter,1)}\n)");
print(f"The circumference of the circle is {round(circumference,2)}\n");
print(f"The area of the circle is {round(radius,3)}");
