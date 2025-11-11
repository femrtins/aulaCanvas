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

    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def contains_point(self, x, y):
        n = len(self.points)
        inside = False
        
        x1, y1 = self.points[0]
        for i in range(n + 1):
            x2, y2 = self.points[i % n]
            if y > min(y1, y2):
                if y <= max(y1, y2):
                    if x <= max(x1, x2):
                        if y1 != y2:
                            inters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                        if x1 == x2 or x <= inters:
                            inside = not inside
            x1, y1 = x2, y2
            
        self.is_selected = inside
        return inside
        
    