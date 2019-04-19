import math


class Projectile:
    g = 9.81

    def __init__(self, u0, angle, height, ramp):
        self.u0 = u0
        self.angle = angle
        self.height = height
        self.ramp = ramp

    def calc_t_ramp(self):
        if (self.ux != 0):
            self.tRamp = (self.ramp.length * math.cos(self.ramp.angle) - self.x0) / self.ux
        else:
            self.tRamp = -1

    def checkRampFall(self):
        self.calc_t_ramp()
        self.calcy(self.tRamp)
        myY = self.y

        print("Height above ramp end:"+str(myY))

        if (myY >= 0 or self.tRamp<0):
            self.rampFall = False
        else:
            self.rampFall = True

    def checkDrop(self, t):
        self.ramp.calcCurrent0(t, self)
        self.calcxy(t)
        self.drop = 0
        print("i checked")

        if (self.rampFall == True):
            if (self.y < self.ramp.current0):
                print(str(self.y)+" "+str(self.ramp.current0))
                self.drop = 1

        else:
            if (self.y < 0):
                self.drop = 1

    def calcx(self, t):
        self.x = self.x0 + self.ux * t

    def calcy(self, t):
        self.y = self.y0 + self.uy * t - (0.5) * self.g * math.pow(t, 2)

    def calcxy(self, t):
        self.calcInit()

        self.calcx(t)
        self.calcy(t)

    def getPosition(self, t):
        self.calcxy(t)
        print("STATS FOR t=" + str(t))
        print("------------------")
        print("Projectile x position:" + str(self.x))
        print("Projectile y position:" + str(self.y))

    def calc_xy0(self):
        self.x0 = self.height * math.sin(self.ramp.angle)
        self.y0 = self.ramp.height + self.height * math.cos(self.ramp.angle)

    def calc_uxy0(self):
        self.ux = self.u0 * math.cos(self.angle - self.ramp.angle)
        self.uy = self.u0 * math.sin(self.angle - self.ramp.angle)

    def printStats(self):
        self.calcInit()

        print("PROJECTILE STATS:")
        print("-----------------")
        print("Projectile initial height:" + str(self.height))
        print("Projectile y0:" + str(self.y0))
        print("Projectile x0:" + str(self.x0))
        print("Projectile uy:" + str(self.uy))
        print("Projectile ux:" + str(self.ux))

    def calcInit(self):
        self.calc_xy0()
        self.calc_uxy0()
