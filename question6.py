# Defining Shape-Wise Areas
def square():
    x1 = float(input("Enter Length of Side:    "))
    area1 = round(x1 * x1, 2)
    print("Area of Square Land is", area1, "square units.")
def circle():
    import math
    r1 = float(input("Enter Radius:   "))
    area2 = round(r1 * r1 * math.pi, 2)
    print("Area of Circular Land is", area2, "square units.")
def rectangle():
    l1 = float(input("Enter Length:   "))
    b1 = float(input("Enter Breadth:  "))
    area3 = round(l1 * b1, 2)
    print("Area of rectangular Land is", area3, "square units.")
def triangle():
    a2 = float(input("Enter side 1:   "))
    b2 = float(input("Enter side 2:   "))
    c2 = float(input("Enter side 3:   "))
    s2 = (a2 + b2 + c2) / 2
    x = s2 - a2
    y = s2 - b2
    z = s2 - c2
    area4 = round((s2 * x * y * z) ** 1/2, 2)
    print("Area of triangular Land is", area4, "square units.")

print("""Choose Ground Shape of Building \n 1. Square \n 2. Circle \n 3. Rectangle \n 4. Triangle""")
opt = int(input("(1, 2, 3, 4):  "))
if opt == 1:
    square()
elif opt == 2:
    circle()
elif opt == 3:
    rectangle()
elif opt == 4:
    triangle()
else:
    print("Try Again :)")
