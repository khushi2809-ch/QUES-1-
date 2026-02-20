import math
import three_d_figures

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

l = math.sqrt(r*r + h*h)   # slant height

print("Curved Surface Area:", three_d_figures.cone_curved_surface_area(r, l))
print("Total Surface Area:", three_d_figures.cone_total_surface_area(r, l))
print("Volume:", three_d_figures.cone_volume(r, h))