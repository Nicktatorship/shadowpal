class Vector(object):
    def __init__(self, _x=0, _y=0, _z=0):
        self.x = _x
        self.y = _y
        self.z = _z
        
    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z)
        
    def __add__(self, component):
        if isinstance(component, Vector):
            return Vector(self.x + component.x, self.y + component.y, self.z + component.z)
        else:
            return Vector(self.x + int(component), self.y + int(component), self.z + int(component))
    
    def product(self):
        return self.x * self.y * self.z
        
    def intersect(self, component):
        if isinstance(component, Vector):
            _altx = component.x
            _alty = component.y
            _altz = component.z
            
            
            
        else:
            return false
        
        
