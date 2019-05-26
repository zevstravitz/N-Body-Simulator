from graphics import *
import time
import math
import numpy as np

#CONSTANTS
TIMESTEP = 0.00
FRAMERATE = 1
BODIES = 3
HEIGHT = 800
WIDTH = 1200
SIZE = 3
VEL = 1
MASS = 2
G_CONSTANT = 100

class Particle:
    def __init__(self):
        self.x = np.random.uniform(0, WIDTH, 1)[0]
        self.vx = np.random.uniform(-VEL, VEL, 1)[0]
        self.y = np.random.uniform(0, HEIGHT, 1)[0]
        self.vy = np.random.uniform(-VEL, VEL, 1)[0]
        self.ax = 0
        self.ay = 0
        self.mass = np.random.uniform(MASS, MASS * 5, 1)[0]
        self.size = self.mass / MASS * SIZE

class Particles:

    def __init__(self):
        self.particles = []
        for i in range(BODIES):
            self.particles.append(Particle())

    def _update_velocities(self):
        for i in range(BODIES):
            self.particles[i].ax = 0
            self.particles[i].ay = 0
            for j in range(BODIES):
                if i == j:
                    continue
                dx = self.particles[j].x-self.particles[i].x
                dy = self.particles[j].y-self.particles[i].y
                dist = math.sqrt(dy**2 + dx**2)
                unit_vector = [dx/dist, dy/dist]
                acc = G_CONSTANT*divide((self.particles[i].mass * self.particles[j].mass),(dist**2), dist)
                self.particles[i].ax += acc*unit_vector[0]
                self.particles[i].ay += acc*unit_vector[1]

            self.particles[i].vx += self.particles[i].ax * FRAMERATE
            self.particles[i].vy += self.particles[i].ay * FRAMERATE

    def _update_particle_pos(self):
        for i in range(BODIES):
            self.particles[i].x += self.particles[i].vx
            self.particles[i].y += self.particles[i].vy
            array_of_circles[i].move(bodies.particles[i].vx, bodies.particles[i].vy)

def divide(num, den, dis):
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
        bodies._update_velocities()
        bodies._update_particle_pos()
        time.sleep(TIMESTEP)

    win.getMouse()
    win.close()
