from utils.glut_utils import *
from canvas.canvas import Canvas
from input.inputHandler import InputHandler
import sys

canvas = Canvas(left=-100, right=100, bottom=-100, top=100)
WIDHT = 800
HEIGHT = 800

input_handler = InputHandler(canvas)

def display_callback():
    canvas.showScreen(WIDHT, HEIGHT)

def reshape_callback(width, height):
    canvas.onReshape(width, height)

def keyboard_callback(key, x, y):
    input_handler.onKeyboard(key, x, y)

def mouse_callback(button, state, x, y):
    input_handler.onMouse(button, state, x, y)

def motion_callback(x, y):
    input_handler.onMotion(x, y)
    
def passive_motion_callback(x, y):
    input_handler.onPassiveMotion(x, y)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(WIDHT, HEIGHT)
glutCreateWindow(b"Canvas")

glutDisplayFunc(display_callback)
glutReshapeFunc(reshape_callback)
glutKeyboardFunc(keyboard_callback)
glutMouseFunc(mouse_callback)
glutMotionFunc(motion_callback)
glutPassiveMotionFunc(passive_motion_callback)

glutMainLoop()
