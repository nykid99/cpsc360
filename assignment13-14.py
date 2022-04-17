from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                                  # glut window number
width, height = 500, 500                                                    # window size

########################################### Assignment ####################################################
def question1a():
    # draw the rectangle
    glColor3f(0.2, 0.5, 0.4)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)                               # color can also be specified for each vertex
    glBegin(GL_POLYGON)
    glVertex3f(-100.0, -200.0, 0.0)                                         # v0
    glVertex3f(100.0, -200.0, 0.0)                                          # v1
    glVertex3f(100.0, 200.0, 0.0)                                           # v2
    glVertex3f(-100.0, 200.0, 0.0)                                          # v3
    glEnd()

    # draw the vertices
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex3f(-100.0, -200.0, 0.0)                                         # v0
    glVertex3f(100.0, -200.0, 0.0)                                          # v1
    glVertex3f(100.0, 200.0, 0.0)                                           # v2
    glVertex3f(-100.0, 200.0, 0.0)                                          # v3
    glEnd()

    #TODO: write your code below to draw 8 triangles 
    #        to triangulte the rectangle with GL_LINE



    print("assignment 13&14-1a")

def question1b():
    # draw the rectangle
    glColor3f(0.2, 0.5, 0.4)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)                               # color can also be specified for each vertex
    glBegin(GL_POLYGON)
    glVertex3f(-100.0, -200.0, 0.0)                                         # v0
    glVertex3f(100.0, -200.0, 0.0)                                          # v1
    glVertex3f(100.0, 200.0, 0.0)                                           # v2
    glVertex3f(-100.0, 200.0, 0.0)                                          # v3
    glEnd()

    # draw the vertices
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex3f(-100.0, -200.0, 0.0)                                         # v0
    glVertex3f(100.0, -200.0, 0.0)                                          # v1
    glVertex3f(100.0, 200.0, 0.0)                                           # v2
    glVertex3f(-100.0, 200.0, 0.0)                                          # v3
    glEnd()

    #TODO: write your code below to draw 8 triangles 
    #       to triangulte the rectangle with GL_FILL



    print("assignment 13&14-1b")

def question2():
    # The first partial-disk of 60 degrees in RED
    glColor3f(1.0, 0.0, 0.0)                                                # disk0
    gluPartialDisk(gluNewQuadric(), 0.0, 50.0, 32, 32, 0.0, 60.0)

    # TODO: write your code BELOW to create another 5 partial-disks
    #        to complete the full disk by rotating the first one


    print("assignment 13&14-2")

def question3a():
    # initial green triangle
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3f(0.2, 0.5, 0.4)
    glBegin(GL_TRIANGLES)
    glVertex3f(-25.0, -25.0, 0.0)
    glVertex3f(25.0, -25.0, 0.0)
    glVertex3f(0.0, 50.0, 0.0)
    glEnd()

    # TODO: write your code BELOW for the transformed triangle in RED
    

    print("assignment 13&14-3a")

def question3b():
    # initial green triangle
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3f(0.2, 0.5, 0.4)
    glBegin(GL_TRIANGLES)
    glVertex3f(-25.0, -25.0, 0.0)
    glVertex3f(25.0, -25.0, 0.0)
    glVertex3f(0.0, 50.0, 0.0)
    glEnd()

    # TODO: write your code BELOW for the transformed triangle in RED


    print("assignment 13&14-3b")

########################################### OpenGL Program ####################################################
def refresh(width, height):
    glViewport(0, 0, width, height)                                         # specify viewport parameters
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(-250.0, 250.0, -250.0, 250.0, -100.0, 100.0)                    # specify orthogonal projection view volume
    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric+view transf)
    glLoadIdentity()                                                        # reset transf matrix to an identity

def drawAxes():                                                             # draw x-axis and y-axis
    glLineWidth(3.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glColor3f(1.0, 0.0, 0.0)                                                # x-axis: red
    glVertex3f(0.0, 0.0, -5.0)                                              # v0
    glVertex3f(100.0, 0.0, -5.0)                                            # v1
    glColor3f(0.0, 1.0, 0.0)                                                # y-axis: green
    glVertex3f(0.0, 0.0, -5.0)                                              # v0
    glVertex3f(0.0, 100.0, -5.0)                                            # v1
    glEnd()

def draw():                                                                 # This is the drawing function defined by you and called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                        # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear display mode of display-window
    glLoadIdentity()                                                        # load an identity matrix
    refresh(width, height)                                                  # reset viweing and projection transforms for every iteration

    drawAxes()                                                              # draw x,y axes

    # To show the result for one quesiton at a time, 
    #    comment out the function of the other question

    # assignment 13&14-1
    # TODO write your code in the function below
    question1a()

    # TODO write your code in the function below
    #question1b()

    # assignment 13&14-2
    # TODO write your code in the function below
    #question2()

    # assignment 13&14-3
    # TODO write your code in the function below
    #question3a()

    # TODO write your code in the function below
    #question3b()

    glutSwapBuffers()                                                       # import for double-buffering

def main():
    glutInit()                                                              # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)  # set display mode of display-window
    glutInitWindowPosition(0, 0)                                            # set top-left display-window position
    glutInitWindowSize(width, height)                                       # set display-window size
    window = glutCreateWindow("cpsc360:A13-14 - TYPE YOUR NAME HERE")        # create window with title
    glutDisplayFunc(draw)                                                   # display graphic content and wait
    glutMainLoop()                                                          # must be called at last; display graphics and put program into infinite loop

main()