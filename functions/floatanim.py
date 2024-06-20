import math

class FloatAnim:
    def __init__(self, speed, amplitude):
        self.angle = 0
        self.speed = speed
        self.amplitude = amplitude

    def update(self):
        self.angle += self.speed
        eased_angle = math.sin(self.angle * math.pi - math.pi/2)
        offset = eased_angle * self.amplitude
        return offset