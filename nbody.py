from graphics import *
import time
import random
import math

#CONSTANTS
TIMESTEP = 1/100
FRAMERATE = 20
BODIES = 3
HEIGHT = 800
WIDTH = 1200
SIZE = 3
VEL = 100
MASS = 5
G_CONSTANT = 30

class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.vx = random.randint(-VEL, VEL)
        self.y = random.randint(0, HEIGHT)
        self.vy = random.randint(-VEL, VEL)
        self.mass = random.randint(MASS, MASS * 5)
        self.size = self.mass / MASS * SIZE

    def _update_particle_pos(self):
        self.x = self.x + self.vx * FRAMERATE
        self.y = self.y + self.vy * FRAMERATE

class Particles:
    def __init__(self):
        self.particles = []
        for i in range(BODIES):
            self.particles.append(Particle())

    def _update_velocities(self):
        for i in range(BODIES):
            for j in range(BODIES):
                if i == j:
                    continue
                dx = self.particles[j].x-self.particles[i].x
                dy = self.particles[j].y-self.particles[i].y
                dist = math.sqrt(dy**2 + dx**2)
                unit_vector = [divide(dx, dist), divide(dy, dist)]
                acc = G_CONSTANT*divide((self.particles[i].mass * self.particles[j].mass),(dist**2))
                self.particles[i].vx += acc*unit_vector[0]
                self.particles[i].vy += acc*unit_vector[1]
                self.particles[j].vx += acc*unit_vector[0]
                self.particles[j].vy += acc*unit_vector[1]

def divide(num, den):
    if den == 0:
        return 0
    return num/den

if __name__ == "__main__":
    win = GraphWin("N Body Simulator", WIDTH, HEIGHT)
    win.setBackground("gray")
    bodies = Particles()
    array_of_circles = []
    for i in range(BODIES):
        b = Circle(Point(bodies.particles[i].x,bodies.particles[i].y), bodies.particles[i].size)
        b.setOutline('blue')
        b.setFill('black')
        array_of_circles.append(b)
        b.draw(win)

    while (True):
        for i in range(BODIES):
            array_of_circles[i].move(bodies.particles[i].vx, bodies.particles[i].vy)
        time.sleep(TIMESTEP)
        #print(bodies.particles[1].vx)
        bodies._update_velocities()
    win.getMouse()
    win.close()
