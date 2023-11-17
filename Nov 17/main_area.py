from graphics import rectangle
from graphics import circle
from graphics.Sub_graphics import cuboid
from graphics.Sub_graphics import sphere





l = int(input("Enter the length of rectangle:"))
print("\n")

b = int(input("Enter the breadth of rectangle:"))
print("\n")


print("Area of rectangle =", rectangle.area_rectangle(l,b))
print("\n")

print("Perimeter of rectangle =", rectangle.perimeter_rectangle(l,b))
print("\n")

r = int(input("Enter the radius of circle:"))
print("\n")


print("Cirumference of circle =", circle.circumference_circle(r))
print("\n")

print("Perimeter of circle =", circle.perimeter_circle(r))
print("\n")



l = int(input("Enter the length of cuboid:"))
print("\n")

b = int(input("Enter the breadth of cuboid:"))
print("\n")

h = int(input("Enter the height of cuboid:"))
print("\n")


print("Area of cuboid =", cuboid.area_cuboid(l,b,h))
print("\n")

print("Perimeter of cuboid =", cuboid.perimeter_cuboid(l,b,h))
print("\n")


r = int(input("Enter the radius of sphere:"))
print("\n")


print("Surface area of sphere =", sphere.area_sphere(r))
print("\n")

print("Volume of sphere =", sphere.volume_sphere(r))
