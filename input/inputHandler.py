import time, os
from utils.glut_utils import *
from utils.world_coordinates import getWorldCoords
from tools.drawing_tool import DrawingTool
from tools.select_tool import SelectTool


class InputHandler:
    def __init__(self, canvas):
        self.canvas = canvas
        
        self.drawing_tool = DrawingTool(canvas)
        self.select_tool = SelectTool(canvas)
        
        self.tools = {
            b'r': self.drawing_tool,
            b'c': self.drawing_tool,
            b'p': self.drawing_tool,
            b's': self.select_tool,
        }
        
        self.active_tool = None 
        
        # clique duplo
        self.last_click_time = 0
        self.double_click_threshold = 0.3

    def set_active_tool(self, key):
        if key not in self.tools:
            # Se a tecla não for uma ferramenta, passa para a ferramenta ativa.
            if self.active_tool:
                self.active_tool.onKeyboard(key, 0, 0) 
            return

        new_tool = self.tools[key]

        # Se a ferramenta mudou, desative a antiga e ative a nova
        if self.active_tool != new_tool:
            if self.active_tool:
                self.active_tool.deactivate() 
            self.active_tool = new_tool
            self.active_tool.activate() 

        # Configurações específicas para a DrawingTool
        if new_tool == self.drawing_tool:
            if key == b'r':
                self.drawing_tool.shape = "rectangle"
            elif key == b'c':
                self.drawing_tool.shape = "circle"
            elif key == b'p':
                self.drawing_tool.shape = "polyline"
            # Ativa a ferramenta de desenho
            self.drawing_tool.activate()

    def onKeyboard(self, key, x , y) -> None:
        key_lower = key.lower()

        # Tecla ESC
        if key == b'\x1b': 
            if self.active_tool == self.drawing_tool and self.drawing_tool.started:
                # Se estiver desenhando, ESC cancela
                self.drawing_tool.deactivate()
            elif self.active_tool == self.select_tool and self.select_tool.get_selected_object():
                # Se estiver selecionando, ESC deseleciona
                self.select_tool.deselect_geometry()
            else:
                # Se não, sai do programa
                print("Saindo...")
                try:
                    glutLeaveMainLoop()
                except Exception:
                    os._exit(0)
            return

        self.set_active_tool(key_lower)
            
    def onMouse(self, button, state, mouse_x, mouse_y):
        x, y = getWorldCoords(mouse_x, mouse_y, self.canvas)
        
        # Verifica clique duplo
        now = time.time()
        is_double_click = (state == GLUT_DOWN) and (now - self.last_click_time < self.double_click_threshold)
        
        if state == GLUT_DOWN:
            self.last_click_time = now
            
        if self.active_tool:
            self.active_tool.onMouse(button, state, x, y, is_double_click)

    def onMotion(self, mouse_x, mouse_y):
        x, y = getWorldCoords(mouse_x, mouse_y, self.canvas)
        
        if self.active_tool:
            self.active_tool.onMotion(x, y)
                
    def onPassiveMotion(self, mouse_x, mouse_y):
        x, y = getWorldCoords(mouse_x, mouse_y, self.canvas)
        
        if self.active_tool:
            self.active_tool.onPassiveMotion(x, y)