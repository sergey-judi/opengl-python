from OpenGL.GL import *
from IDrawable import IDrawable


class Cube(IDrawable):

    def __init__(self, length):
        self.length = length
        self.point_array = []
        self.normal_array = []
        self.get_point_data()

    def get_point_data(self):
        self.point_array = [
            # задняя грань
            [-self.length / 2, -self.length / 2, -self.length / 2],
            [-self.length / 2, self.length / 2, -self.length / 2],
            [self.length / 2, self.length / 2, -self.length / 2],
            [self.length / 2, -self.length / 2, -self.length / 2],
            # левая боковая грань
            [-self.length / 2, -self.length / 2, self.length / 2],
            [-self.length / 2, self.length / 2, self.length / 2],
            [-self.length / 2, self.length / 2, -self.length / 2],
            [-self.length / 2, -self.length / 2, -self.length / 2],
            # верхняя грань
            [-self.length / 2, self.length / 2, self.length / 2],
            [-self.length / 2, self.length / 2, -self.length / 2],
            [self.length / 2, self.length / 2, -self.length / 2],
            [self.length / 2, self.length / 2, self.length / 2],
            # правая боковая грань
            [self.length / 2, -self.length / 2, self.length / 2],
            [self.length / 2, self.length / 2, self.length / 2],
            [self.length / 2, self.length / 2, -self.length / 2],
            [self.length / 2, -self.length / 2, -self.length / 2],
            # нижняя грань
            [-self.length / 2, -self.length / 2, self.length / 2],
            [-self.length / 2, -self.length / 2, -self.length / 2],
            [self.length / 2, -self.length / 2, -self.length / 2],
            [self.length / 2, -self.length / 2, self.length / 2],
            # передняя грань
            [-self.length / 2, -self.length / 2, self.length / 2],
            [-self.length / 2, self.length / 2, self.length / 2],
            [self.length / 2, self.length / 2, self.length / 2],
            [self.length / 2, -self.length / 2, self.length / 2]
        ]

        self.normal_array = [
            [0, 0, 1] * 4,
            [1, 0, 0] * 4,
            [0, -1, 0] * 4,
            [-1, 0, 0] * 4,
            [0, 1, 0] * 4,
            [0, 0, -1] * 4
        ]

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.point_array)
        glNormalPointer(GL_FLOAT, 0, self.normal_array)
        glDrawArrays(GL_QUADS, 0, len(self.point_array))
        glDisableClientState(GL_NORMAL_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)
