#tester loop for generate files
#

from turtle import*
from random import*
import turtle as ak

tablo=ak.Turtle()
tb= ak.Shape("compound")

ak.bgcolor("black")
ak.color("black")

ak.hideturtle()
y=-5
x=-12
tabla={}

# ak.goto(x*50,y*50)
ak.speed(-99999)
ak.clear()
ak.begin_fill()
ak.fillcolor("red")
ak.end_fill()

for j in range(20):
    red=100
    blue=0

    s=randint(3,12)


    l=randint(3,8)
    # ak.color("red")

    a=[50,50,50,50,50,50,50,50]
    for f in range (8):
        a[f]=randint(-200,200)
        

    for x in range(s*(-1),s):
        if x<=0:
            red-=6
            blue+=6
            ak.color(0,(blue)*0.01,(blue)*0.01)
        if x>0:
            red+=6
            blue-=6
            ak.color(0,(blue)*0.01,(blue)*0.01)
        for y in range(l*(-1),l):
      
            #ak.clear()
            ak.penup()
            ak.goto(x*a[0],y*a[1])
            ak.pendown()
            
            
            ak.goto(x*a[0],y*a[1])
            ak.goto((x+1)*a[2],y*a[3])
            ak.goto((x+1)*a[4],(y-1)*a[5])
            ak.goto(x*a[6],(y-1)*a[7])
            

            

    ak.getscreen()
    # 
    ak.getcanvas().postscript(file=str(a[0])+str(a[1])+str(a[2])+str(a[3])+str(a[4])+str(a[5])+str(a[6])+str(a[7])+".eps")
    ak.clear()
done()                

