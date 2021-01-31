from math import sin, cos, pi


class Light:

    def __init__(self):
        self.pos_x = self.pos_y = self.pos_z = 0
        self.satellite_pos_x = self.satellite_pos_y = self.satellite_pos_z = 0
        self.distance = 400
        self.satellite_distance = 40
        self.phi = 0.0
        self.theta = 90.0
        self.satellite_phi = 0.0
        self.satellite_theta = 90.0
        self.moving = False
        self.moving_satellite = False
        self.calculate_light_position()

    def calculate_light_position(self):
        self.pos_x, self.pos_y, self.pos_z = self.calculate_xyz(self.distance, self.phi, self.theta)
        self.calculate_satellite_position()

    def calculate_satellite_position(self):
        self.satellite_pos_x, self.satellite_pos_y, self.satellite_pos_z = \
            self.calculate_xyz(self.satellite_distance, self.satellite_theta, self.satellite_phi)

    def calculate_xyz(self, radius, angle_phi, angle_theta):
        x = radius * sin(angle_theta * pi / 180) * cos(angle_phi * pi / 180)
        y = radius * sin(angle_theta * pi / 180) * sin(angle_phi * pi / 180)
        z = radius * cos(angle_theta * pi / 180)
        return x, y, z
