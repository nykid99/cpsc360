from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                                  # glut window number
width, height = 500, 500                                                    # window size

########################################### Lecture examples ####################################################
def drawPoints():
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10.0)                                                       # specify point size (1.0 default)
    glBegin(GL_POINTS)
    glVertex3f(50.0, 50.0, 0.0)                                             # v0
    glVertex3f(450.0, 50.0, 0.0)                                            # v1
    glVertex3f(450.0, 450.0, 0.0)                                           # v2
    glVertex3f(50.0, 450.0, 0.0)                                            # v3
    glEnd()

def drawLines():
    glColor3f(0.2, 0.5, 0.4)
    glLineWidth(5.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glVertex3f(50.0, 50.0, 0.0)                                             # v0
    glVertex3f(450.0, 50.0, 0.0)                                            # v1
    glVertex3f(450.0, 450.0, 0.0)                                           # v2
    glVertex3f(50.0, 450.0, 0.0)                                            # v3
    glEnd()

def drawTriangles():
    glColor3f(0.2, 0.5, 0.4)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)                               # replace GL_FILL with GL_LINE
    glBegin(GL_TRIANGLES)                                                   # replace GL_TRIANGLES with GL_TRIANGLE_STRIP
    glVertex2f(20.0, 50.0)                                                  # v0
    glVertex2f(220.0, 50.0)                                                 # v1
    glVertex2f(120.0, 250.0)                                                # v2
    glVertex2f(250.0, 100.0)                                                # v3
    glVertex2f(350.0, 300.0)                                                # v4
    glVertex2f(450.0, 100.0)                                                # v5
    glEnd()

def drawPolygon():
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)                               # color can also be specified for each vertex
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)                                                # red
    glVertex3f(50.0, 50.0, 0.0)                                             # v0
    glColor3f(0.0, 1.0, 0.0)                                                # green
    glVertex3f(250.0, 50.0, 0.0)                                            # v1
    glColor3f(0.0, 0.0, 1.0)                                                # blue
    glVertex3f(250.0, 250.0, 0.0)                                           # v2
    glColor3f(0.6, 0.2, 1.0)                                                # purple
    glVertex3f(50.0, 250.0, 0.0)                                            # v3
    glEnd()

########################################### Exercise 1: Point and Lines ####################################################
def exercise1_Points():
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10.0)                                                       # specify point size (1.0 default)
    glBegin(GL_POINTS)
    glVertex3f(50.0, 50.0, 0.0)                                             # v0
    glVertex3f(150.0, 350.0, 0.0)                                           # v1
    glVertex3f(250.0, 50.0, 0.0)                                            # v2
    glVertex3f(350.0, 350.0, 0.0)                                           # v3
    glVertex3f(450.0, 50.0, 0.0)                                            # v4
    glEnd()

def exercise1_Linestrip():
    glColor3f(0.2, 0.5, 0.4)
    glLineWidth(5.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINE_STRIP)
    glVertex3f(50.0, 50.0, 0.0)                                             # v0
    glVertex3f(150.0, 350.0, 0.0)                                           # v1
    glVertex3f(250.0, 50.0, 0.0)                                            # v2
    glVertex3f(350.0, 350.0, 0.0)                                           # v3
    glVertex3f(450.0, 50.0, 0.0)                                            # v4
    glEnd()

def exercise1():
    # draw the points
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10.0)
    # TODO: write your code below 

    # draw the line_strip
    glColor3f(0.2, 0.5, 0.4)
    glLineWidth(5.0)  
    # TODO: write your code below


########################################### Exercise 2: Triangles ####################################################
def exercise2_triangles():
    glColor3f(0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLES)
    glVertex3f(150.0, 50.0, 0.0)                                            # v0
    glVertex3f(350.0, 50.0, 0.0)                                            # v1
    glVertex3f(150.0, 450.0, 0.0)                                           # v3
    glVertex3f(350.0, 50.0, 0.0)                                            # v1
    glVertex3f(350.0, 450.0, 0.0)                                           # v2
    glVertex3f(150.0, 450.0, 0.0)                                           # v3
    glEnd()

def exercise2_trianglestrip():
    glColor3f(0.0, 0.0, 0.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex3f(150.0, 50.0, 0.0)                                            # v0
    glVertex3f(350.0, 50.0, 0.0)                                            # v1
    glVertex3f(150.0, 450.0, 0.0)                                           # v3
    glVertex3f(350.0, 450.0, 0.0)                                           # v2
    glEnd()

def exercise2():
    # draw the rectangle
    glColor3f(0.2, 0.5, 0.4)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)                               # color can also be specified for each vertex
    glBegin(GL_POLYGON)
    glVertex3f(150.0, 50.0, 0.0)                                            # v0
    glVertex3f(350.0, 50.0, 0.0)                                            # v1
    glVertex3f(350.0, 450.0, 0.0)                                           # v2
    glVertex3f(150.0, 450.0, 0.0)                                           # v3
    glEnd()

    # draw the vertices
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex3f(150.0, 50.0, 0.0)                                            # v0
    glVertex3f(350.0, 50.0, 0.0)                                            # v1
    glVertex3f(350.0, 450.0, 0.0)                                           # v2
    glVertex3f(150.0, 450.0, 0.0)                                           # v3
    glEnd()

    # triangulate the rectangle to express it with two triangles 
    #   using GL_TRIANGLES or GL_TRIANGLE_STRIP
    # TODO: write you code below


########################################### OpenGL Program ####################################################
def refresh(width, height):
    glViewport(0, 0, width, height)                                         # specify viewport parameters
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(0, 500, 0, 500, 0.0, 1.0)                                       # specify orthogonal projection view volume
    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric+view transf)
    glLoadIdentity()                                                        # reset transf matrix to an identity
    
def draw():                                                                 # This is the drawing function defined by you and called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                        # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear display mode of display-window
    glLoadIdentity()                                                        # load an identity matrix
    refresh(width, height)                                                  # reset viweing and projection transforms for every iteration

    # draw points
    drawPoints()

    # draw lines
    #drawLines()

    # exercise1
    #exercise1()

    # draw triangles
    #drawTriangles()

    # draw polygon
    #drawPolygon()

    # exercise2
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