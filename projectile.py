import math
from myConstants import *
from angleMath import AngleMath
import sys

sys.setrecursionlimit(9999)
class Projectile:
    tList = []
    xList = []
    yList = []
    kEnergyList=[]
    pEnergyList=[]
    EnergyList=[]

    tFallList = [0]
    xFallList = []

    def __init__(self, u0, angle, height, ramp):
        self.u0 = u0
        self.angle = angle
        self.height = height
        self.ramp = ramp
        self.realu0 = u0
        self.realHeight = height
        self.realAngle = angle
        self.shots = 0

    def printResults(self):
        self.calcxtFall(0.0000001)
        print("Falling time:" + str(self.tFall))
        print("Traveled distance:" + str(self.xFall))

    def calc_t_ramp(self):
        self.calcInit()
        if (self.ux0 != 0):
            self.tRamp = (self.ramp.length * math.cos(self.ramp.angle) - self.x0) / self.ux0
        else:
            self.tRamp = -1

        # self.calc_t_ramp_info()

    def calc_t_ramp_info(self):
        print("calc_t_ramp")
        print("distance to ramp end:" + str((self.ramp.length * math.cos(self.ramp.angle)) - self.x0))
        print("current x0:" + str(self.x0))
        print("ux0:" + str(self.ux0))
        print("t Ramp is: " + str(self.tRamp))

    def checkRampFall(self):
        self.calc_t_ramp()
        self.calcy(self.tRamp)
        self.calcx(self.tRamp)
        self.y
        self.ramp.calcCurrent0(self.x)

        if ((self.y >= 0 or self.tRamp < 0) and self.ux0 != 0):  # kapou edw einai to la8os
            self.rampFall = False
        elif (self.ux0 == 0 and self.ramp.current0 < 0):
            self.rampFall = False
        else:
            self.rampFall = True

            # self.checkRampFallInfo()

    def checkRampFallInfo(self):
        print("Height above ramp end:" + str(self.y))
        print("x at ramp end:" + str(self.x))
        print("Ramp height at t ramp:" + str(self.ramp.current0))
        print("Ramp fall is:" + str(self.rampFall))

    def checkDrop(self, t):
        self.getPosition(t)
        self.ramp.calcCurrent0(self.x)

        self.drop = 0

        # self.checkDropInfo()

        if (self.rampFall == True):
            if (self.y < self.ramp.current0):
                self.drop = 1

        else:
            if (self.y < 0):
                self.drop = 1

    def checkDropInfo(self):
        print("Drop check:")
        print("my Ramp fall is:" + str(self.rampFall))
        print("my y0 is:" + str(self.y0))
        print("my x0 is:" + str(self.x0))
        print("my uy0 is:" + str(self.uy0))
        print("my ux0 is:" + str(self.ux0))
        print("my y is:" + str(self.y))
        print("my current 0 is:" + str(self.ramp.current0))
        print("Drop status is:" + str(self.drop))
        print("Drop check end!")

    def calcx(self, t):
        self.x = self.x0 + self.ux0 * t

    def calcy(self, t):
        self.y = self.y0 + self.uy0 * t - (0.5) * myConstants.g * t * t

    def calcxy(self, t):

        self.calcx(t)
        self.calcy(t)

    def getPosition(self, t):
        self.calcInit()
        self.calcxy(t)

    def printPosition(self, t):

        print("STATS FOR t=" + str(t))
        print("------------------")
        print("Projectile x position:" + str(self.x))
        print("Projectile y position:" + str(self.y))

    def calc_xy0(self):

        if len(self.xFallList) == 0:

            self.xFallList.append(self.realHeight * math.sin(self.ramp.angle))
            self.x0 = 0

        lx0 = self.xFallList[-1]

        if len(self.xFallList)==1:
            self.ramp.current0=self.ramp.height
        else:
            self.ramp.calcCurrent0(lx0)
        if (self.ramp.current0 < 0):
            a = 0
        else:
            a = self.ramp.current0

        self.x0 = lx0
        self.y0 = a + self.height * math.cos(self.ramp.angle)

        #print("i calculated initials for x="+str(lx0)+"and y0 is:"+str(self.y0)+"because ramp height is:"+str(self.ramp.current0))

    def calc_uxy0(self):
        self.ramp.calcCurrent0(self.x0)
        a = self.ramp.current0

        if (a > 0):

            self.ux0 = self.u0 * math.cos(self.angle - self.ramp.angle)
            self.uy0 = self.u0 * math.sin(self.angle - self.ramp.angle)
        else:
            self.ux0 = self.u0 * math.cos(self.angle)
            self.uy0 = self.u0 * math.sin(self.angle)

        #self.calc_uxy0_info()

    def calc_uxy0_info(self):
        print("calc uxy0:")
        print("angle:" + str(AngleMath.toDeg(self.angle)))
        print("x0:" + str(self.x0))
        print("y0:" + str(self.y0))
        print("ramp height:" + str(self.ramp.current0))
        print("ux0:" + str(self.ux0))
        print("uy0:" + str(self.uy0))
        U = math.sqrt(self.ux0 * self.ux0 + self.uy0 * self.uy0)
        print("U:" + str(U))

    def calc_ux(self, t):

        self.ux = self.ux0

    def calc_uy(self, t):

        self.uy = self.uy0 - myConstants.g * t

    def calc_u(self, t):
        self.calc_uxy0()
        self.calc_ux(t)
        self.calc_uy(t)
        myUx = self.ux
        myUy = self.uy
        self.u = math.sqrt((math.pow(myUx, 2) + math.pow(myUy, 2)))

        if (myUx != 0):
            self.uAngle = math.atan(myUy / myUx)
        else:
            self.uAngle = 0

    def print_u(self, t):
        self.calc_u(t)
        print("t=" + str(t))
        print("u=" + str(self.u) + " at an angle " + str(AngleMath.toDeg(self.uAngle)))

    def printInit(self):
        print("My x0=" + str(self.x0))
        print("My y0=" + str(self.y0))
        print("My ux=" + str(self.ux0))
        print("My uy=" + str(self.uy0))

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

    def calcxtFall(self, myAcc):
        myRate = 0.01
        t = 0

        self.checkRampFall()
        self.calc_u(t)

        self.printInit()
        while True:
            print("TIME:" + str(t + self.tFallList[-1]))
            if (len(self.EnergyList)!=0):
                if (self.EnergyList[-1] < 3000):
                    print("energy drop")
            self.getPosition(t)

            #self.printPosition(t)
            self.checkDrop(t)

            if (self.drop == 1):
                t -= myRate
                myRate = myRate / 2
                if (myRate < myAcc):

                    self.calc_u(t)
                    self.updateFallList(t)

                    if (abs(self.uy) > 0.01 and self.shots<myConstants.maxHits):
                        print("before new shot" + str(self.uy))
                        print("shot number:"+str(self.shots+2))
                        self.newShot(t)

                        self.calcxtFall(myAcc)

                    break
            self.calc_u(t)

            self.xList.append(self.x)
            self.yList.append(self.y)
            self.tList.append(t + self.tFallList[-1])
            self.kEnergyList.append(0.5*myConstants.mass*self.u*self.u)
            self.pEnergyList.append(myConstants.g * myConstants.mass * self.y)
            self.EnergyList.append(self.kEnergyList[-1]+self.pEnergyList[-1])
            print("Energy:"+str(self.EnergyList[-1]))
            print("actual velocity:"+str(self.u))


            t += myRate

    def newShot(self, t):
        self.shots += 1
        print("NEW SHOT----------------")
        print("t new shot=" + str(t+self.tFallList[-2]))
        self.height = 0

        self.getPosition(0)
        #self.printPosition(0)


        self.ramp.calcCurrent0(self.x)

        if (self.ramp.current0 > 0):

            rux = self.u * math.cos((self.uAngle) + (self.ramp.angle))
            ruy = self.u * math.sin((self.uAngle) + (self.ramp.angle))
            ruy = abs((ruy * myConstants.energyPerc))
            newU = math.sqrt(rux * rux + ruy * ruy)
            newAngle = (math.atan(ruy / rux))

            self.newVelocityCheck(rux, ruy, newAngle)

        else:
            print("energy loss investigation")
            print("u:"+str(self.u))
            print("ux:" + str(self.ux))
            print("uy:" + str(self.uy))
            print("kenergy:"+str(self.kEnergyList[-1]))
            self.uy0 = -self.uy * myConstants.energyPerc
            newU = math.sqrt(self.uy0 * self.uy0 + self.ux * self.ux)
            newAngle = (math.atan(self.uy0 / self.ux))

        self.u0 = newU
        self.angle = newAngle
        self.height = 0

        self.calc_u(t)
        print("u:" + str(self.u))
        print("ux:" + str(self.ux))
        print("uy:" + str(self.uy))
        print("kenergy:" + str(self.kEnergyList[-1]))


    def updateFallList(self, t):
        self.tFall = t
        self.tFallList.append(self.tFall + self.tFallList[-1])
        self.xFall = self.x
        self.xFallList.append(self.xFall)

    def newVelocityCheck(self, rux, ruy, newAngle):
        print("new velocity check")
        print("ux" + str(self.ux))
        print("uy" + str(self.uy))
        print("u Angle:" + str(AngleMath.toDeg(self.uAngle)))
        print("ramp angle:" + str(AngleMath.toDeg(self.ramp.angle)))
        print("u:" + str(self.u))
        print("rux:" + str(rux))
        print("ruy:" + str(ruy))
        Ru = math.sqrt(rux * rux + ruy * ruy)
        print("Ru:" + str(Ru))
        print("new angle:" + str(AngleMath.toDeg(newAngle)))
