from ramp import Ramp
from target import Target
from angleMath import AngleMath
from projectile import Projectile
from learn import Learn
import math
from scipy.misc import derivative
import graphics
from myConstants import myConstants

myRamp = Ramp(700, AngleMath.toRad(15))
myProjectile = Projectile(60, AngleMath.toRad(20), 100, myRamp)

graphics.initialGraphics(myProjectile)
print("initial x0:" + str(myProjectile.x0))
print("initial y0:" + str(myProjectile.y0))
myRamp.printStats()

myProjectile.calcxtFall(0.000001)

t = 0.0
# for i in range(1, len(myProjectile.tFallList)):

for i in range(0, len(myProjectile.tList)):

    if (myProjectile.tList[i] >= t):
        myProjectile.x = myProjectile.xList[i]
        myProjectile.y = myProjectile.yList[i]

        graphics.move(graphics.player, myProjectile,t)
        t += myConstants.myRate

# Learn.bestAngle1(0.0000000000001,0.00000000000001)
# Learn.bestAngle2(0.00000001)
'''
print("my t list")
print(myProjectile.tList)
print("x list")
print(myProjectile.xList)
print("y list")
print(myProjectile.yList)
'''
print("kenergy list")
print(myProjectile.kEnergyList)

print("penergy list")
print(myProjectile.pEnergyList)

print("energy list")
print(myProjectile.EnergyList)
