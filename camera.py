class Camera:
    def __init__(self, surface, center, zoom, screenHeight):
        self.surface = surface
        self.height = screenHeight #TODO: callback on screen size change
        self.center = center #relative to world
        self.zoom = zoom

        self.world = None

    def set_world(self, world):
        self.world = world

    def draw(self):
        for e in self.world.entities:
            e.draw(self) #TODO: only draw what's in viewport

    def step(self, dt):
        pass #TODO: implement object tracking

    def vector_to_screen(self, pt): #TODO: memoize this intelligently
        ''' takes world coordinates, returns screen coordinates'''
        x,y = pt
        x -= self.center[0]
        x *= self.zoom

        y -= self.center[1]
        y *= self.zoom
        y = self.height - y
        return (x,y)

    def scalar_to_screen(self, sc):
        return sc * self.zoom
        
        
