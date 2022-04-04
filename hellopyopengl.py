from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                                  # glut window number
width, height = 500, 500                                                    # window size

def refresh(width, height):
    glViewport(0, 0, width, height)                                         # specify viewport parameters
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(0, 400, 0, 400, 0.0, 1.0)                                       # specify orthogonal projection view volume
    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric+view transf)
    glLoadIdentity()                                                        # reset transf matrix to an identity

def draw():                                                                 # This is the drawing function defined by you and called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                        # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear display mode of display-window
    glLoadIdentity()                                                        # load an identity matrix
    refresh(width, height)                                                  # reset viweing and projection transforms for every iteration

    # draw a green triangle
    glColor3f(0.2, 0.5, 0.4)                                                # set object color
    glBegin(GL_TRIANGLES)                                                   # OpenGL primitive: triangle
    glVertex2f(50.0, 50.0)                                                  # v0
    glVertex2f(250.0, 50.0)                                                 # v1
    glVertex2f(150.0, 250.0)                                                # v2
    glEnd()

    # draw a red triangle
    glColor3f(0.8, 0.2, 0.1)                                                # set object color
    glBegin(GL_TRIANGLES)                                                   # OpenGL primitive: triangle
    glVertex2f(250.0, 100.0)                                                # v0
    glVertex2f(450.0, 100.0)                                                # v1
    glVertex2f(350.0, 300.0)                                                # v2
    glEnd()

    glutSwapBuffers()                                                       # import for double-buffering

def main():
    glutInit()                                                              # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)  # set display mode of display-window
    glutInitWindowPosition(0, 0)                                            # set top-left display-window position
    glutInitWindowSize(width, height)                                       # set display-window size
    window = glutCreateWindow("cpsc 360")                                   # create window with title
    glutDisplayFunc(draw)                                                   # display graphic content and wait
    glutMainLoop()                                                          # must be called at last; display graphics and put program into infinite loop

main()