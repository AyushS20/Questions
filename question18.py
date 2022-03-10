class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2 * (self.length + self.breadth)
a = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))

obj = rectangle(a, b)
print("Area of rectangle:", obj.area(), "square units.")
print("Perimeter of Rectangle:", obj.perimeter(), "units.")
 
print()
