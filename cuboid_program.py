import three_d_figures

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Curved Surface Area:", three_d_figures.cuboid_curved_surface_area(l, b, h))
print("Total Surface Area:", three_d_figures.cuboid_total_surface_area(l, b, h))
print("Volume:", three_d_figures.cuboid_volume(l, b, h))
