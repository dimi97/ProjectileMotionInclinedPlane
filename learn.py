from ramp import Ramp
from target import Target
from angleMath import AngleMath
from projectile import Projectile
import math
from scipy.misc import derivative


class Learn:

    def cost(myTarget, myProjectile):
        return math.pow(myTarget.x - myProjectile.xFall, 2)

    def printStats(myTarget, myProjectile):
        print("Target was:" + str(myTarget.x))
        print("Projectile fell at:" + str(myProjectile.xFall))
        print("Cost is:" + str(Learn.cost(myTarget, myProjectile)))

    def xofangle(x):
        myRamp = Ramp(100, 0)
        myProjectile = Projectile(math.sqrt(2), x, 0, myRamp)


        myProjectile.calcxtFall(0.00000000000000001)

        return myProjectile.xFall

    def bestAngle1(acc,step):
        myAngle = 0
        while True:

            myDer = derivative(Learn.xofangle, myAngle, dx=1e-3)
            # print("Derivative Value: " + str(myDer))
            lf = 1
            if (abs(lf * myDer) < step/10):
                lf = step/10 / myDer

            myAngle += lf * myDer
            print("CURRENT ANGLE:" + str(AngleMath.toDeg(myAngle)))

            if abs(myDer) < acc:
                break

        print("Best angle derivative method is:" + str(AngleMath.toDeg(myAngle)))

    def bestAngle2(acc):
        angle = 0.0
        angleRate = 0.1
        myDir = 1

        while (angleRate > acc):

            if (Learn.xofangle(angle + angleRate) > Learn.xofangle(angle)):

                angle += angleRate
                prevDir = 1
            elif (Learn.xofangle(angle - angleRate) > Learn.xofangle(angle)):

                angle -= angleRate
                prevDir = -1
            else:
                angleRate = angleRate / 2

            if (myDir * prevDir < 0):
                angleRate = (angleRate) / 2
                angleRate = abs(angleRate)
            print("CURRENT ANGLE:" + str(AngleMath.toDeg(angle)))

        print("Best angle numerical method:" + str(AngleMath.toDeg(angle)))
