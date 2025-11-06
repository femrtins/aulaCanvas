import math
from geometry.circle import Circle
from geometry.rectangle import Rectangle
from geometry.polyline import Line, Polyline

class DrawingTool:
    def __init__(self, shape="rectangle"):
        self.shape = shape      # Mudar shape interativamente
        self.color = (0,0,0)    # Mudar color interativamente
        self.start_x = None
        self.start_y = None
        self.started = False
        self.points = []

    def start(self, x, y):
        # Inicializa o desenho quando o MOUSE_DOWN
        self.start_x = x
        self.start_y = y
        self.started = True
        
        if self.shape == "polyline":
            self.points.append((self.start_x,self.start_y))
        
    def add_point(self, x, y):
        if self.shape == "polyline":
            self.points.append((x, y))

    def finish(self, x, y):
        # Finaliza o desenho quando o MOUSE_UP
        match self.shape:
            case "polyline":
                self.add_point(x, y)
                return Polyline(self.color, self.points)
            case "circle":
                radius = math.sqrt((self.start_x - x) ** 2 + (self.start_y - y) ** 2)
                self.started = False 
                return Circle(self.start_x, self.start_y, radius, self.color)
            case "rectangle":
                width = x - self.start_x
                height = y - self.start_y
                self.started = False
                return Rectangle(self.start_x, self.start_y, height, width, self.color)
            
    def make_line(self, x,y):
        if self.shape == "polyline":
            return Line(self.start_x,self.start_y, x, y)

            
        
        