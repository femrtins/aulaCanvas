from utils.glut_utils import *
from geometry.geometry import Geometry

class Polyline(Geometry):
    def __init__(self, color, points):
        super().__init__(points[0][0], points[0][1], color)
        self.points = points
        
    def draw(self):
        cx, cy = self.x0, self.y0
        glPushMatrix()
        glTranslatef(cx, cy, 0)
        glRotatef(self.angle, 0, 0, 1)
        

        glColor3f(*self.color)
        glDisable(GL_LINE_STIPPLE)
        glBegin(GL_LINE_LOOP)
        for (x, y) in self.points:
            glVertex2f(x - cx, y - cy)
        glEnd()
        
        glPopMatrix()

    def draw_open(self):
        glLineStipple(5, 0xAAAA)
        glEnable(GL_LINE_STIPPLE)
        glBegin(GL_LINE_STRIP)
        glColor3f(1,0,1)
        for (x, y) in self.points:
            glVertex2f(x, y)
        glEnd()

class Line(Geometry):
    def __init__(self, x0, y0, x1, y1):
        super().__init__(x0, y0, (1,0,1))
        self.x1 = x1
        self.y1 = y1
        
    def draw(self):

        glColor3f(*self.color)
        glBegin(GL_LINES)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x1, self.y1)
        glEnd()
    
    def draw_open(self):
        glLineStipple(5, 0xAAAA)
        glEnable(GL_LINE_STIPPLE)
        glColor3f(1,0,1)
        glBegin(GL_LINES)
        glVertex2f(self.x0, self.y0)
        glVertex2f(self.x1, self.y1)
        glEnd()