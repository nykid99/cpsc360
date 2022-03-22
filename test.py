import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

print("Import successful!")

width, height = 500,500

# ---Section 1---
def square():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(100, 100) # Coordinates for the bottom left point
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(200, 100) # Coordinates for the bottom right point
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(200, 200) # Coordinates for the top right point
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(100, 200) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

def polygon():
    glBegin(GL_POLYGON)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(20.0, 20.0, 0.0)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(80.0, 20.0, 0.0)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(80.0, 80.0, 0.0)
    glColor3f(1.0,1.0,0.0)
    glVertex3f(20.0, 80.0, 0.0)
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glOrtho(-100.0, 100.0, -100.0, 100.0, -100.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity

# ---Section 2---

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    refresh2d(width, height)

    #square() # Draw a square using our function
    polygon()
    glColor3f(1.0, 0.0, 0.0)
    glutWireSphere(50.0, 10, 10)

    glutSwapBuffers()

#---Section 3---  
def main():  
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE) # Set the display mode to be colored
    glutInitWindowSize(width, height)   # Set the w and h of your window
    glutInitWindowPosition(200, 200)   # Set the position at which this windows should appear
    wind = glutCreateWindow("OpenGL Coding Practice") # Set a window title
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen) # Keeps the window open
    print("ALL success!")
    glutMainLoop()  # Keeps the above created window displaying/running in a loop

main()