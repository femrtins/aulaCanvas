class Geometry:
    def __init__(self, x0, y0, color):
        self.x0 = x0
        self.y0 = y0
        self.color = color
        self.is_selected = False
        self.type = None
        
    def draw(self):
        pass
    
    def draw_open(self):
        pass
    
    def contains_point(self, x, y):
        # fazer uma reta horizontal a partir do ponto (x, y) e contar intersecoes
        pass
        
    