from turtle import *
from random import randint
from random import random
from threading import Thread

hideturtle()
bgcolor('black')



n = 0
speed(110)
colormode(255)

while 100>n >= 0:
    speed(1000)
    forward(500)
    right(90)
    forward(1)
    right(90)
    forward(500)
    left(90)
    forward(1)
    left(90)
    R = randint(0, 255)
    B = randint(0, 255)
    G = randint(0, 255)
    color(R, G, B)
    n += 1

while 340> n >= 100:
    right(n)
    forward(n * 3)
    color('white')
    n += 1

while 340 <= n < 400:
    speed(110)
    up()
    goto(randint(-400,400),
         randint(-400,400))
    down()
    R = randint(0,255)
    B = randint(0,255)
    G = randint(0,255)
    color(R, G, B)
    dot(randint(20,80))
    n += 1
while 400 <= n <401:
    clear()
    t = [Turtle(), Turtle()]
    c = [1,3]

    colors = ["#F24452","#542d59", "#F2CF63"]
    bgcolor("black")
    tracer(30)
    ht()
    n += 1

    for index, i  in enumerate(t):
        i.ht()
        i.width(3)
        i.pu()
        i.seth(90)
        i.bk(120*(c[index]))
        i.seth(0)
        i.pd()

    for i in colors:
        t[0].color(i)
        t[1].color(i)
        color(i)
        for _ in range(361):
            for _ in range(12):
                t[0].fd(2)
                t[0].lt(1)
            pu()
            goto(t[0].pos())
            t[1].fd(c[1]*2)
            t[1].lt(1)
            pd()
            goto(t[1].pos())


while 401 >= n:
    t = [Turtle(), Turtle()]
    speed(500)
    ht()
    c = [1, 3]
    length = 100
    angle = 50
    size = 5
    for i in range(length):
        color = ['white']
        pencolor('white')
        fillcolor('white')
        penup()
        forward(i+50)
        pendown()
        left(angle)
        begin_fill()
        circle(size)
        end_fill()



