# input/tool.py (Novo arquivo)
class Tool:
    """Classe base abstrata para todas as ferramentas (desenho, seleção, etc.)"""
    def __init__(self, canvas):
        self.canvas = canvas

    def onMouse(self, button, state, x, y):
        """Chamado no evento de clique do mouse."""
        pass

    def onMotion(self, x, y):
        """Chamado no evento de movimento com o mouse pressionado."""
        pass

    def onPassiveMotion(self, x, y):
        """Chamado no evento de movimento com o mouse solto."""
        pass
    
    def onKeyboard(self, key, x, y):
        """Chamado no evento de teclado."""
        pass

    def activate(self):
        """Chamado quando a ferramenta se torna ativa."""
        print(f"Ativando {self.__class__.__name__}")
        pass

    def deactivate(self):
        """Chamado quando a ferramenta é desativada."""
        print(f"Desativando {self.__class__.__name__}")
        pass