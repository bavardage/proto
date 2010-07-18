import log, logging
import Box2D as box2d
import pygame

from utils import *

entity_log = logging.getLogger('entity')

class Entity:
    _body_def = None
    _shape_def = None

    def __init__(self, position, properties={}):
        entity_log.debug("in Entity __init__ %s" % self)
        self._position = position #TODO: property for actual position?
        self.properties = dict(properties)

    def construct(self, world):
        entity_log.debug("constructing %s" % self)
        self.body = world.world.CreateBody(self.body_def)
        self.body.CreateShape(self.shape_def)
        if not self.properties.get('static', False):
            self.body.SetMassFromShapes()
        entity_log.debug("done constructing %s" % self)

    @property
    def body_def(self):
        if self._body_def is None:
            self._body_def = box2d.b2BodyDef()
            self._body_def.position = self._position
        return self._body_def

    @property
    def shape_def(self):
        raise NotImplementedError

    def destroy(self, world):
        raise NotImplementedError

    def draw(self, camera):
        raise NotImplementedError        

    def step(self, dt):
        pass

    def apply_properties_to_def(self, d):
        for k,v in self.properties.items():
            if hasattr(d, k):
                setattr(d, k, v)


########################################
# Some default entities
########################################

class BallEntity(Entity):
    def draw(self, camera):
        pygame.draw.circle(camera.surface,
                           self.properties.get('color', (0,0,0,255)),
                           camera.vector_to_screen(self.body.position.tuple()),
                           camera.scalar_to_screen(self.properties['radius']), 
                           self.properties.get('line-width', 1))

    @property
    def shape_def(self):
        if self._shape_def is None:
            self._shape_def = box2d.b2CircleDef()
            self.apply_properties_to_def(self.shape_def)
        return self._shape_def


class BoxEntity(Entity):
    def draw(self, camera):
        w,h = [self.properties[k] for k in ('width', 'height')]
        vertices = [camera.vector_to_screen(v) 
                    for v in [self._position,
                              vadd(self._position, (w,0)),
                              vadd(self._position, (w,h)),
                              vadd(self._position, (0,h))]]
        pygame.draw.aalines(camera.surface,
                            self.properties.get('color', (0,0,0,255)),
                            True,
                            vertices)

#                         self.properties.get('line-width', 1))

    @property
    def shape_def(self):
        if self._shape_def is None:
            self._shape_def = box2d.b2PolygonDef()
            self._shape_def.SetAsBox(self.properties['width'],
                                     self.properties['height'])
        return self._shape_def
            
                                             
