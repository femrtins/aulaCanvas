class Geometry:
    def __init__(self, x0, y0, color):
        self.x0 = x0
        self.y0 = y0
        self.color = color
        self.is_selected = False
        self.type = None
        self.angle = 0.0
        
    def draw(self):
        pass
    
    def draw_open(self):
        pass
    
    def contains_point(self, x, y):
        # Implementação do algoritmo Ray-Casting (Ponto em Polígono)
        n = len(self.points)
        inside = False
        
        p1x, p1y = self.points[0]
        for i in range(n + 1):
            p2x, p2y = self.points[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
            
        self.is_selected = inside
        return inside
        
    