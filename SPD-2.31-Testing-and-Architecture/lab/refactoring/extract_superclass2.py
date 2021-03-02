# by Kami Bigdely
# Extract superclass.
class Shape:
    def __init__(self, x, y, visible=True):
        self.x = x
        self.y = y
        self.visible = visible
    
    def display(self, message):
        print(message)

    def set_visible(self, is_visible):
        self.visible = is_visible
    
    def get_center(self):
        self.x, self.y

class Circle(Shape):
    
    def __init__(self, center_x, center_y, r, visible = True):
        super().__init__(center_x, center_y, visible)
        self.r = r
      
    def display(self):
        print('drew the circle.')
    
class Rectangle(Shape):
    
    def __init__(self, x, y, width, height, visible = True):
        # left-bottom corner.
        super().__init__(x, y, visible)
        self.width = width
        self.height = height

    def display(self):
        if self.visible:
            super().display("drew the rectangle.")
            
    def hide(self):
        super().set_visible(False)
        
    def make_visible(self):
        super().set_visible(True)
        
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 


if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visible(True)
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point',rect.get_center())