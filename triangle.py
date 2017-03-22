import turtle
import math
import random


def triangle (L, t):
    t.left(60)
    t.forward(L)
    t.right(120)
    t.forward(L)
    t.right(120)
    t.forward(L)
    t.right(180)
    

def fractial (t, L, lv):
  if(lv==1):
    triangle(L, t)
  else:
    fractial(t, L/2, lv-1)
    t.lt(60)
    t.fd(L/2)
    t.rt(60)
    fractial(t, L/2, lv-1)
    t.rt(60)
    t.fd(L/2)
    t.lt(60)
    fractial(t, L/2, lv-1)
    t.back(L/2)
wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(2)
Albert.color('white')
fractial(Albert,200, 4)
   