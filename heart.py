from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1.0, 1.0)
    glPointSize(13)
    glBegin(GL_LINES)
    glVertex2f(-500, 0)
    glVertex2f(500, 0)

    glVertex2f(0, -500)
    glVertex2f(0, 500)
    glEnd()
    heart_shape()
    glFlush()

def heart_shape():
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.0, 0.0)
    x = -1.139

    while(x <= 1.139):
        delta = np.cbrt(x*x) * np.sqrt(x*x) - 4*x*x + 4
        y1 = (np.cbrt(x*x) + np.sqrt(delta)) / 2
        y2 = (np.cbrt(x*x) - np.sqrt(delta)) / 2
         
        glVertex2f(x, y1)
        glVertex2f(x, y2)

        x += 0.001
    glEnd()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Heart Shape")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()


main()
