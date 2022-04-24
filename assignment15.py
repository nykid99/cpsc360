from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                                                  # glut window number
width, height = 500, 500                                                    # window size

########################################### OpenGL Program ####################################################
def draw_tetrahedron():
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)                                                # right face
    glVertex3f(0, -10, -40)                                                 # a
    glVertex3f(20, -10, -80)                                                # b
    glVertex3f(0, 20, -60)                                                  # d 
    glColor3f(0.0, 1.0, 0.0)                                                # back face   
    glVertex3f(20, -10, -80)                                                # b
    glVertex3f(-20, -10, -80)                                               # c
    glVertex3f(0, 20, -60)                                                  # d
    glColor3f(0.0, 0.0, 1.0)                                                # left face
    glVertex3f(0, -10, -40)                                                 # a
    glVertex3f(0, 20, -60)                                                  # d
    glVertex3f(-20, -10, -80)                                               # c
    glColor3f(0.6, 0.2, 1.0)                                                # bottom face
    glVertex3f(0, -10, -40)                                                 # a
    glVertex3f(-20, -10, -80)                                               # c
    glVertex3f(20, -10, -80)                                                # b       
    glEnd()

def drawAxes():                                                             # draw x-axis and y-axis
    glLineWidth(3.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glColor3f(1.0, 0.0, 0.0)                                                # x-axis: red
    glVertex3f(0.0, 0.0, -99.0)                                             # v0
    glVertex3f(50.0, 0.0, -99.0)                                            # v1
    glColor3f(0.0, 1.0, 0.0)                                                # y-axis: green
    glVertex3f(0.0, 0.0, -99.0)                                             # v0
    glVertex3f(0.0, 50.0, -99.0)                                            # v1
    glEnd()

def refresh(width, height):
    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, width, height)                                         # specify viewport parameters
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
   
    gluPerspective(90.0, 1.0, 5.0, 100.0)                                   # perspective projection
    
    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric+view transf)
    glLoadIdentity()                                                        # reset transf matrix to an identity
    
def draw():                                                                 # This is the drawing function defined by you and called all the time
    glClearColor(1.0, 1.0, 0.0, 1.0)                                        # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)                      # clear display mode of display-window
    glLoadIdentity()                                                        # load an identity matrix
    refresh(width, height)                                                  # reset viweing and projection transforms for every iteration

    # viewing transformation
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)                                   # eyex,eyey,eyez,lookatx,lookaty,lookatz,upx,upy,upz                              
    
    # draw x,y axes
    drawAxes()

    # draw a tetrahedron for gluLookAt() examples
    draw_tetrahedron()

    # draw the cube
    glColor3f(0, 1, 0)
    glutSolidCube(5)

    glutSwapBuffers()                                                       # import for double-buffering

def main():
    glutInit()                                                              # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)  # set display mode of display-window
    glutInitWindowPosition(0, 0)                                            # set top-left display-window position
    glutInitWindowSize(width, height)                                       # set display-window size
    window = glutCreateWindow("cpsc360:A15 - TYPE YOUR NAME HERE")          # create window with title
    glutDisplayFunc(draw)                                                   # display graphic content and wait
    glutMainLoop()                                                          # must be called at last; display graphics and put program into infinite loop

main()