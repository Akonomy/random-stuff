from turtle import*
import turtle as ak
ak.speed(1)
ak.bgcolor("black")

def inima(rotate,color):
    ak.begin_poly()
    ak.begin_fill()
    ak.color(color)
    ak.fillcolor("red")
    ak.pensize(3)
    ak.left(140)
    ak.forward(112)

    ak.circle(-60,200)
    ak.left(118)
    ak.circle(-60,200)
    ak.forward(115)
    ak.end_fill()
    ak.end_poly()
    heart0 = ak.get_poly()
    ak.register_shape("heart",heart0)


    ak.shape("heart")
    ak.shapesize(0.1)
    ak.left(rotate)

ak.speed(1)
ak.forward(500)
ak.forward(-500)
ak.speed(2)
inima(143,"red")

ak.st()
ak.clear()
ak.speed(3)
inima(-128,"white")
for i in range(1,120):
    ak.shapesize(i/100)    

ak.clear()
ak.penup()
ak.goto(-150,-50)
ak.speed(5)
write=ak.Turtle()
write.penup()
write.ht()
write.speed(-99999)
write.goto(-150,-50)
write.color("red")
write.write("Love you!",font=("Arial",30))
ak.pencolor("red")
ak.goto(100,-50)


done()