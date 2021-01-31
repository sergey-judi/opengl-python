from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos, pi

from Surface import Surface
from Light import Light
from Cube import Cube
from Sphere import Sphere


class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.eye_x = self.eye_y = self.eye_z = 0
        self.radius = 100
        self.phi = 0.0
        self.theta = 90.0
        self.up_x = 0
        self.up_y = 1
        self.up_z = 0
        self.scale = 1
        self.surface = Surface(lambda x, y: 50*(sin(x * pi / 180) + cos(y * pi / 180)))
        self.light = Light()
        self.cube = Cube(10)
        self.sphere = Sphere(20)
        self.enable_light_source= True

    def calculate_eye_position(self):
        self.eye_z = self.radius * sin(self.theta * pi / 180) * cos(self.phi * pi / 180)
        self.eye_x = self.radius * sin(self.theta * pi / 180) * sin(self.phi * pi / 180)
        self.eye_y = self.radius * cos(self.theta * pi / 180)

    def set_eye_pos(self):
        self.calculate_eye_position()
        gluLookAt(self.eye_x, self.eye_y, self.eye_z, 0, 0, 0, self.up_x, self.up_y, self.up_z)
        self.set_scale()

    def emplace_light_source(self):
        glPushMatrix()
        light_position = (self.light.pos_x, self.light.pos_y, self.light.pos_z, 0)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glPopMatrix()

        glPushMatrix()

        glTranslatef(self.light.pos_x, self.light.pos_y, self.light.pos_z)

        glPushMatrix()
        glTranslatef(self.light.satellite_pos_x, self.light.satellite_pos_y, self.light.satellite_pos_z)
        glRotated(self.light.satellite_phi, 0, 1, 0)
        glColor3f(0.5, 0.5, 0.5)
        self.cube.draw()
        glPopMatrix()

        glPushMatrix()
        glRotated(90, 1, 0, 0)
        glRotated(self.light.phi, 0, 0, 1)
        self.sphere.draw()
        glPopMatrix()

        glPopMatrix()

    def draw_axis(self):
        # x-axis and the arrow
        glPushMatrix()
        glRotate(90, 0, 1, 0)
        glTranslated(0, 0, 50)
        glColor3f(1, 0, 0)
        glutSolidCone(2, 5, 100, 100)
        glPopMatrix()
        glBegin(GL_LINE_LOOP)
        glVertex3f(0, 0, 0)
        glVertex3f(50, 0, 0)
        glEnd()

        # y-axis and the arrow
        glPushMatrix()
        glRotate(-90, 1, 0, 0)
        glTranslated(0, 0, 50)
        glColor3f(0, 1, 0)
        glutSolidCone(2, 5, 100, 100)
        glPopMatrix()
        glBegin(GL_LINE_LOOP)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 50, 0)
        glEnd()

        # z-axis and the arrow
        glPushMatrix()
        glTranslated(0, 0, 50)
        glColor3f(0, 0, 1)
        glutSolidCone(2, 5, 100, 100)
        glPopMatrix()

        glBegin(GL_LINE_LOOP)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 50)
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslated(0, 150, 0)
        glColor3f(0.3, 0.6, 0.6)
        glutSolidCube(20)
        glPopMatrix()

        self.draw_axis()

        glColor3f(1, 1, 0)
        self.surface.draw()

        self.emplace_light_source()

        glFlush()

    def set_scale(self):
        glScale(self.scale, self.scale, self.scale)
