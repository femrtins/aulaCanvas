from utils.glut_utils import *

class Canvas:
    def __init__(self, left, right, bottom, top):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top
        self.geometries = [] 
        self.temp_geometry = None
        self.other_temp_geometry = None
        self.selection_box = None
        
        self.buttons = []
        self.mouse_pressed = False
        self.start_mouse_pos = None
    
    def configure_visualization(self, width=800, height=800):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        # Ajustar o aspect ratio
        # aspect = width / float(height)
        # if aspect >= 1:
        #     glOrtho(self.left * aspect, self.right * aspect, self.bottom, self.top, -100.0, 100.0)
        # else:
        #     glOrtho(self.left, self.right, self.bottom / aspect, self.top / aspect, -100.0, 100.0)
        
        glOrtho(self.left, self.right, self.bottom, self.top, -100.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


    def onReshape(self, width, height):
        return self.configure_visualization(width, height)


    def showScreen(self, width, height):
        """
        Função de desenho principal
        
        """
        # limpa cor e profundidade
        glClearColor(1, 1, 1, 1.0)  # Define a cor de fundo
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.configure_visualization(width, height)    
        
        if self.temp_geometry != None:
            self.temp_geometry.draw_open()
        if self.other_temp_geometry != None:
            self.other_temp_geometry.draw_open() 
        if self.selection_box != None:
            self.selection_box.draw()
            
            
        if hasattr(self, "selection_tool") and self.selection_tool.selected_geometry:
            self.selection_tool.draw_bounding_box()
        
        # desenha todas as geometrias
        for geometry in self.geometries:
            geometry.draw()
        
        
                    
        glutSwapBuffers()

    def addGeometry(self, geometry):
        self.geometries.append(geometry)
        
    def addButton(self, button):
        self.buttons.append(button)