from turtle import Screen, Turtle
pointList = []
numberOfPoints = 200
multiplier = 10
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

def createGraphics():
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

def run():
    t.hideturtle()
    screen.tracer(False)
    setup()
    getPoints()
    createGraphics()
    screen.tracer(True)

run()

screen.mainloop()
