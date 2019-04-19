import math


class Ramp:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle
        self.height = self.length * math.sin(self.angle)

    def printStats(self):
        print("RAMP STATS:")
        print("-----------------")
        print("Ramp length:" + str(self.length))
        print("Ramp height:" + str(self.height))
        print("Ramp angle:" + str(self.angle))

    def calcCurrent0(self,t,myProjectile):
        self.current0=(self.length*math.cos(self.angle)-myProjectile.x)*math.tan(self.angle)