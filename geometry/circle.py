from utils.glut_utils import *
from geometry.geometry import Geometry
import math

class Circle(Geometry):
    def __init__(self, x0, y0, radius, color):
        super().__init__(x0, y0, color)
        self.radius = radius
        self.type = "Circ"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def reescale(self, factor):
        radius = radius * factor
    
    
    def draw(self):
        glPushMatrix()
        
        glTranslatef(self.x0, self.y0, 0)
        glRotatef(self.angle, 0, 0, 1)
        
        glLineWidth(1)
        glDisable(GL_LINE_STIPPLE)
        glBegin(GL_LINE_LOOP)   
        glColor3f(*self.color)
        for i in range(0,360):
            px = math.cos(i * math.pi/180) * self.radius
            py = math.sin(i * math.pi/180) * self.radius 
            glVertex2f(px,py)
        glEnd()
        
        glPopMatrix()
        
    def draw_open(self):
        glLineStipple(5, 0xAAAA)
        glEnable(GL_LINE_STIPPLE)
        glBegin(GL_LINE_LOOP)  
        glColor3f(1,0,1)
        for i in range(0,360):
            px = self.x0 + math.cos(i * math.pi/180) * self.radius
            py = self.y0 + math.sin(i * math.pi/180) * self.radius 
            glVertex2f(px,py)
        glEnd()
        
    def contains_point(self, x, y):
        
        radius = self.radius ** 2
        if (self.x0 - x) ** 2 + (self.y0 - y) ** 2 <= radius:
            # self.is_selected = True
            return True
        # self.is_selected = False
        return False
    
    
    
             