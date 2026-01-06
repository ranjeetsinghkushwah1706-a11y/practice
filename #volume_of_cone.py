#volume_of_cone

import math

r = float(input("Enter radius of the cone: "))
h = float(input("Enter height of the cone: "))

volume = (1/3) * math.pi * r * r * h

print("Volume of the cone =", volume)
