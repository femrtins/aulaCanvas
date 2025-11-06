from utils.glut_utils import *
from geometry.geometry import Geometry

class Rectangle(Geometry):
    def __init__(self, x0, y0, height, width, color):
        super().__init__(x0, y0, color)
        self.height = height
        self.width = width 
        self.type = "Rec"
       
    def draw(self):
        glBegin(GL_QUADS)
        glColor3f(*self.color)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x0 + self.width, self.y0)
        glVertex2f(self.x0 + self.width, self.y0 + self.height)
        glVertex2f(self.x0, self.y0 + self.height)
        glEnd()
        
    def draw_open(self):
        glLineStipple(5, 0xAAAA)
        glEnable(GL_LINE_STIPPLE)
        glColor3f(1,0,1)
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x0 + self.width, self.y0)
        glVertex2f(self.x0 + self.width, self.y0 + self.height)
        glVertex2f(self.x0, self.y0 + self.height)
        glEnd()
         
    def contains_point(self, x, y):
        pass