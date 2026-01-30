class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def orbit(self, orbital):
        return 31_557_600 * orbital

    def on_mercury(self):
        return round(self.seconds / self.orbit(0.2408467), 2)

    def on_venus(self):
        return round(self.seconds / self.orbit(0.61519726), 2)
        
    def on_earth(self):
        return round(self.seconds / self.orbit(1.0), 2)
    
    def on_mars(self):
        return round(self.seconds / self.orbit(1.8808158), 2)
    
    def on_jupiter(self):
        return round(self.seconds / self.orbit(11.862615), 2)
    
    def on_saturn(self):
        return round(self.seconds / self.orbit(29.447498), 2)
    
    def on_uranus(self):
        return round(self.seconds / self.orbit(84.016846), 2)
    
    def on_neptune(self):
        return round(self.seconds / self.orbit(164.79132), 2)
    