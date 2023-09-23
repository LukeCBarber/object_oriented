class Rectangle:
    
    #constructor
    def __init__(self, width, length, xpos, ypos):
        
        self.width = width
        self.length = length
        self.xpos = xpos
        self.ypos = ypos

    def get_coordinates(self):
        self.coordinates = '(' + str(self.xpos) +','+str(self.ypos)+ ')'
        print('- Coordinates:', self.coordinates)
        

    def get_area(self):
        self.area = self.length*self.width
        print('- Area:',self.area)
        

    def get_perimeter(self):
        self.peri = 2*self.length+2*self.width
        print('- Perimeter:',self.peri)

def main():

    rectangle1 = Rectangle(10,15,5,3)
    print("Rectangle #1")
    rectangle1.get_coordinates()
    rectangle1.get_area()
    rectangle1.get_perimeter()
    print()

    rectangle2 = Rectangle(3,5,15,7)
    print("Rectangle #2")
    rectangle2.get_coordinates()
    rectangle2.get_area()
    rectangle2.get_perimeter()
    print()
        
        

main()


