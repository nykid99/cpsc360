from turtle import heading, width
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                  # glut window number
width, height = 500, 400                                    # window size

def draw_rectangle(x, y, width, height):
    glBegin(GL_QUADS)                                       # start drawing a rectangle
    glVertex2f(x, y)                                        # bottom-left point
    glVertex2f(x + width, y)                                # bottom-right point
    glVertex2f(x + width, y + height)                       # top-right point
    glVertex2f(x, y + height)                               # top-left point
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw():                                                 # draw() is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)      # clear the screen
    glLoadIdentity()                                        # reset transformations
    refresh2d(width, height)                                # set mode to 2D

    # TODO draw rectangle
    glColor3f(0.0, 0.0, 1.0)                                # set color to blue
    draw_rectangle(10, 10, 200, 100)                        # bottom-left at (10,10) with width=200, height=100

    glutSwapBuffers()                                       # import for double-buffering

# initialization
glutInit()                                                  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                           # set window size
glutInitWindowPosition(0, 0)                                # set the window position
window = glutCreateWindow("cpsc 360")                       # create window with title
glutDisplayFunc(draw)                                       # set draw function callback
glutIdleFunc(draw)                                          # draw all the time
glutMainLoop()                                              # start everything

