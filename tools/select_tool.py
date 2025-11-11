import math
from utils.glut_utils import *
from tools.tool import Tool 
from tools.color import Color

class SelectTool(Tool):
    def __init__(self, canvas ):
        super().__init__(canvas)
        self.selected_geometry = []
        self.mode = 'translate' 
        self.start_x = None
        self.start_y = None
        self.is_dragging = False
        self.canvas.color = Color(-99,-99)
  

    def get_selected_object(self):
        return self.get_selected_object

    def activate(self):
        self.mode = 'translate'
        print("Ferramenta de Seleção Ativa. Modos: [t]ransladar, [e]scalar, [o] rotacionar, [d] deletar, [x] consultar")

    def deactivate(self):
        self.deselect_geometry()

    def deselect_geometry(self):
        self.selected_geometry = []
        self.canvas.selection_box = None
        self.is_dragging = False
        glutPostRedisplay()

    def select_geometry(self, x, y, add=False, toggle=False):
        """Tenta selecionar uma geometria em (x, y)."""
        # self.deselect_geometry() 
        
        # # for da lista das geometrias com reversed 
        # for geometry in reversed(self.canvas.geometries):
        #     if geometry.contains_point(x, y):
        #         self.selected_geometry.append(geometry)
        #         self.canvas.selection_box = SelectionBox(geometry)
        #         glutPostRedisplay()
        #         return True
        
        # return False
        
        hit = None
        for geometry in reversed(self.canvas.geometries):
            if geometry.contains_point(x, y):
                hit = geometry
                break

        if not hit:
            # nothing hit
            if not add and not toggle:
                # replace selection with none
                self.deselect_geometry()
            return False

        if toggle:
            if hit in self.selected_geometries:
                self.selected_geometries.remove(hit)
            else:
                self.selected_geometries.append(hit)
        elif add:
            if hit not in self.selected_geometries:
                self.selected_geometries.append(hit)
        else:
            # replace selection
            self.selected_geometries = [hit]

        # update selection box (combined for all selected)
        self.canvas.selection_box = SelectionBox(self.selected_geometries)
        glutPostRedisplay()
        return True

    def onKeyboard(self, key, x, y):
        """Define o modo de transformação."""
        if not self.selected_geometry:
            print("Selecione um objeto primeiro (tecla 's')")
            return 

        key_lower = key.lower()
        if key_lower == b't':
            self.mode = 'translate'
            print(f"Modo: {self.mode}")
        elif key_lower == b'o': 
            self.mode = 'rotate'
            print(f"Modo: {self.mode}")
        elif key_lower == b'e':
            self.mode = 'scale'
            print(f"Modo: {self.mode}")
        elif key_lower == b'd':
            self.mode = 'delete'
            self._delete()
            print(f"Modo: {self.mode}")
        elif key_lower == b'x':
            self.mode = 'consulte'
            self._consulte()
            print(f"Modo: {self.mode}")
            glutPostRedisplay()

    def onMouse(self, button, state, x, y, is_double_click=False):
        if button != GLUT_LEFT_BUTTON:
            return
        
        if state == GLUT_DOWN and self.canvas.color.inside(x,y) != None:
            self._paint(x,y)
            return

        if state == GLUT_DOWN :
            # check modifier for multi-selection (Shift)
            mods = glutGetModifiers()
            shift = bool(mods & GLUT_ACTIVE_SHIFT)

            # toggle with Ctrl? (optional)
            ctrl = bool(mods & GLUT_ACTIVE_CTRL)

            # If shift -> add, if ctrl -> toggle, else replace
            if shift:
                hit = self.select_geometry(x, y, add=True)
            elif ctrl:
                hit = self.select_geometry(x, y, toggle=True)
            else:
                hit = self.select_geometry(x, y, add=False, toggle=False)

            # start dragging if clicked on a selected geometry
            if hit:
                # if the clicked geometry is selected (already ensured), start drag
                self.is_dragging = True
                self.start_x = x
                self.start_y = y
            else:
                # clicked empty area -> deselect (unless shift/ctrl were used)
                if not (shift or ctrl):
                    self.deselect_geometry()

        # elif state == GLUT_DOWN :
        #     hit_geometry = False
            # Verifica se clicou em um objeto já selecionado
        
        
            
            # if self.selected_geometry and self.selected_geometry.contains_point(x, y):
            #     hit_geometry = True
            # else:
            #     # Se não, tenta selecionar um novo
            #     hit_geometry = self.select_geometry(x, y)

            # if hit_geometry:
            #     self.is_dragging = True
            #     self.start_x = x
            #     self.start_y = y
             
        elif state == GLUT_UP:
            self.is_dragging = False
            self.start_x = None
            self.start_y = None

    def onMotion(self, x, y):
        """Chamado quando arrastamos o mouse."""
        if not self.is_dragging or not self.selected_geometry:
            return

        # Delega para a função de transformação apropriada
        if self.mode == 'translate':
            self._translate(x, y)
        elif self.mode == 'scale':
            self._scale(x, y)
        elif self.mode == 'rotate':
            self._rotate(x, y)

        
        self.start_x = x
        self.start_y = y
        
        
        glutPostRedisplay()

    # --- Métodos Privados de Transformação  ---

    def _translate(self, current_x, current_y):
        if self.start_x is None: return
        dx = current_x - self.start_x
        dy = current_y - self.start_y
        g = self.selected_geometry
        
        # Move o pivô
        g.x0 += dx
        g.y0 += dy
        
        # move todos os pontos da polilinha 
        if hasattr(g, 'points'):
            g.points = [(px + dx, py + dy) for (px, py) in g.points]

    def _scale(self, current_x, current_y):
        if self.start_x is None: return
        
        g = self.selected_geometry
        
        # (Movimento para a direita/cima aumenta, esquerda/baixo diminui)
        dx = current_x - self.start_x
        dy = current_y - self.start_y
        
        scale_factor = 1.0 + (dx + dy) * 0.01 
        scale_factor = max(0.1, scale_factor) # evita inverter/ ou zero
            
        if hasattr(g, 'width'):
            g.width *= scale_factor
            g.height *= scale_factor
        elif hasattr(g, 'radius'):
            g.radius *= scale_factor
        elif hasattr(g, 'points'):
            # escala polilinha em relação ao seu pivô 
            new_points = []
            for (px, py) in g.points:
                # vetor do pivô ao ponto
                vx = px - g.x0
                vy = py - g.y0
                # escala o vetor
                vx_new = vx * scale_factor
                vy_new = vy * scale_factor
                # adiciona de volta ao pivô
                new_points.append((g.x0 + vx_new, g.y0 + vy_new))
            g.points = new_points

    def _rotate(self, current_x, current_y):
        if not self.selected_geometry or self.start_x is None:
            return

        dy = current_y - self.start_y
        angle_delta = dy * 1.0 
        
        self.selected_geometry.angle += angle_delta
    
    def _delete(self):
        if not self.selected_geometry:
            return
        
        self.canvas.geometries.remove(self.selected_geometry)
        self.selected_geometry = None
    
    def _consulte(self):
        if not self.selected_geometry:
            return
        
        print(f"Área: {self.selected_geometry.area():.2f}u²" )
        print(f"Perimetro: {self.selected_geometry.perimeter():.2f}u" )
        
    def _paint(self, x, y):
        if not self.selected_geometry:
            return

        selector = self.canvas.color.inside(x, y)
        print(selector)  

        if selector:
            selector.picker.move(x)
            self.selected_geometry.color = self.canvas.color.calculate_color()
            glutPostRedisplay()

        
        
    

        


# -----------------------------------------------------------------
# CAIXA DE SELEÇÃO 
# -----------------------------------------------------------------
class SelectionBox:
    def __init__(self, geometry):
        self.geometry = geometry
    

    def draw(self):
        """Desenha a caixa usando as mesmas transformações do objeto."""
        
        g = self.geometry
        glPushMatrix()

        try:
            
            if g.type == "Rec":
            
                cx = g.x0 + g.width / 2.0
                cy = g.y0 + g.height / 2.0
                w_half = g.width / 2.0
                h_half = g.height / 2.0
                
                glTranslatef(cx, cy, 0)
                glRotatef(g.angle, 0, 0, 1)
                
                self._draw_box_outline(-w_half, -h_half, w_half, h_half)
                
            elif g.type == "Circ":
                cx = g.x0
                cy = g.y0
                r = g.radius
                
                glTranslatef(cx, cy, 0)
                glRotatef(g.angle, 0, 0, 1)
                
                self._draw_box_outline(-r, -r, r, r)
                
            elif hasattr(g, 'points'):

                cx = g.x0
                cy = g.y0
                
                glTranslatef(cx, cy, 0)
                glRotatef(g.angle, 0, 0, 1)
                
                local_points = [(px - cx, py - cy) for (px, py) in g.points]
                min_x = min(p[0] for p in local_points)
                max_x = max(p[0] for p in local_points)
                min_y = min(p[1] for p in local_points)
                max_y = max(p[1] for p in local_points)
                self._draw_box_outline(min_x, min_y, max_x, max_y)
        
        finally:
            glPopMatrix()

    def _draw_box_outline(self, x_min, y_min, x_max, y_max):
        
        glLineStipple(5, 0xAAAA)
        glEnable(GL_LINE_STIPPLE)
        glColor3f(0.2, 0.2, 0.8) 
        glLineWidth(2.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x_min, y_min)
        glVertex2f(x_max, y_min)
        glVertex2f(x_max, y_max)
        glVertex2f(x_min, y_max)
        glEnd()
        glDisable(GL_LINE_STIPPLE)
        glLineWidth(1.0)
        
        # Handles
        glColor3f(0.2, 0.2, 0.8)
        self._draw_handle(x_min, y_min)
        self._draw_handle(x_max, y_min)
        self._draw_handle(x_max, y_max)
        self._draw_handle(x_min, y_max)

    def _draw_handle(self, x, y, size=1):
        s = size 
        glBegin(GL_QUADS)
        glVertex2f(x - s, y - s)
        glVertex2f(x + s, y - s)
        glVertex2f(x + s, y + s)
        glVertex2f(x - s, y + s)
        glEnd()