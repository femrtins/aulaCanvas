from utils.glut_utils import *

class Color:
    def __init__(self, x, y):
        self.height = 5
        self.widht = 50
        self.r = Selector(x, y+ self.height * 2, self.height,  self.widht , (1.0, 0.0, 0.0))
        self.g = Selector(x, y+ self.height, self.height,  self.widht , (0.0, 1.0, 0.0))
        self.b = Selector(x, y, self.height,  self.widht , (0.0, 0.0, 1.0))
    
    def draw(self):
        self.r.draw()
        self.g.draw()
        self.b.draw()
        
    def inside(self, x, y):
        if self.r.contains(x, y):
            return self.r
        if self.g.contains(x, y):
            return self.g
        if self.b.contains(x, y):
            return self.b
        return None


    def calculate_color(self):
        red = self.r.picker.calculateColor()
        green = self.g.picker.calculateColor()
        blue = self.b.picker.calculateColor()
        return (red, green, blue)

class Selector:
    def __init__(self, x0, y0,  heigth, width, color):
        self.x0 = x0
        self.y0 = y0
        self.height = heigth
        self.width = width
        self.color = color
        self.selected = False
        self.picker = Picker(x0, y0, 50, heigth)

    def draw(self):
        
        glColor3f(0.5,0.5,0.5) 
        glLineWidth(2)
        
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x0 + self.width, self.y0)
        glVertex2f(self.x0 + self.width, self.y0 + self.height)
        glVertex2f(self.x0, self.y0 + self.height)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x0, self.y0 + self.height)

        glColor3fv(self.color)
        glVertex2f(self.x0 + self.width, self.y0 + self.height)
        glVertex2f(self.x0 + self.width, self.y0)
        glEnd()
        self.picker.draw()
        
    def contains(self, x, y):
        if y >= self.y0 and y <= self.y0 + self.height: 
            if x >= self.x0 and x <= self.x0 + self.width:
                return True 
        return False
        
class Picker:
    def __init__(self, x0, y0, width, height):
        self.selected = None
        self.x0 = x0
        self.y0 = y0
        self.height = height
        self.width = width
        self.selectorWidthMin = self.x0
        self.selectorWidthMax = self.x0 + width
        self.color = (1.0, 1.0, 1.0)
    
    def draw(self):
  
        glColor3f(0.5, 0.5, 0.5) 
        glLineWidth(3)
        
        # glBegin(GL_TRIANGLES)
        # glVertex2f(self.x0 - self.width, self.y0 + self.height + 5)
        # glVertex2f(self.x0 + self.width, self.y0 + self.height + 5)
        # glVertex2f(self.x0, self.y0 + self.height)
        # glEnd()
        
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x0, self.y0 + self.height)
        glEnd()
        
        
    def move(self, x):
        self.x0 = x
        if self.x0 < self.selectorWidthMin:
            self.x0 = self.selectorWidthMin
        if self.x0 > self.selectorWidthMax:
            self.x0 = self.selectorWidthMax
    
    def calculateColor(self):
 

        cor = (self.x0 - self.selectorWidthMin) / (self.selectorWidthMax - self.selectorWidthMin)
        return cor
    
class Button:
    def __init__(self, x0, y0,width,height):
        self.x0 = x0
        self.y0 = y0
        self.width = width 
        self.height = height
    
    def draw(self):
        glColor3f(0.5,0.5,0.5) 
        glLineWidth(2)
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x0 + self.width, self.y0)
        glVertex2f(self.x0 + self.width, self.y0 + self.height)
        glVertex2f(self.x0, self.y0 + self.height)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.5,0.5,0.5)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x0 + self.width, self.y0)
        glVertex2f(self.x0 + self.width, self.y0 + self.height)
        glVertex2f(self.x0, self.y0 + self.height)
        glEnd()
    
    def isClicked(self, mouse_x, mouse_y):
        if mouse_y < self.y0 + self.height and mouse_y > self.y0:
            if mouse_x > self.x0 and mouse_x < self.x0 + self.width:
                return True
        return False