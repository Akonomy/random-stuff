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
red=100
blue=0

s=randint(3,12)


l=randint(3,8)
# ak.color("red")

a=[1,2,3,4,5,6,7,8]
for f in range (8):
    a[f]=randint(-50,50)
    

for x in range(s*(-1),s):
    if x<=0:
        red-=6
        blue+=6
        ak.color((red)*0.01,red*0.002,(blue)*0.01)
    if x>0:
        red+=6
        blue-=6
        ak.color((red)*0.01,0,(blue)*0.01)
    for y in range(l*(-1),l):
  
        #ak.clear()
        ak.penup()
        ak.goto(x*a[0],y*a[1])
        ak.pendown()
        
        
        ak.goto(x*a[0],y*a[1])
        ak.goto((x+1)*a[2],y*a[3])
        ak.goto((x+1)*a[4],(y-1)*a[5])
        ak.goto(x*a[6],(y-1)*a[7])
        
        ak.penup()
        ak.goto(x*50,(y-1)*50)


        ak.begin_poly()
        ak.goto(x*50,y*50)
        ak.goto((x+1)*50,y*50)
        ak.goto((x+1)*50,(y-1)*50)
        ak.goto(x*50,(y-1)*50)
        ak.end_poly()
        ak.pendown()

        tabla[str(str(x)+":"+str(y))]=ak.get_poly()
        

ak.getscreen()
# 
ak.getcanvas().postscript(file=str(a[0])+str(a[1])+str(a[2])+str(a[3])+str(a[4])+str(a[5])+str(a[6])+str(a[7])+".eps")

ak.penup()
ak.goto(s*(-1)*50,l*(-1)*50)
ak.pendown()
ak.goto(s*(-1)*50,(l-1)*50)
ak.goto(s*50,(l-1)*50)
ak.goto(s*50,(l+1)*(-1)*50)
ak.goto(s*(-1)*50,(l+1)*(-1)*50)
ak.penup()


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
    #print(x, y)
    global tabla
    global castigator
    global index
    for n in tabla.keys():
        if x>tabla[n][0][0] and  x<tabla[n][2][0]:
            if y> tabla[n][0][1] and y<tabla[n][2][1]:
                print(n)
                z=n.split(":")
                a=int(z[0])
                b=int(z[1])
                ak.penup()
                ak.goto(a*50,b*50)
                ak.pendown()
                ak.begin_fill()
                ak.fillcolor("red")
                ak.goto(a*50,b*50)
                ak.goto((a+1)*50,b*50)
                ak.goto((a+1)*50,(b-1)*50)
                ak.goto(a*50,(b-1)*50)
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
                ak.goto(a*50,b*50)
                ak.pendown()
                ak.begin_fill()
                ak.fillcolor("yellow")
                ak.goto(a*50,b*50)
                ak.goto((a+1)*50,b*50)
                ak.goto((a+1)*50,(b-1)*50)
                ak.goto(a*50,(b-1)*50)
                ak.end_fill()
                ak.penup()
                ak.done()
                break
                
                

    




#functii  de care nu te atingi :))), glumesc
ak.onscreenclick(get_mouse_click_coor)


done()                
