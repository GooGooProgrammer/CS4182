from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math, time
import ImportObject


class ring:
    obj = 0
    displayList = 0
    
    posX = 0.0
    posY = 0.0
    posZ = 0.0

    sizeX = 0.05
    sizeY = 0.05
    sizeZ = 0.05
    
    def __init__(self, x, z,y):
        self.obj = ImportObject.ImportedObject("./objects/ring")
        self.posX = x
        self.posZ = z
        self.posY = y
        
    def makeDisplayLists(self):
        self.obj.loadOBJ()

        self.displayList = glGenLists(1)
        glNewList(self.displayList, GL_COMPILE)
        self.obj.drawObject()
        glEndList()
    
    def draw(self):
        
        glPushMatrix()
        glTranslatef(self.posX,self.posY,self.posZ)
        glRotatef(90,1.0,0.0,0.0)
        glScalef(self.sizeX,self.sizeY,self.sizeZ)

        glCallList(self.displayList)
        glPopMatrix()
   
    
            
        
