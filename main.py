import pygame
from constants import*
import player
import asteroid
import asteroidfield
import shot
from circleshape import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    play = True
    clock = pygame.time.Clock()
    dt=0
    frame_rate = 60
    #Initial framing for player
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    #Player
    #Containers
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #sets all players to that container (seems to need to be done first before intialization)
    player.Player.containers=(updateable,drawable)
    ship = player.Player(x,y)
    #creating a group to hold all asteroids
    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids,updateable,drawable)
    asteroidfield.AsteroidField.containers = (updateable)
    asteroid_field = asteroidfield.AsteroidField()
    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots,updateable,drawable)

    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for updateables in updateable:
            updateables.update(dt)
        for ast in asteroids:
            game_over = ship.collision(ast)
            for s in shots:
                if s.collision(ast):
                    ast.split()
            if game_over == True:
                print("Game Over!")
                play = False
                
        for drawables in drawable:
            drawables.draw(screen)
        dt = clock.tick(frame_rate)/1000
        pygame.display.flip()
        #print (dt)


if __name__ == "__main__":
    main()
