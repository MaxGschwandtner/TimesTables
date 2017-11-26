from turtle import Screen, Turtle
import time
pointList = []
colors = ['blue', 'cyan', 'green', 'yellow', 'orange', 'magenta', 'red', 'brown']
numberOfPoints = 200
screen = Screen()
t = Turtle()

def setup():
    t.penup()
    t.right(90)
    t.forward(200)
    t.left(90)
    t.pendown()
    t.circle(200)
    t.penup()
    t.home()
    t.left(180)
    t.pendown()

def getPoints():
    for i in range(numberOfPoints):
        t.penup()
        t.forward(200)
        p = t.position()
        pointList.append(p)
        if numberOfPoints <= 100:
            t.write(str(i))
        t.left(180)
        t.forward(200)
        angle = 360/numberOfPoints
        t.right(180 + angle)
        t.pendown()

def createGraphics(multiplier):
    for i in range(numberOfPoints):
        t.penup()
        t.goto(pointList[i])
        t.pendown()
        for j in range(numberOfPoints):
            if (multiplier * i)%numberOfPoints == j:
                t.goto(pointList[j])
                t.penup()
                t.home()
                t.pendown()

def run(multiplier):
    t.hideturtle()
    screen.tracer(False)
    setup()
    getPoints()
    createGraphics(multiplier)
    screen.tracer(True)

def writeNumbers(num):
    t.penup()
    t.goto(-250, -250)
    t.write(str(num), font=("Arial", 25, "normal"))
    t.home()
    t.pendown()

def animation():
    for i in range(2, 100):
        t.clear()
        t.pencolor(colors[i%8])
        run(i)
        writeNumbers(i)
        time.sleep(0.7)

animation()
screen.mainloop()

