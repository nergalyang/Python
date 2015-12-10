# Partial example code for Spaceship

import simplegui
import math
Width=800
Height=600
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# sound assets purchased from sounddogs.com, please do not redistribute
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")

def angle_to_vector(ang):
    return [10*math.cos(ang), 10*math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [130, 45], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    def update(self):
        self.angle+=self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % Width
        self.pos[1] = (self.pos[1] + self.vel[1]) % Height

        press_key = 0.15 / 60
        release_key = 0.10
        self.vel[0] *= (1 - press_key)
        self.vel[1] *= (1 - press_key)

        if self.thrust:
            forward = angle_to_vector(self.angle)
            self.vel[0] += release_key * forward[0]
            self.vel[1] += release_key * forward[1]
    def change_thrust(self,a):
        self.thrust = a
    def increase_angvel(self):
        self.angle_vel += .04

    def decrease_angvel(self):
        self.angle_vel -= .04
        
def down(key):
    if key == simplegui.KEY_MAP['left']:
        Nergal.decrease_angvel()
    elif key == simplegui.KEY_MAP['right']:
        Nergal.increase_angvel()
    elif key == simplegui.KEY_MAP['up']:
        Nergal.change_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        Nergal.shoot()

def up(key):
    if key == simplegui.KEY_MAP['left']:
        Nergal.increase_angvel()
    elif key == simplegui.KEY_MAP['right']:
        Nergal.decrease_angvel()
    elif key == simplegui.KEY_MAP['up']:
        Nergal.change_thrust(False)
    
def draw(canvas):
    Nergal.draw(canvas)
    Nergal.update()
    
    
    
frame = simplegui.create_frame("Nadesico", Width, Height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(down)
frame.set_keyup_handler(up)
Nergal = Ship([Width/2, Height/2], [0, 0], 0, ship_image, ship_info)
frame.set_canvas_background("Black")
frame.start()