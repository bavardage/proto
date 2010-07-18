import pygame
import Box2D as box2d

from world import World
from entity import *
from camera import Camera
import log

hz = 30
dt = 1.0/hz



def run():
    WIDTH = 640
    HEIGHT = 480

    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
    w = World()

    c = Camera(screen, (0,0), 3.0, HEIGHT)
    c.set_world(w)

    b = BallEntity((100,100), {'radius': 10, 'density': 10, 'restitution': 0.1,
                               'static': True, 'line-width': 5})
    w.add_entity(b)

    b2 = BallEntity((100,60), {'radius': 20, 'density': 100, 'restitution': 1.0})
    w.add_entity(b2)
    b2.body.SetLinearVelocity((0,40))

    base = BoxEntity((20,20), {'width': 100, 'height': 10})#, 'static': True})
    w.add_entity(base)

    while running:
        screen.fill((255,255,255))
        c.draw()
        pygame.display.flip()

        w.step(dt)
        clock.tick(hz)

run()
