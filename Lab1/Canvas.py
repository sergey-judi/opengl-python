from OpenGL.GL import *
from DataProvider import DataProvider
from Point import Point


class Canvas:

    def __init__(self, width, height, coeff, grid_coeff):
        self.width = width
        self.height = height
        self.coeff = coeff
        self.grid_coeff = grid_coeff
        self.fpos_x = width / 2
        self.fpos_y = height / 2
        self.pressed_x = 0
        self.pressed_y = 0
        self.provider = DataProvider(self.fpos_x, self.fpos_y, self.coeff)

    def draw_axis(self):
        # drawing grid lines with given step value
        step = self.grid_coeff
        # drawing central axis
        glLineWidth(2)
        Canvas.draw_line(Point(self.width/2, 0), Point(self.width/2, self.height), True, False)
        Canvas.draw_line(Point(0, self.height/2), Point(self.width, self.height/2), False, True)
        glLineWidth(1)
        # drawing grid in all directions
        glBegin(GL_LINES)
        i = self.width/2
        while i < self.width:
            Canvas.draw_line(Point(i, 0), Point(i, self.height), False, False)
            i += step
        i = self.width/2
        while i > 0:
            Canvas.draw_line(Point(i, 0), Point(i, self.height), False, False)
            i -= step
        i = self.height/2
        while i < self.height:
            Canvas.draw_line(Point(0, i), Point(self.width, i), False, False)
            i += step
        i = self.height/2
        while i > 0:
            Canvas.draw_line(Point(0, i), Point(self.width, i), False, False)
            i -= step
        glEnd()

    def draw_polygons(self):
        # vertex is a list of points (Points(x, y))
        vertex = self.provider.update_point_data()

        # triangle is a list of vertices numbers that it consists of
        # len(triangle) = 3
        for triangle in self.provider.vertex_data['triangles']:
            Canvas.draw_triangle(
                vertex[triangle[0]],
                vertex[triangle[1]],
                vertex[triangle[2]]
            )

        # quad is a list of vertices numbers that it consists of
        # len(quad) = 4
        for quad in self.provider.vertex_data['quads']:
            Canvas.draw_rectangle(
                vertex[quad[0]],
                vertex[quad[1]],
                vertex[quad[2]],
                vertex[quad[3]]
            )

    def display_figure(self):
        glClear(GL_COLOR_BUFFER_BIT)

        # draw grid
        glPolygonMode(GL_FRONT, GL_LINE)
        glColor3f(0.2, 0.9, 0.7)
        self.draw_axis()

        # draw filled polygons
        glPolygonMode(GL_FRONT, GL_FILL)
        glColor3f(0.4, 1.0, 0.6)
        self.draw_polygons()

        # draw only contours of polygons
        glPolygonMode(GL_FRONT, GL_LINE)
        glColor3f(0.0, 0.0, 0.0)
        self.draw_polygons()

        glFinish()

    def update(self):
        # update provider filed in order to update point data
        self.provider.update_pos_x(self.fpos_x)
        self.provider.update_pos_y(self.fpos_y)
        self.provider.update_coeff(self.coeff)

    @staticmethod
    def draw_line(point1, point2, begin=True, end=True):
        if begin:
            glBegin(GL_LINES)
        glVertex2f(point1.x, point1.y)
        glVertex2f(point2.x, point2.y)
        if end:
            glEnd()

    @staticmethod
    def draw_triangle(point1, point2, point3, begin=True, end=True):
        if begin:
            glBegin(GL_TRIANGLES)
        glVertex2f(point1.x, point1.y)
        glVertex2f(point2.x, point2.y)
        glVertex2f(point3.x, point3.y)
        if end:
            glEnd()

    @staticmethod
    def draw_rectangle(point1, point2, point3, point4, begin=True, end=True):
        if begin:
            glBegin(GL_QUADS)
        glVertex2f(point1.x, point1.y)
        glVertex2f(point2.x, point2.y)
        glVertex2f(point3.x, point3.y)
        glVertex2f(point4.x, point4.y)
        if end:
            glEnd()
