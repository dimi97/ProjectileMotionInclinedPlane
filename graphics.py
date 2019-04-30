import turtle
from turtle import *
import tkinter
import os
from ramp import Ramp
from projectile import Projectile
from angleMath import AngleMath
from myConstants import myConstants


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Physics Simulation")
wn.bgpic("bd.png")
player = turtle.Turtle()


def printStats(t):

    turtle.color('deep pink')
    style = ('Arial', 30, 'italic')
    turtle.write(t, font=style, align='left')

    turtle.hideturtle()





def initialGraphics(myProjectile):
    myHeight = myConstants.myHeight
    myWidth = myConstants.myWidth
    drawBorder(myWidth, myHeight)
    drawRamp(myProjectile.ramp, myHeight, myWidth)

    drawProjectile(player, myProjectile, myHeight, myWidth)


def drawBorder(width, height):
    myWidth = width
    myHeight = height
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("black")
    border_pen.penup()
    border_pen.setposition(-myWidth / 2, -myHeight / 2)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(2):
        border_pen.fd(myWidth)
        border_pen.lt(90)
        border_pen.fd(myHeight)
        border_pen.lt(90)
    border_pen.hideturtle()


def drawRamp(myRamp, myHeight, myWidth):
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("black")
    border_pen.penup()

    border_pen.setposition(-myWidth / 2, myRamp.height - myHeight / 2)
    border_pen.pendown()
    border_pen.pensize(7)
    border_pen.rt(AngleMath.toDeg(myRamp.angle))
    border_pen.fd(myRamp.length)
    border_pen.hideturtle()


def drawProjectile(player, myProjectile, myHeight, myWidth):
    player.shape("circle")
    player.shapesize(0.65, 0.65)
    player.penup()
    player.speed(0)
    myProjectile.calc_xy0()
    player.setposition(-myWidth / 2, myProjectile.ramp.height - myHeight / 2)
    player.color("black")
    player.pendown()
    player.pensize(7)
    player.lt(90 - AngleMath.toDeg(myProjectile.ramp.angle))
    player.fd(myProjectile.height)
    player.pensize(4)
    player.color("yellow")


def move(player, myProjectile,t):

    x = player.xcor()
    y = player.ycor()

    x = myProjectile.x - myConstants.myWidth / 2
    y = myProjectile.y - myConstants.myHeight / 2

    player.setx(x)
    player.sety(y)

