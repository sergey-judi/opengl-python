from Window import Window


if __name__ == '__main__':
    window1 = Window(512, 512, 'Lab1 Sergey Pereyaslavskiy', coeff=30, grid_coeff=30)
    window1.show()

# non-object-oriented implementation
"""width = 512
height = 512
midX = width / 2
midY = height / 2
coeff = 20
mx = 0
my = 0


def draw_line(point1, point2):
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    glVertex2f(point1.x, point1.y)
    glVertex2f(point2.x, point2.y)
    glEnd()


def draw_triangle(point1, point2, point3):
    glVertex2f(point1.x, point1.y)
    glVertex2f(point2.x, point2.y)
    glVertex2f(point3.x, point3.y)


def draw_rectangle(point1, point2, point3, point4):
    glVertex2f(point1.x, point1.y)
    glVertex2f(point2.x, point2.y)
    glVertex2f(point3.x, point3.y)
    glVertex2f(point4.x, point4.y)


def draw_polygons(x, y):
    a1 = Point(x, y)
    a2 = a1 + coeff
    a3 = a1.offset_x(coeff)
    a4 = a3.offset_y(-3 * coeff)
    a5 = a4.offset_x(3 * coeff)
    a6 = a4.offset_x(-coeff)
    a7 = a4.offset_y(coeff)
    a8 = a4.offset_y(-coeff)
    a9 = a5.offset_x(-1.5 * coeff)
    a10 = a9 - coeff
    a11 = a9.offset_y(-2 * coeff)
    a12 = a9.offset_x(coeff).offset_y(-coeff)
    a13 = a11 - coeff
    a14 = a13.offset_x(4 * coeff)
    a15 = a9.offset_x(2 * coeff)
    a16 = a15.offset_y(-2 * coeff)
    a17 = a16.offset_x(2 * coeff)
    a18 = a14.offset_x(2 * coeff)

    glBegin(GL_TRIANGLES)
    draw_triangle(a1, a2, a3)
    draw_triangle(a3, a4, a5)
    draw_triangle(a6, a7, a8)
    draw_triangle(a12, a13, a14)
    draw_triangle(a9, a16, a15)
    glEnd()

    glBegin(GL_QUADS)
    draw_rectangle(a9, a10, a11, a12)
    draw_rectangle(a14, a16, a17, a18)
    glEnd()


def display_figure():
    centreX = midX - 3.75*coeff
    centreY = midY + 2.5*coeff

    glClearColor(0, 0, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3d(1.0, 1.0, 0.0)
    draw_polygons(centreX, centreY)

    glLineWidth(2)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glColor3d(0.0, 0.0, 0.0)
    draw_polygons(centreX, centreY)

    glFinish()


def reshape(w, h):
    global width, height, midX, midY
    midX = w*midX/width
    midY = h*midY/height
    width = w
    height = h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, 0, h, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key, x, y):
    global midX, midY
    pressed_key = key.decode("utf-8")
    if pressed_key == ' ':
        midX = width/2
        midY = height/2
    if MOVEMENT_MODE:
        if pressed_key == 'w' or pressed_key == 's':
            if 0 < midX:
                midX -= coeff
        elif pressed_key == 'a' or pressed_key == 'd':
            if midX < width/2:
                midX += coeff
    else:
        if key.decode("utf-8") == 'w':
            if midY + 3*coeff < height:
                midY += coeff
        elif key.decode("utf-8") == 's':
            if midY - 3*coeff > 0:
                midY -= coeff
        elif key.decode("utf-8") == 'a':
            if midX - 3*coeff > 0:
                midX -= coeff
        elif key.decode("utf-8") == 'd':
            if midX + 3*coeff < width:
                midX += coeff
    glutPostRedisplay()


def motion_func(x, y):
    global midX, midY, mx, my
    dx = x - mx
    dy = y - my
    if 0 < midX+dx < width:
        midX += dx
    if 0 < midY-dy < height:
        midY -= dy
    mx = x
    my = y
    glutPostRedisplay()


def mouse_func(button, state, x, y):
    global mx, my
    mx = x
    my = y


def wheel_func(wheel, direction, x, y):
    global coeff
    if direction > 0 and coeff < 60:
        coeff += 10
    elif direction < 0 and coeff > 10:
        coeff -= 10
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Lab1 Figure")
    glutDisplayFunc(display_figure)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse_func)
    glutMotionFunc(motion_func)
    glutMouseWheelFunc(wheel_func)
    glutMainLoop()
"""

"""
def write_vertex_data(file_out='vertex_data.json'):
    vertex_data = {
        "points":
        [
            [-3.75, 2.5],   # a0
            [-2.75, 3.5],   # a1
            [-2.75, 2.5],   # a2
            [-2.75, -0.5],  # a3
            [0.25, -0.5],   # a4
            [-3.75, -0.5],  # a5
            [-2.75, 0.5],   # a6
            [-2.75, -1.5],  # a7
            [-1.25, -0.5],  # a8
            [-2.25, -1.5],  # a9
            [-1.25, -2.5],  # a10
            [-0.25, -1.5],  # a11
            [-2.25, -3.5],  # a12
            [1.75, -3.5],   # a13
            [0.75, -0.5],   # a14
            [0.75, -2.5],   # a15
            [2.75, -2.5],   # a16
            [3.75, -3.5]    # a17
        ],
        "triangles":
        [
            [0, 1, 2],
            [2, 3, 4],
            [5, 6, 7],
            [11, 12, 13],
            [8, 14, 15]
        ],
        "quads":
        [
            [8, 9, 10, 11],
            [13, 15, 16, 17]
        ]
    }
    with open(file_out, 'w') as fout:
        json.dump(vertex_data, fout)


def read_vertex_data(file_in='vertex_data.json'):
    with open(file_in, 'r') as fin:
        vertex_data = json.load(fin)
        # print(json.dumps(vertex_data, indent=4))
        return vertex_data
"""
