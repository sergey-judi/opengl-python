from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from Canvas import Canvas

# if MOVEMENT_MODE is 0, a figure can move in all directions
# else figure can move only along vector (-1, 0)
MOVEMENT_MODE = 0


class Window:

    def __init__(self, width, height, window_name, coeff=10, grid_coeff=30):
        self.width = width
        self.height = height
        self.window_name = window_name
        self.canvas = Canvas(width, height, coeff, grid_coeff)

    def apply_settings(self):
        # bg color, viewport settings and (0, 0) position
        glViewport(0, 0, self.width, self.height)
        glClearColor(0, 0.5, 0.5, 1)
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        glOrtho(0, self.width, 0, self.height, 1.0, -1.0)

    def show(self, pos_x=0, pos_y=0):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(pos_x, pos_y)
        glutCreateWindow(self.window_name)
        # bg color, viewport settings and (0, 0) position
        self.apply_settings()
        # set callback functions
        glutDisplayFunc(self.canvas.display_figure)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutMouseFunc(self.mouse_func)
        glutMotionFunc(self.motion_func)
        glutMouseWheelFunc(self.wheel_func)
        glutMainLoop()

    def set_figure_pos(self, x, y):
        # placing a figure in the beginning of execution
        self.canvas.fpos_x = x
        self.canvas.fpos_y = y

    def reshape(self, w, h):
        # compute a new figure position in reshaped window
        self.canvas.fpos_x *= w / self.canvas.width
        self.canvas.fpos_y *= h / self.canvas.height
        # new width and height of reshaped window
        self.width = self.canvas.width = w
        self.height = self.canvas.height = h
        # viewport settings and (0, 0) position
        self.apply_settings()
        # apply changes
        self.canvas.update()

    def keyboard(self, key, x, y):
        pressed_key = key.decode("utf-8").lower()
        if pressed_key == chr(27):
            sys.exit(0)
        if pressed_key == ' ':
            self.canvas.fpos_x = self.width / 2
            self.canvas.fpos_y = self.height / 2
        if MOVEMENT_MODE:
            if pressed_key == 'w' or pressed_key == 's':
                if 0 < self.canvas.fpos_x:
                    self.canvas.fpos_x -= self.canvas.grid_coeff
            elif pressed_key == 'a' or pressed_key == 'd':
                if self.canvas.fpos_x < self.width:
                    self.canvas.fpos_x += self.canvas.grid_coeff
        else:
            if pressed_key == 'w':
                if self.canvas.fpos_y + self.canvas.grid_coeff < self.height:
                    self.canvas.fpos_y += self.canvas.grid_coeff
            elif pressed_key == 's':
                if self.canvas.fpos_y - self.canvas.grid_coeff > 0:
                    self.canvas.fpos_y -= self.canvas.grid_coeff
            elif pressed_key == 'd':
                if self.canvas.fpos_x + self.canvas.grid_coeff < self.width:
                    self.canvas.fpos_x += self.canvas.grid_coeff
            elif pressed_key == 'a':
                if self.canvas.fpos_x - self.canvas.grid_coeff > 0:
                    self.canvas.fpos_x -= self.canvas.grid_coeff
        self.canvas.update()
        glutPostRedisplay()

    def mouse_func(self, button, state, x, y):
        # remember coordinates when mouse button was pressed
        self.canvas.pressed_x = x
        self.canvas.pressed_y = y

    def motion_func(self, x, y):
        # compute the distance the pointer has gone
        dx = x - self.canvas.pressed_x
        dy = y - self.canvas.pressed_y
        # move figure coordinates
        if 0 < self.canvas.fpos_x + dx < self.canvas.width:
            self.canvas.fpos_x += dx
        if 0 < self.canvas.fpos_y - dy < self.canvas.height:
            self.canvas.fpos_y -= dy
        # remember coordinates when pointer is moving
        self.canvas.pressed_x = x
        self.canvas.pressed_y = y
        # apply changes
        self.canvas.update()
        # call display function
        glutPostRedisplay()

    def wheel_func(self, wheel, direction, x, y):
        # if mouse wheel is moving forward zoom in
        if direction > 0 and self.canvas.coeff < 60:
            self.canvas.coeff += 5
        # if mouse wheel is moving backward zoom out
        elif direction < 0 and self.canvas.coeff > 5:
            self.canvas.coeff -= 5
        # apply changes
        self.canvas.update()
        # call display function
        glutPostRedisplay()
