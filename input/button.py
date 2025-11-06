from utils.glut_utils import *

class Button:
    def __init__(self, x, y, width, height, label, color=(0.7, 0.7, 0.7), callback=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.color = color
        self.callback = callback  # função a ser chamada ao clicar

    def draw(self):
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.width, self.y)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x, self.y + self.height)
        glEnd()

      
    def is_inside(self, px, py):
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height

    def click(self):
        if self.callback:
            self.callback()
