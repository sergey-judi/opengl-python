from math import sin, cos, pi


class Surface:

    def __init__(self):
        self.x_bound = 500
        self.y_bound = 500
        self.step_x = 20
        self.step_y = 20
        self.point_array = []
        self.get_point_data()

    @staticmethod
    def function(x, y):
        return 50*(sin(x * pi / 180) + cos(y * pi / 180))

    def get_point_data(self):
        self.compute_points_up_y(self.x_bound, self.y_bound, self.step_x, self.step_y, swap=False)
        self.compute_points_up_y(self.y_bound, self.x_bound, self.step_y, self.step_x, swap=True)

    def compute_points_up_z(self, x_bound, y_bound, step_x, step_y, swap=False):
        x = -x_bound
        while x != x_bound + step_x:
            y = -y_bound
            while y != y_bound:
                y += step_y
                if not swap:
                    z = self.function(x, y)
                    self.point_array.append([x, y, z])
                else:
                    z = self.function(y, x)
                    self.point_array.append([y, x, z])
            x += step_x
        x = -x_bound
        while x != x_bound + step_x:
            y = y_bound
            while y != -y_bound:
                y -= step_y
                if not swap:
                    z = self.function(x, y)
                    self.point_array.append([x, y, z])
                else:
                    z = self.function(y, x)
                    self.point_array.append([y, x, z])
            x += step_x

    def compute_points_up_y(self, x_bound, z_bound, step_x, step_z, swap=False):
        x = -x_bound
        while x != x_bound + step_x:
            z = -z_bound
            while z != z_bound:
                z += step_z
                if not swap:
                    y = self.function(x, z)
                    self.point_array.append([x, y, z])
                else:
                    y = self.function(z, x)
                    self.point_array.append([z, y, x])
            x += step_x
        x = -x_bound
        while x != x_bound + step_x:
            z = z_bound
            while z != -z_bound:
                z -= step_z
                if not swap:
                    y = self.function(x, z)
                    self.point_array.append([x, y, z])
                else:
                    y = self.function(z, x)
                    self.point_array.append([z, y, x])
            x += step_x
