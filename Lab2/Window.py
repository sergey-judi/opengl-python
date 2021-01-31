from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

from Canvas import Canvas


class Window:

    def __init__(self, width, height, window_name):
        self.width = width
        self.height = height
        self.window_name = window_name
        self.is_perspective = True
        self.canvas = Canvas(width, height)

    def apply_settings(self):
        glMatrixMode(GL_PROJECTION)
        gluPerspective(120, 1, 1, 1000)
        glOrtho(-self.width / 2, self.width / 2, -self.height / 2, self.height / 2, -1000, 1000)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        glClearColor(1, 1, 1, 1)
        self.canvas.calculate_eye_position()
        self.canvas.set_eye_pos()
        glViewport(0, 0, self.width, self.height)

    def show(self, pos_x=0, pos_y=0):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(pos_x, pos_y)
        glutCreateWindow(self.window_name)
        self.apply_settings()
        glutDisplayFunc(self.canvas.display)
        glutKeyboardFunc(self.keyboard)
        glutReshapeFunc(self.reshape)
        glutMouseWheelFunc(self.wheel_func)
        glutMainLoop()

    def reshape(self, w, h):
        self.width = self.canvas.width = w
        self.height = self.canvas.height = h
        glMatrixMode(GL_PROJECTION)
        if self.is_perspective:
            gluPerspective(60, 1, 1, 1000)
        glLoadIdentity()
        glOrtho(-self.width / 2, self.width / 2, -self.height / 2, self.height / 2, -1000, 1000)
        glMatrixMode(GL_MODELVIEW)
        self.canvas.set_eye_pos()
        glViewport(0, 0, self.width, self.height)

    def keyboard(self, key, x, y):
        glLoadIdentity()
        pressed_key = key.decode("utf-8").lower()
        if pressed_key == chr(27):
            sys.exit(0)
        elif pressed_key == 'p' and self.is_perspective is False:
            self.is_perspective = True
            self.reshape(self.width, self.height)
            glLoadIdentity()
        elif pressed_key == 'o' and self.is_perspective is True:
            self.is_perspective = False
            self.reshape(self.width, self.height)
        if self.is_perspective:
            if pressed_key == ' ':
                self.canvas.phi = 0.0
                self.canvas.theta = 90.0
                self.canvas.up_x = self.canvas.up_z = 0
                self.canvas.up_y = 1
            elif pressed_key == 'w':
                self.canvas.theta = (self.canvas.theta - 5) % 360
                if self.canvas.theta == 0:
                    self.canvas.theta = -5 % 360
            elif pressed_key == 's':
                self.canvas.theta = (self.canvas.theta + 5) % 360
                if self.canvas.theta == 0:
                    self.canvas.theta = 5 % 360
            elif pressed_key == 'd':
                self.canvas.phi = (self.canvas.phi + 5) % 360
            elif pressed_key == 'a':
                self.canvas.phi = (self.canvas.phi - 5) % 360

            if 0 < self.canvas.theta <= 180:
                self.canvas.up_y = 1
            else:
                self.canvas.up_y = -1
            self.canvas.set_eye_pos()
        glutPostRedisplay()

    def wheel_func(self, wheel, direction, x, y):
        if self.is_perspective:
            # if mouse wheel is moving forward zoom in
            if direction > 0:
                self.canvas.scale *= 1.1
                glScale(1.1, 1.1, 1.1)
            # if mouse wheel is moving backward zoom out
            elif direction < 0:
                self.canvas.scale *= 0.9
                glScale(0.9, 0.9, 0.9)
            # call display function
            glutPostRedisplay()
