from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                              # glut window number
width, height = 500, 500                                                # window size

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw():                                                             # draw() is called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                    # set display-window color to yellow
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                  # clear display window
    glLoadIdentity()                                                    # reset transformations
    refresh2d(width, height)                                            # set mode to 2D

    glColor3f(0.2, 0.5, 0.4)                                            # set object color
    # draw points
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(100, 100)                                                # first point (x1, y1)
    glVertex2f(300, 200)                                                # second point (x2, y2)
    glEnd()

    # draw quads
    glBegin(GL_QUADS)
    glVertex2f(100.0, 100.0)                                            # bottom-left point
    glVertex2f(300.0, 100.0)                                            # bottom-right point
    glVertex2f(300.0, 200.0)                                            # top-right point
    glVertex2f(100.0, 200.0)                                            # top-left point
    glEnd()

    # draw triangles
    glBegin(GL_TRIANGLES)
    glVertex2f(100.0, 210.0)                                            # v0
    glVertex2f(300.0, 210.0)                                            # v1
    glVertex2f(300.0, 310.0)                                            # v2
    glEnd()

    glutSwapBuffers()                                                   # import for double-buffering

# initialization
glutInit()                                                              # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)  # set display mode
glutInitWindowPosition(0, 0)                                            # set top-left display-window position
glutInitWindowSize(width, height)                                       # set display-window size
window = glutCreateWindow("cpsc 360")                                   # create window with title
glutDisplayFunc(draw)                                                   # display everthing and wait
glutMainLoop()  