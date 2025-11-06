import time
from utils.glut_utils import *
from utils.world_coordinates import getWorldCoords
from geometry.rectangle import Rectangle
from geometry.circle import Circle
from utils.drawing_tool import DrawingTool
from utils.selection_tool import SelectionTool
from utils.transformation_tools import TransformationTools
import math

last_click_time = 0
double_click_threshold = 0.3

class InputHandler:
    def __init__(self, canvas):
        self.canvas = canvas
        self.mouse_down = False
        self.state = None
        self.drawing_tool = DrawingTool()  
        self.selection_mode = False
        self.selection_tool = SelectionTool(canvas) 
        self.geometry_selected = None
        self.transformation_tool = TransformationTools(canvas)
        self.transform_mode = None
            
    def onKeyboard(self, key, x , y) -> None:
        if key == b'\x1b':  # ESC
            try:
                glutLeaveMainLoop()  # Funciona no FreeGLUT
            except Exception:
                os._exit(0)  # Saída imediata se glutLeaveMainLoop não existir
        
        if key.lower() == b'r':
            self.drawing_tool.shape = "rectangle"
            
        if key.lower() == b'c':
            self.drawing_tool.shape = "circle"
        
        if key.lower() == b'p':  
            self.drawing_tool.shape = "polyline"
            
        if key.lower() == b't':
            self.transform_mode = 'translate'
        
        if key.lower() == b'e':
            self.transform_mode = 'scale'
    

        if key.lower() == b's':
            if self.selection_mode == True:
                self.selection_mode = False
                self.selection_tool.deselect_geometry()
            else:
                self.drawing_tool.shape = None   
                self.selection_mode = True    
                
    

    def onMouse(self, button, state, mouse_x, mouse_y):
        
        global last_click_time
        global double_click_threshold
        
                         
        if button == GLUT_LEFT_BUTTON:
            x, y = getWorldCoords(mouse_x, mouse_y, self.canvas)
            now = time.time()
            
            if state == GLUT_DOWN:
                
                if self.selection_mode:
                    self.selection_tool.select_geometry(x, y)
                    selected = self.selection_tool.get_selected_object()
                    if selected:
                        self.transformation_tool.start_transform(selected, x, y)
                                             
                # If double click ends the geometry
                elif now - last_click_time < double_click_threshold:
                    if self.drawing_tool.shape == "polyline":
                        geometry = self.drawing_tool.finish(x, y)
                        if geometry:
                            self.canvas.addGeometry(geometry)
                        self.canvas.temp_geometry = None
                        self.drawing_tool.shape = None
                        self.canvas.other_temp_geometry = None
                        self.drawing_tool.started = False
                        self.drawing_tool.points = []
                        glutPostRedisplay()
                               
                else:
                # If normal click starts the geometry
                    self.mouse_down = True
                    self.drawing_tool.started = True
                    self.drawing_tool.start(x, y)
                
            # Ends geometry on mouse up (rectangle and circle)
            elif state == GLUT_UP and self.drawing_tool.shape:
                
                if self.transform_mode:
                    self.transformation_tool.start_x = None
                    self.transformation_tool.start_y = None
                
                self.mouse_down = False
                geometry = self.drawing_tool.finish(x, y)
                
                if geometry:
                    if self.drawing_tool.shape == "polyline":
                        self.canvas.other_temp_geometry = geometry
                    else:
                        self.canvas.addGeometry(geometry)
                self.canvas.temp_geometry = None              
                
            last_click_time = now
        
    def onMotion(self, mouse_x, mouse_y):
        x, y = getWorldCoords(mouse_x, mouse_y, self.canvas)
        
        if self.transform_mode and self.transformation_tool.selected_geometry:
            if self.transform_mode == 'translate':
                self.transformation_tool.translate(x, y)
            elif self.transform_mode == 'scale':
                self.transformation_tool.scale(x, y)
            glutPostRedisplay()
        
        if self.mouse_down and self.drawing_tool.shape and self.drawing_tool.shape != "polyline":
            geometry = self.drawing_tool.finish(x, y)
            self.canvas.temp_geometry = geometry 
            glutPostRedisplay()
        
        # It is drawing like a pencil
        
        # if self.mouse_down and self.drawing_tool.shape == "polyline":
        #     x, y = getWorldCoords(mouse_x, mouse_y, self.canvas)
        #     self.drawing_tool.add_point(x, y)
        #     geometry = self.drawing_tool.finish(x, y)
        #     self.canvas.temp_geometry = geometry 
        #     glutPostRedisplay()
                
        
    def onPassiveMotion(self, mouse_x, mouse_y):
        
        if self.drawing_tool.shape == "polyline" and self.drawing_tool.started:
            x, y = getWorldCoords(mouse_x, mouse_y, self.canvas)
            geometry = self.drawing_tool.make_line(x, y)
            self.canvas.temp_geometry = geometry 
            glutPostRedisplay()


            
            
            
            
            
            
        
        
        