# Write a Rectangle class, allowing you to build a rectangle with length and width attributes.
# Create a perimeter() method to calculate the perimeter of the rectangle and an area() 
# method to calculate the area of ​​the rectangle.
# Create a method display() that displays the length, width, perimeter and area of an object 
# created using an instantiation on Rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and 
# with a height attribute and another volume() method to calculate the volume of the Parallelepiped.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def rectangle_perimeter(self):
        return (self.length+self.width)*2

    def rectangle_area(self):
        return self.length*self.width

    def display(self):
        print('Length is',self.length)
        print('Width is',self.width)
        print('Area is',self.rectangle_area())
        print('Perimeter is',self.rectangle_perimeter())
        
class Parallelepipede(Rectangle):
    def __init__(self,length,width,heigth):
        super().__init__(length, width)
        self.heigth = heigth

    def volume_parallelepipede(self):
        return self.length*self.width*self.heigth

newRectangle = Rectangle(12, 10)
Rectangle.display(newRectangle)
newParallelepipede = Parallelepipede(12,10,5)
print('Volume is',newParallelepipede.volume_parallelepipede())