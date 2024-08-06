class Rectangle:
    def __init__(shape,length,width):
        shape.length = length
        shape.width = width
        
    def area(shape):
        area = shape.length * shape.width
        print (area)

r1 = Rectangle(17,12)
r2 = Rectangle(65,69)

print(r1.length)
r1.area()

r2.area()