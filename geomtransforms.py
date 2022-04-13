from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                                  # glut window number
width, height = 500, 500                                                    # window size

########################################### Lecture examples ####################################################
def example_initTeapot():
    glColor3f(0.0, 0.0, 0.0)                                                # specify object color
    glLineWidth(1.0)                                                        # reset line width to 1.0
    glutWireTeapot(50.0)                                                    # draw a teaport of size 50 in wireframe mode

def example_translate():
    glTranslatef(100.0, 100.0, 0.0)                                         # construct translation matrix with a translation vector
    glColor3f(0.2, 0.5, 0.4)                                                # draw the transformed teaport in green
    glutWireTeapot(50.0)

def example_scale():
    glScalef(2.0, 2.0, 2.0)                                                 # construct scaling matrix with three scaling factors
    glColor3f(0.2, 0.5, 0.4)                                                # draw the transformed teaport in green
    glutWireTeapot(50.0)

def example_rotate():
    glRotatef(90.0, 0.0, 0.0, 1.0)                                          # construct rotation matrix along z-axis (0,0,1)
    glColor3f(0.2, 0.5, 0.4)                                                # draw the transformed teaport in green
    glutWireTeapot(50.0)

def example_rotate_tranlate():                                              # rotate then translate
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3f(0.2, 0.5, 0.4)
    glBegin(GL_TRIANGLES)                                                   # draw the initial triangle
    glVertex3f(-25.0, -25.0, 0.0)
    glVertex3f(25.0, -25.0, 0.0)
    glVertex3f(0.0, 50.0, 0.0)
    glEnd()

    glTranslatef(100.0, 100.0, 0.0)                                         # M1: translate
    glRotatef(90.0, 0.0, 0.0, 1.0)                                          # M2: rotate along z-axis (0,0,1)
    
    glColor3f(1.0, 0.0, 0.0)                                                # draw the transformed triangle
    glBegin(GL_TRIANGLES)
    glVertex3f(-25.0, -25.0, 0.0)
    glVertex3f(25.0, -25.0, 0.0)
    glVertex3f(0.0, 50.0, 0.0)
    glEnd()

def example_tranlate_rotate():                                              # translate then rotate
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3f(0.2, 0.5, 0.4)
    glBegin(GL_TRIANGLES)                                                   # draw the initial triangle
    glVertex3f(-25.0, -25.0, 0.0)
    glVertex3f(25.0, -25.0, 0.0)
    glVertex3f(0.0, 50.0, 0.0)
    glEnd()

    glRotatef(90.0, 0.0, 0.0, 1.0)                                          # M1: rotate along x-axis (0,0,1)
    glTranslatef(100.0, 100.0, 0.0)                                         # M2: translate
    
    glColor3f(1.0, 0.0, 0.0)                                                # draw the transformed triangle
    glBegin(GL_TRIANGLES)
    glVertex3f(-25.0, -25.0, 0.0)
    glVertex3f(25.0, -25.0, 0.0)
    glVertex3f(0.0, 50.0, 0.0)
    glEnd()   

def example_partialdisk():
    glColor3f(0.2, 0.5, 0.4)
    gluPartialDisk(gluNewQuadric(), 0.0, 50.0, 32, 32, 0.0, 45.0)

########################################### Exercise ####################################################
# Exercise 1
def exercise1():
    # TODO: comment out "example_initTeapot()" in draw()
    # TODO: write your code below to scale the object 


    # draw the square using GL_LINE_LOOP
    glColor3f(0.2, 0.5, 0.4)
    glLineWidth(5.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINE_LOOP)                                                   # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glVertex3f(50.0, 0.0, 0.0)                                              # v0
    glVertex3f(0.0, 50.0, 0.0)                                              # v1
    glVertex3f(-50.0, 0.0, 0.0)                                             # v2
    glVertex3f(0.0, -50.0, 0.0)                                             # v3
    glEnd()

def exercise1_solution():
    # TODO: comment out "example_initTeapot()" in draw()
    # TODO: write your code below to scale the object 
    glScalef(1.0, 2.0, 1.0)

    # draw the square using GL_LINE_LOOP
    glColor3f(0.2, 0.5, 0.4)
    glLineWidth(5.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINE_LOOP)                                                   # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glVertex3f(50.0, 0.0, 0.0)                                              # v0
    glVertex3f(0.0, 50.0, 0.0)                                              # v1
    glVertex3f(-50.0, 0.0, 0.0)                                             # v2
    glVertex3f(0.0, -50.0, 0.0)                                             # v3
    glEnd()

# Exercise 2
def exercise2():
    # draw a green partial-disk
    glColor3f(0.2, 0.5, 0.4)
    gluPartialDisk(gluNewQuadric(), 0.0, 50.0, 32, 32, 0.0, 45.0)

    # TODO: write your code BELOW to create the red disk


def exercise2_solution():
    # draw a green partial-disk
    glColor3f(0.2, 0.5, 0.4)
    gluPartialDisk(gluNewQuadric(), 0.0, 50.0, 32, 32, 0.0, 45.0)

    # TODO: write your code BELOW to create the red disk
    glRotatef(-45.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)
    gluPartialDisk(gluNewQuadric(), 0.0, 50.0, 32, 32, 0.0, 45.0)

########################################### OpenGL Program ####################################################
def drawAxes():                                                             # draw x-axis and y-axis
    glLineWidth(3.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glColor3f(1.0, 0.0, 0.0)                                                # x-axis: red
    glVertex3f(0.0, 0.0, -5.0)                                               # v0
    glVertex3f(100.0, 0.0, -5.0)                                             # v1
    glColor3f(0.0, 1.0, 0.0)                                                # y-axis: green
    glVertex3f(0.0, 0.0, -5.0)                                               # v0
    glVertex3f(0.0, 100.0, -5.0)                                             # v1
    glEnd()

def refresh(width, height):
    glViewport(0, 0, width, height)                                         # specify viewport parameters
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(-250.0, 250.0, -250.0, 250.0, -100.0, 100.0)                    # specify orthogonal projection view volume
    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric+view transf)
    glLoadIdentity()                                                        # reset transf matrix to an identity
    
def draw():                                                                 # This is the drawing function defined by you and called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                        # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear display mode of display-window
    glLoadIdentity()                                                        # load an identity matrix
    refresh(width, height)                                                  # reset viweing and projection transforms for every iteration

    # draw x,y axes
    drawAxes()
    
    # initial teapot in black at origin 
    example_initTeapot()

    # geometric transformation
    #example_translate()                                                    # translation
    #example_scale()                                                        # scale
    #example_rotate()                                                       # rotation
    #example_rotate_tranlate()
    #example_tranlate_rotate()

    #exercise1()
    #exercise2()

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