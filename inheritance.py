from curses.textpad import rectangle


class Rectangle:
    def __init__(self,base, high):
        self.base =base 
        self.high =high

    def area(self):
        return self.base * self.high

class Square(Rectangle):
     
     def __init__(self, side):
         super().__init__(side,side)

if __name__=='__main__':
    rectangle=Rectangle(base=3,high=4)
    print(rectangle.area())

    square=Square(side=5)
    print(square.area())