import circleshape
from constants import *
import pygame

class Shot(circleshape.CircleShape):
        def __init__(self,x,y,SHOT_RADIUS):
            super().__init__(x,y,SHOT_RADIUS)
            self.width=1 #come back to this
        def draw (self,screen):
            pygame.draw.circle(screen,"white",self.position, self.radius,self.width)
        def update(self,dt):
            self.position += self.velocity * dt