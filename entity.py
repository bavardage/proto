class Entity:
    def __init__(self, position, properties={}):
        self._position = position #TODO: property for actual position?
        self.properties = dict(properties)

    def construct(self, world):
        raise NotImplementedError

    def destroy(self, world):
        raise NotImplementedError

    def draw(self, camera):
        raise NotImplementedError        

    def step(self, dt):
        print "step entity"

    def apply_properties_to_def(self, d):
        for k,v in self.properties.items():
            setattr(d, k, v)
