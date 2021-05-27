class Rectangle():
    width = 0
    height = 0
    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)
    def set_width(self, width):
        self.width = width
        #also adjusts height if it's a square
        if self.__class__.__name__ == 'Square':
            self.height = width
    def set_height(self, height):
        self.height = height
        if self.__class__.__name__ == 'Square':
            self.width = height
    def get_area(self):
        return(self.width*self.height)
    def get_perimeter(self):
        return(2 * (self.width + self.height))
    def get_diagonal(self):
        return((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return('Too big for picture.')
        return(('*'*self.width+'\n')*self.height)
    #checks the amount of times shape fits in self over width and height
    def get_amount_inside(self, shape):
        divideWide = int(self.width / shape.width)
        divideHigh = int(self.height / shape.height)
        if divideWide >= 1 and divideHigh >= 1:
            return(divideHigh*divideWide)
        else:
            return(0)
    def __str__(self):
        return(f'Rectangle(width={self.width}, height={self.height})')

class Square(Rectangle):
    def __init__(self, side):
      self.set_side(side)
    def set_side(self, side):
      #because set_width already automatically sets side for Square objects we only need to set the width
      self.set_width(side)
    def __str__(self):
        return(f'Square(side={self.height})')