# Testing template for Particle class
import simplegui
import random
Width = 400
Height = 500
Particle_Radius = 5
Color_List = ["red","black","white","blue"]
Direction_Choice = [[1,0],[-1,0],[0,1],[0,-1]]

###################################################
# Student should add code for the Particle class here
class Particle:
    def __init__(self,position,color):
        self.position = position
        self.color = color
    def move(self,offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]
    def draw(self,canvas):
        canvas.draw_circle(self.position, Particle_Radius, 1, random.choice(Color_List))
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color
###################################################
# Test code for the Particle class

def draw_circle(canvas):
    for p in Particle_List:
        p.move(random.choice(Direction_Choice))
    for p in Particle_List:
        p.draw(canvas)




frame = simplegui.create_frame('Testing', Width, Height)
frame.set_draw_handler(draw_circle)
Particle_List = []
for i in range(50):
    p = Particle([Width/2,Height/2],random.choice(Color_List))
    Particle_List.append(p)



frame.start()