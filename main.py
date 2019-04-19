from ramp import Ramp
from projectile import Projectile
import math

# Ramp(length,angle)
myRamp = Ramp(10, 0)

# Projectile(u0, angle, height, ramp)
myProjectile = Projectile(math.sqrt(2), -math.pi / 2, 10, myRamp)

myProjectile.calcxy(0)

myRamp.printStats()
myProjectile.printStats()


myRate=0.001
t=-myRate
myProjectile.checkRampFall()
while True:
    t+=myRate
    myProjectile.getPosition(t)
    myProjectile.checkDrop(t)
    if (myProjectile.drop==1):
        break
    if (t>=15):
        break


def getInput():
