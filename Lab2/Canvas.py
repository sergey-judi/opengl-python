from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos, pi

from Surface import Surface


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
        self.surface = Surface()

    def calculate_eye_position(self):
        self.eye_z = self.radius * sin(self.theta * pi / 180) * cos(self.phi * pi / 180)
        self.eye_x = self.radius * sin(self.theta * pi / 180) * sin(self.phi * pi / 180)
        self.eye_y = self.radius * cos(self.theta * pi / 180)
        #self.eye_x = sin(self.theta * pi / 180) * cos(self.phi * pi / 180)
        #self.eye_y = sin(self.theta * pi / 180) * sin(self.phi * pi / 180)
        #self.eye_z = cos(self.theta * pi / 180)

    def set_eye_pos(self):
        self.calculate_eye_position()
        gluLookAt(self.eye_x, self.eye_y, self.eye_z, 0, 0, 0, self.up_x, self.up_y, self.up_z)
        self.set_scale()

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

    def draw_surface(self, vertex_array=True):
        if vertex_array:
            glEnableClientState(GL_VERTEX_ARRAY)
            glVertexPointer(3, GL_FLOAT, 0, self.surface.point_array)
            glDrawArrays(GL_LINES, 0, len(self.surface.point_array))
            glDisableClientState(GL_VERTEX_ARRAY)
        else:
            glBegin(GL_LINES)
            for x, y, z in self.surface.point_array:
                glVertex3f(x, y, z)
            glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(0, 0, 0)
        glutSolidSphere(1, 10, 10)

        glPushMatrix()
        glTranslated(0, 150, 0)
        glColor3f(0, 0, 0)
        glutWireCube(10)
        # glColor3f(0.3, 0.6, 0.6)
        # glutSolidCube(10)
        glPopMatrix()

        glPushMatrix()
        glTranslated(0, -50, 0)
        glRotate(-90, 1, 0, 0)
        glColor3f(0.5, 0, 1)
        glutSolidCone(10, 20, 10, 10)
        glPopMatrix()

        self.draw_axis()
        glColor3f(1, 1, 0)
        self.draw_surface(vertex_array=True)
        glFlush()

    def set_scale(self):
        glScale(self.scale, self.scale, self.scale)
