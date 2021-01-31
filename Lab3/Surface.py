from OpenGL.GL import *
import numpy as np
from IDrawable import IDrawable


class Surface(IDrawable):

    def __init__(self, custom_func):
        self.x_bound = 200
        self.y_bound = 200
        self.step_x = 10
        self.step_y = 10
        self.point_array = []
        self.normal_array = []
        self.function = custom_func
        self.get_point_data()

    @staticmethod
    def function(x, y):
        pass

    def get_point_data(self):
        self.compute_points(self.x_bound, self.y_bound, self.step_x, self.step_y, swap=False)
        self.compute_points(self.y_bound, self.x_bound, self.step_y, self.step_x, swap=True)

    def compute_points(self, x_bound, z_bound, step_x, step_z, swap=False):
        x = -x_bound
        while x != x_bound + step_x:
            z = -z_bound
            while z != z_bound:
                z += step_z
                if not swap:
                    y = self.function(x, z)
                    self.point_array.append([x, y, z])
                    normal = self.compute_normals(x, y, z)
                    self.normal_array.append(normal)
                else:
                    y = self.function(z, x)
                    self.point_array.append([z, y, x])
                    normal = self.compute_normals(z, y, x)
                    self.normal_array.append(normal)
            x += step_x
        x = -x_bound
        while x != x_bound + step_x:
            z = z_bound
            while z != -z_bound:
                z -= step_z
                if not swap:
                    y = self.function(x, z)
                    self.point_array.append([x, y, z])
                    normal = self.compute_normals(x, y, z)
                    self.normal_array.append(normal)
                else:
                    y = self.function(z, x)
                    self.point_array.append([z, y, x])
                    normal = self.compute_normals(z, y, x)
                    self.normal_array.append(normal)
            x += step_x

    def compute_normals(self, x1, y1, z1):
        x2 = x1+1
        z2 = z1
        y2 = self.function(x2, z2)
        x3 = x1
        z3 = z1+1
        y3 = self.function(x3, z3)

        a = np.array([x1, y1, z1])
        b = np.array([x2, y2, z2])
        c = np.array([x3, y3, z3])
        p = b - a
        q = c - a
        n = np.cross(q, p)
        norm = np.linalg.norm(n)
        return list(n/norm)

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.point_array)
        glNormalPointer(GL_FLOAT, 0, self.normal_array)
        glDrawArrays(GL_LINES, 0, len(self.point_array))
        glDisableClientState(GL_NORMAL_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)
