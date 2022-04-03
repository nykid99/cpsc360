from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                                  # glut window number
width, height = 500, 500                                                    # window size

def refresh(width, height):
    glViewport(0, 0, width, height)                                         # specify viewport parameters
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(-0.5*width, 0.5*width, -0.5*height, 0.5*height, 0.0, 1.0)       # specify orthogonal projection view volume
    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric+view transf)
    glLoadIdentity()                                                        # reset transf matrix to an identity

def draw():                                                                 # draw() is called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                        # set display window color to yellow
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear display window
    glLoadIdentity()                                                        # reset transformations
    refresh(width, height)                                                  # reset transforms

    # draw a colored triangle
    glColor3f(0.2, 0.5, 0.4)                                                # set object color
    glBegin(GL_TRIANGLES)
    glVertex2f(-50.0, -100.0)                                               # v0
    glVertex2f(50.0, -100.0)                                                # v1
    glVertex2f(50.0, 0.0)                                                   # v2
    glEnd()

    glutSwapBuffers()                                                       # import for double-buffering

def main():
    glutInit()                                                              # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)  # set display mode
    glutInitWindowPosition(0, 0)                                            # set top-left display-window position
    glutInitWindowSize(width, height)                                       # set display-window size
    window = glutCreateWindow("cpsc 360")                                   # create window with title
    glutDisplayFunc(draw)                                                   # display everthing and wait
    glutMainLoop()  

main()