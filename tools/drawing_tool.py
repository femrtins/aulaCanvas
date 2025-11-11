import math
from utils.glut_utils import *
from geometry.circle import Circle
from geometry.rectangle import Rectangle
from geometry.polyline import Line, Polyline
from tools.tool import Tool 

class DrawingTool(Tool): 
    def __init__(self, canvas):
        super().__init__(canvas) 
        self.shape = None     
        self.color = (0,0,0)   
        self.start_x = None
        self.start_y = None
        self.started = False
        self.points = []

    def activate(self):
       
        self.started = False
        self.points = []
        self.canvas.temp_geometry = None
        self.canvas.other_temp_geometry = None
        if self.shape:
             print(f"Ferramenta de Desenho Ativa. Forma: {self.shape}")

    def deactivate(self):
        """Limpa ao trocar de ferramenta"""
        
        self.activate() 
        self.shape = None

    def onMouse(self, button, state, x, y, is_double_click=False):
        if button != GLUT_LEFT_BUTTON:
            return

        if self.shape == "polyline":
            self._handle_polyline_mouse(state, x, y, is_double_click)
        elif self.shape in ["rectangle", "circle"]:
            self._handle_simple_shape_mouse(state, x, y)
        
        glutPostRedisplay()

    def _handle_polyline_mouse(self, state, x, y, is_double_click):
        if state == GLUT_DOWN:
            if is_double_click:
                # Finaliza Polilinha com clique duplo
                if len(self.points) > 1:
                    # Finish adiciona o último ponto
                    geometry = self.finish(x, y) 
                    if geometry:
                        self.canvas.addGeometry(geometry)
                self.activate()
                print("Polilinha finalizada.")
                
            else:
                # Adiciona ponto
                if not self.started:
                    # Atart adiciona o primeiro ponto
                    self.start(x, y) 
                    # Atualiza geometria temporária
                    self.canvas.other_temp_geometry = Polyline(self.color, self.points)
                else:
                    self.add_point(x, y)
                    self.canvas.other_temp_geometry = Polyline(self.color, self.points) 
                print(f"Ponto adicionado: ({x:.2f}, {y:.2f})")

    def _handle_simple_shape_mouse(self, state, x, y):
        if state == GLUT_DOWN:
            self.started = True
            self.start(x, y)
            print(f"Iniciando desenho de {self.shape}")
        elif state == GLUT_UP and self.started:
            # Finaliza no mouse up
            geometry = self.finish(x, y)
            if geometry:
                self.canvas.addGeometry(geometry)
            self.started = False
            self.canvas.temp_geometry = None
            print(f"{self.shape} finalizado.")

    def onMotion(self, x, y):
        # Desenho de pré-visualização para círculo e retângulo
        if self.started and self.shape in ["rectangle", "circle"]:
            geometry = self.finish(x, y)
            self.canvas.temp_geometry = geometry 
            glutPostRedisplay()

    def onPassiveMotion(self, x, y):
        # Pré-visualização da linha da polilinha
        if self.started and self.shape == "polyline":
            geometry = self.make_line(x, y) 
            self.canvas.temp_geometry = geometry 
            glutPostRedisplay()
  
    def start(self, x, y):
        self.start_x = x
        self.start_y = y
        self.started = True
        
        if self.shape == "polyline":
            self.points = [(self.start_x, self.start_y)]
        
    def add_point(self, x, y):
        if self.shape == "polyline":
            self.points.append((x, y))

    def finish(self, x, y):
        # Finaliza o desenho
        if not self.started:
             return None
             
        match self.shape:
            case "polyline":
                self.add_point(x, y)
                if len(self.points) < 2: return None
                return Polyline(self.color, self.points)
            case "circle":
                radius = math.sqrt((self.start_x - x) ** 2 + (self.start_y - y) ** 2)
                if radius == 0: return None
                return Circle(self.start_x, self.start_y, radius, self.color)
            case "rectangle":
                width = x - self.start_x
                height = y - self.start_y
                if width == 0 or height == 0: return None
                return Rectangle(self.start_x, self.start_y, height, width, self.color)
            case _:
                return None
            
    def make_line(self, x,y):
        if self.shape == "polyline" and self.started:
            last_x, last_y = self.points[-1]
            return Line(last_x, last_y, x, y)
        return None