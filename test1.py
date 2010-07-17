import pygame
import Box2D as box2d
from world import World
from entity import Entity
from camera import Camera

hz = 30
dt = 1.0/hz

class BallEntity(Entity):
    def __init__(self, position, properties):
        Entity.__init__(self, position, properties)

    def construct(self, world):
        print "constructing"
        self.body_def = box2d.b2BodyDef()
        self.body_def.position = self._position
        self.body = world.world.CreateBody(self.body_def)
        
        self.shape_def = box2d.b2CircleDef()
        self.apply_properties_to_def(self.shape_def)
        
        self.body.CreateShape(self.shape_def)
        self.body.SetMassFromShapes()

    def draw(self, camera):
        print "draw, pos is? %s" % self.body.position
        pygame.draw.circle(camera.surface,
                           (255,0,0,255),
                           camera.vector_to_screen(self.body.position.tuple()),
                           camera.scalar_to_screen(self.properties['radius']), 
                           1)

    def step(self, dt):
        print "step ball"



def run():
    WIDTH = 640
    HEIGHT = 480

    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
    w = World()

    c = Camera(screen, (0,0), 3.0, HEIGHT)
    c.set_world(w)

    b = BallEntity((100,100), {'radius': 10, 'density': 10, 'restitution': 0.1})
    w.add_entity(b)

    b2 = BallEntity((100,60), {'radius': 20, 'density': 100})
    w.add_entity(b2)
    b2.body.SetLinearVelocity((0,40))

    while running:
        screen.fill((255,255,255))
        print b.body.position
        c.draw()
        pygame.display.flip()

        w.step(dt)
        clock.tick(hz)

run()
