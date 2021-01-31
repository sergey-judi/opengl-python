from OpenGL.GL import *
from OpenGL.GLU import *
from IDrawable import IDrawable
from PIL import Image
from numpy import array


class Sphere(IDrawable):

    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        gl_new_sphere = gluNewQuadric()
        gluQuadricOrientation(gl_new_sphere, GLU_INSIDE)
        gluQuadricTexture(gl_new_sphere, GL_TRUE)
        gluQuadricDrawStyle(gl_new_sphere, GLU_FILL)
        glColor3d(1, 1, 1)
        gluSphere(gl_new_sphere, self.radius, 20, 20)
        gluDeleteQuadric(gl_new_sphere)
        glDisable(GL_TEXTURE_2D)

    def get_point_data(self):
        pass

    def load_texture(self, filename):
        print('Trying to open', filename)
        try:
            image = Image.open(filename)
        except IOError as ex:
            print('IOError: failed to open texture file')
            return -1
        print('Opened file: size =', image.size, 'format =', image.format)
        image_data = array(list(image.getdata()))
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
        image.close()
