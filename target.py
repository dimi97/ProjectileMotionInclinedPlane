from ramp import Ramp
from projectile import Projectile
import math

class Target:

    def __init__(self, x, offset):
        self.x = x
        self.offset = offset

    def setOffset(self, offset):
        self.offset = offset;
