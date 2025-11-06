from utils.glut_utils import *

class SelectionTool:

    def __init__(self, canvas):
        self.canvas = canvas
        self.selected_geometry = None

    def get_selected_object(self):
        return self.selected_geometry

    def select_geometry(self, x, y):
        for geometry in self.canvas.geometries:
            if geometry.contains_point(x, y):
                self.selected_geometry = geometry
                break 

        if self.selected_geometry:
            selection_Box = SelectionBox(self.selected_geometry)
            self.canvas.selection_box = selection_Box
        else:
            print("No geometry selected.")
            
    def deselect_geometry(self):
        self.selected_geometry = None
        self.canvas.selection_box = None

            
class SelectionBox:
    def __init__(self, geometry):
        self.geometry = geometry

    def draw(self):

        x0 = self.geometry.x0
        y0 = self.geometry.y0

        if self.geometry.type == "Rec":
            width = self.geometry.width
            height = self.geometry.height
        elif self.geometry.type == "Circ":
            width = height = self.geometry.radius * 2
            x0 -= self.geometry.radius
            y0 -= self.geometry.radius
        else:
            return

        glLineStipple(5, 0xAAAA)
        glEnable(GL_LINE_STIPPLE)
        glColor3f(0, 0, 0.51)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x0, y0)
        glVertex2f(x0 + width, y0)
        glVertex2f(x0 + width, y0 + height)
        glVertex2f(x0, y0 + height)
        glEnd()
        glDisable(GL_LINE_STIPPLE)
        
        glBegin(GL_QUADS)
        glVertex2f(x0-1, y0-1)
        glVertex2f(x0+1, y0-1)
        glVertex2f(x0+1, y0+1)
        glVertex2f(x0-1, y0+1)
        glEnd()
        
        glBegin(GL_QUADS)
        glVertex2f(x0 + width - 1, y0 -1)
        glVertex2f(x0 + width +1, y0-1) 
        glVertex2f(x0 + width +1, y0 +1)
        glVertex2f(x0 + width -1 , y0 +1)
        glEnd()
        
        glBegin(GL_QUADS)
        glVertex2f(x0 + width - 1, y0 + height - 1)
        glVertex2f(x0 + width +1, y0 + height -1 )
        glVertex2f(x0 + width +1, y0 + height +1)
        glVertex2f(x0 + width - 1, y0 + height +1)
        glEnd()
        
