import circleshape
from constants import *
import pygame
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.width = 2
    def draw (self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius,self.width)
    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            self.radius -= ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position[0],self.position[1],self.radius)
            ast1.velocity = self.velocity.rotate(angle) *1.2
            ast2 = Asteroid(self.position[0],self.position[1],self.radius)
            ast2.velocity = self.velocity.rotate(-angle) *1.2




