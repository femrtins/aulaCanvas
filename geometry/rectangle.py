from utils.glut_utils import *
from geometry.geometry import Geometry

class Rectangle(Geometry):
    def __init__(self, x0, y0, height, width, color):
        super().__init__(x0, y0, color)
        self.height = height
        self.width = width 
        self.type = "Rec"
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return self.height*2 + self.width*2
       
    def draw(self):
        cx = self.x0 + self.width / 2.0
        cy = self.y0 + self.height / 2.0
        
        w_half = self.width / 2.0
        h_half = self.height / 2.0

        glPushMatrix()  
        
        glTranslatef(cx, cy, 0)
        glRotatef(self.angle, 0, 0, 1) 
        glDisable(GL_LINE_STIPPLE)
        glBegin(GL_LINE_LOOP) 
        glColor3f(*self.color)
        glVertex2f(-w_half, -h_half) 
        glVertex2f( w_half, -h_half) 
        glVertex2f( w_half,  h_half) 
        glVertex2f(-w_half,  h_half) 
        glEnd()
        
        glPopMatrix()
        
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
        glDisable(GL_LINE_STIPPLE)
         
    def contains_point(self, x, y):
        x_min = min(self.x0, self.x0 + self.width)
        x_max = max(self.x0, self.x0 + self.width)
        
        y_min = min(self.y0, self.y0 + self.height)
        y_max = max(self.y0, self.y0 + self.height)

        return (x_min <= x <= x_max) and (y_min <= y <= y_max)