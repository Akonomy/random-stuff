#

from turtle import*
from random import*
import turtle as ak

tablo=ak.Turtle()
tb= ak.Shape("compound")

ak.bgcolor("black")
ak.color("white")

ak.hideturtle()
y=-5
x=-12
tabla={}
# 
# ak.goto(-200,150)
# ak.color("cyan")
# ak.write("Bun",font=("Arial",30),align="center")
# ak.forward(85)
# ak.write("venit",font=("Arial",30),align="center")
# ak.forward(80)
# ak.write("la",font=("Arial",30),align="center")
# ak.forward(75)
# ak.write("jocul",font=("Arial",30),align="center")
# ak.forward(110)
# ak.write("",font=("Arial",30),align="center")
# ak.forward(-185)
# ak.right(90)
# ak.forward(80)
# ak.color("red")
# ak.write("Find",font=("Arial",35),align="center")
# ak.right(-90)
# ak.forward(85)
# ak.color("orange")
# ak.write("or",font=("Arial",35),align="center")
# ak.forward(85)
# ak.color("red")
# ak.write("Lose",font=("Arial",35),align="center")


# ak.goto(x*50,y*50)
ak.speed(-9999999)
ak.clear()
ak.begin_fill()
ak.fillcolor("red")
ak.end_fill()
red=0
blue=255
green=150

s=randint(3,12)


l=randint(2,7)
ak.colormode(255)

for x in range(s*(-1),s):
#     if x<=0:
#         red-=6
#         blue+=6
#         ak.color((red)*0.01,(red)*0.01,(blue)*0.01)
#     if x>0:
#         red+=6
#         blue-=6
#         ak.color(0,(red)*0.01,(blue)*0.01)
    for y in range(l*(-1),l):
        
        if red<255:
            red+=3
            if green>0:
                green-=1
        if blue>0:
            blue-=1
        if green<130 and red<100:
            green+=2
        ak.color(red,green,blue) 
        ak.penup()
        ak.goto(x*45,(y-1)*45)
        ak.pendown()
        
        #ak.clear()
        ak.pendown()
        ak.begin_poly()
        ak.goto(x*45,y*45)
        ak.goto((x+1)*45,y*45)
        ak.goto((x+1)*45,(y-1)*45)
        ak.goto(x*45,(y-1)*45)
        ak.end_poly()
        ak.penup()

        tabla[str(str(x)+":"+str(y))]=ak.get_poly()
        
        
        
demi=True
castigator=0
while demi:
    for i in tabla.keys():
        g=randint(0,78542)
        if g==6969:
            m=tabla[i]
            castigator=m
            index=i
            demi=False
            break
            
            
        
ak.penup()

    
    
def get_mouse_click_coor(x, y):
    print(x, y)
    global tabla
    global castigator
    global index
    ak.color(23,45,45)
    for n in tabla.keys():
        if x>tabla[n][0][0] and  x<tabla[n][2][0]:
            if y> tabla[n][0][1] and y<tabla[n][2][1]:
                print(n)
                z=n.split(":")
                a=int(z[0])
                b=int(z[1])
                ak.penup()
                ak.goto(a*45,b*45)
                ak.pendown()
                ak.begin_fill()
                
                ak.fillcolor("red")
                ak.goto(a*45,b*45)
                ak.goto((a+1)*45,b*45)
                ak.goto((a+1)*45,(b-1)*45)
                ak.goto(a*45,(b-1)*45)
                ak.goto(a*45,b*45)
                ak.end_fill()
                ak.penup()
        #castigator=castigator.split(":")    
        if x>int(castigator[0][0]) and  x<int(castigator[2][0]):
            if y> int(castigator[0][1]) and y<int(castigator[2][1]):
                print("AI CASTIGAT")
                z=index.split(":")
                a=int(z[0])
                b=int(z[1])
                ak.penup()
                ak.goto(a*45,b*45)
                ak.pendown()
                ak.begin_fill()
                ak.fillcolor("yellow")
                ak.goto(a*45,b*45)
                ak.goto((a+1)*45,b*45)
                ak.goto((a+1)*45,(b-1)*45)
                ak.goto(a*45,(b-1)*45)
                ak.end_fill()
                ak.penup()
                ak.done()
                break
                
                

    




#functii  de care nu te atingi :))), glumesc
ak.onscreenclick(get_mouse_click_coor)

ak.getscreen()
# 
ak.getcanvas().postscript(file="pattern6.eps")
done()                