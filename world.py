import Box2D as box2d

class World:
    velocity_iterations = 10
    position_iterations = 8
    def __init__(self):
        self.setup_world()
        self.entities = []

    def setup_world(self):
        self.worldAABB = box2d.b2AABB()
        self.worldAABB.lowerBound = (-2000.0, -2000.0)
        self.worldAABB.upperBound = (2000.0, 2000.0)
        self.gravity = (0.0, -9.81)
        doSleep = False
        self.world = box2d.b2World(self.worldAABB, self.gravity, doSleep) 

    def add_entity(self, entity):
        self.entities.append(entity)
        entity.construct(self)

    def remove_entity(self, entity, strict=False):
        if not strict:
            if entity in self.entities:
                self.entities.remove(entity)
        else: #die if not present
            self.entities.remove(entity)

    def step(self, dt):
        for e in self.entities:
            e.step(dt)
        self.world.Step(dt, self.velocity_iterations, self.position_iterations)
        self.world.Validate()

    
