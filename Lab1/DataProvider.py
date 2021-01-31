import json
from Point import Point

# if INPUT_FILE string is empty ('') the information about figure will be created
# else get data from the given file
INPUT_FILE = 'vertex_data_upd.json'
WRITE_TO_FILE = False


class DataProvider:

    def __init__(self, fpos_x, fpos_y, coeff):
        self.fpos_x = fpos_x
        self.fpos_y = fpos_y
        self.coeff = coeff
        self.vertex_data = None
        self.init_vertex_data()

    def update_pos_x(self, new_x):
        self.fpos_x = new_x

    def update_pos_y(self, new_y):
        self.fpos_y = new_y

    def update_coeff(self, new_coeff):
        self.coeff = new_coeff

    def update_point_data(self):
        # return new information about the points after
        # changing of any among x coord, y coord, scale coefficient
        points = tuple(
            (self.coeff * px + self.fpos_x, self.coeff * py + self.fpos_y)
            for px, py in self.vertex_data['points']
        )
        return tuple(
            Point(point[0], point[1])
            for point in points
        )

    def init_vertex_data(self, input_file=INPUT_FILE):
        # getting the information about the figure
        if input_file:
            self.vertex_data = self.load_vertex_data(input_file)
        else:
            # remembering an old coefficient
            temp_coeff = self.coeff
            # setting coefficient to 1 (the default width of segment)
            self.update_coeff(1)
            # getting a data about vertices coordinates
            # -4 and 3 are the parameters that move figure to the centre of window
            self.vertex_data = self.create_vertex_data(-4, 3)
            # setting the remembered coefficient back
            self.update_coeff(temp_coeff)

    def create_vertex_data(self, x, y, write_to_file=WRITE_TO_FILE):
        # create data using the offsets from the start point (a0)
        a0 = Point(x, y)
        a1 = a0 + self.coeff
        a2 = a0.offset_x(self.coeff)
        a3 = a2.offset_y(-3 * self.coeff)
        a4 = a3.offset_x(3 * self.coeff)
        a5 = a3.offset_x(-self.coeff)
        a6 = a3.offset_y(self.coeff)
        a7 = a3.offset_y(-self.coeff)
        a8 = a4.offset_x(-1.5 * self.coeff)
        a9 = a8 - self.coeff
        a10 = a8.offset_y(-2 * self.coeff)
        a11 = a8.offset_x(self.coeff).offset_y(-self.coeff)
        a12 = a10 - self.coeff
        a13 = a12.offset_x(4 * self.coeff)
        a14 = a8.offset_x(2 * self.coeff)
        a15 = a14.offset_y(-2 * self.coeff)
        a16 = a15.offset_x(2 * self.coeff)
        a17 = a13.offset_x(2 * self.coeff)
        vertices = (a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17)
        # place data into dictionary
        vertex_data = {
            'points': [],
            "triangles":
            [
                [1, 0, 2],
                [2, 3, 4],
                [6, 5, 7],
                [11, 12, 13],
                [14, 8, 15]
            ],
            "quads":
            [
                [8, 9, 10, 11],
                [15, 13, 17, 16]
            ]
        }
        # write points coordinates to a list in a dictionary
        for vertex in vertices:
            vertex_data['points'].append(vertex.coordinates())
        # write information to .json file if necessary
        if write_to_file:
            with open('vertex_data.json', 'w') as fout:
                json.dump(vertex_data, fout)
        # return dictionary with information about the figure
        return vertex_data

    def load_vertex_data(self, file_in):
        # load information about the figure from the .json file if necessary
        with open(file_in, 'r') as fin:
            vertex_data = json.load(fin)
            # return dictionary with information about the figure
            return vertex_data
