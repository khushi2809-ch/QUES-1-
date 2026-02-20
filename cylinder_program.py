import three_d_figures

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area:", three_d_figures.cylinder_curved_surface_area(r, h))
print("Total Surface Area:", three_d_figures.cylinder_total_surface_area(r, h))
print("Volume:", three_d_figures.cylinder_volume(r, h))