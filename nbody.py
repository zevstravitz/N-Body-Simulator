from graphics import *
import time
import math
import numpy as np

#CONSTANTS
TIMESTEP = 1/100
FRAMERATE = 1
BODIES = 4
HEIGHT = 800
WIDTH = 1200
SIZE = 3
VEL = 10
MASS = 5
G_CONSTANT = 3

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
            acc_vec = [0,0]
            for j in range(BODIES):
                if i == j:
                    continue
                dx = self.particles[j].x-self.particles[i].x
                dy = self.particles[j].y-self.particles[i].y
                dist = math.sqrt(dy**2 + dx**2)
                unit_vector = [divide(dx, dist), divide(dy, dist)]
                acc = G_CONSTANT*divide((self.particles[i].mass * self.particles[j].mass),(dist**2))

                self.particles[i].ax += acc*unit_vector[0]
                self.particles[i].ay += acc*unit_vector[1]

            self.particles[i].vx -= self.particles[i].ax
            self.particles[i].vy += self.particles[i].ay

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
        bodies._update_velocities()
    win.getMouse()
    win.close()
