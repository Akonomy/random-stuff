#computer go find waay
from turtle import*
import turtle as ak
from random import*
from operator import itemgetter

import random
ak.speed(-99999)
ak.hideturtle()  
class cube:
    def __init__(self,x,y,size=10,PRESS=False,LOCK=False):
        self.x=x
        self.y=y
        self.size=size
        self.PRESS=PRESS
        self.LOCK=LOCK
        
    def draw(self):
        ak.penup()
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.pendown()
        
        ak.begin_poly()
        ak.goto(self.x*self.size,self.y*self.size)
        ak.goto((self.x+1)*self.size,self.y*self.size)
        ak.goto((self.x+1)*self.size,(self.y+1)*self.size)
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.end_poly()
        ak.penup()
        
    def fill(self,color="black"):
        self.color=color
        #ak.pencolor(self.color)
        ak.fillcolor(self.color)
        ak.penup()
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.pendown()
        
        ak.begin_fill()
        ak.goto(self.x*self.size,self.y*self.size)
        ak.goto((self.x+1)*self.size,self.y*self.size)
        ak.goto((self.x+1)*self.size,(self.y+1)*self.size)
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.end_fill()
        ak.penup()
        
    def remove(self):
        self.color="black"
        #ak.pencolor(self.color)
        ak.fillcolor(self.color)
        ak.penup()
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.pendown()
        
        ak.begin_fill()
        ak.goto(self.x*self.size,self.y*self.size)
        ak.goto((self.x+1)*self.size,self.y*self.size)
        ak.goto((self.x+1)*self.size,(self.y+1)*self.size)
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.goto(self.x*self.size,(self.y+1)*self.size)
        ak.end_fill()
        ak.penup()
    def getposition(self):
        return self.x*self.size,self.y*self.size,self.size
    def getHalfpos(self):
        return (self.x*self.size)+(self.size/2),(self.y*self.size)+(self.size/2)
  
    def press(self,PRESS):
        self.PRESS=PRESS
        return self.PRESS
    def ispress(self):
        return self.PRESS
    def lock(self,LOCK):
        self.LOCK=LOCK
        return self.LOCK
    def islock(self):
        return self.LOCK
    def check(self,X,Y):
        if self.x*self.size<X and (self.x+1)*self.size>X:
            if self.y*self.size>Y and (self.y-1)*self.size<Y:
                return True
            else:
                return False
        else:
            return False        
    
    
  
class node:
    def __init__(self,x,y,path=[False,False,False,False]):
        self.firstRun=True
        self.x=x
        self.y=y
        self.top=path[0]
        self.bottom=path[2]
        self.right=path[1]
        self.left=path[3]
        self.cale1=0
        self.cale2=0
        self.cale3=0
        self.cale4=0
        self.list=[]
    class cale:
        def __init__(self,prioritate,lenght,way,dead,):
            self.prioritate=prioritate
            self.way=way
            self.lenght=lenght
            self.dead=dead
            
        def go(self):
            self.prioritate+=1
            
        def lv(self):
            return self.prioritate
        def isWay(self):
            return self.way
        def modWay(self,way):
            self.way=way
        def getLenght(self):
            return self.lenght
        def ifdead(self):
            return self.dead
        def modDead(self,dead):
            self.dead=dead
        def getCale(self):
            return self.cale    
    def getWay(self,l=[0,0,0,0]):
        self.cale=[0,0,0,0,0]
        if self.right:
            self.cale[1]=node.cale(l[1],0,False,False)
            self.list.append([self.cale[1].lv(),self.cale[1],1])
        if self.bottom:
            self.cale[2]=node.cale(l[2],0,False,False)
            self.list.append([self.cale[2].lv(),self.cale[2],2])
        if self.left:
            self.cale[3]=node.cale(l[3],0,False,False)
            self.list.append([self.cale[3].lv(),self.cale[3],3])
        if self.top:
            self.cale[0]=node.cale(l[0],0,False,False)
            self.list.append([self.cale[0].lv(),self.cale[0],0])


    def gotWay(self):
        if self.firstRun:
            self.firstRun=False
            self.getWay()
            
        if len(self.list)>0:
            self.list.sort(key=lambda x:x[0])
            self.list[0][1].go()
            self.list[0][0]=self.list[0][1].lv()
            return self.list[0][2]
        else:
            return False
            
       
       
       


        
        
test=node(1,1,[True,True,True,True])

#test.getWay()

for x in range(50):
    print(test.gotWay())

    
    







v,h=-2,8

obj=[[ 0 for x in range(-100,100)] for y in range(-100,100)]
for x in range(-2,2):
    for y in range(v,h):
        obj[x][y]=cube(x,y,30)
        obj[x][y].draw()
        


      
print(obj[0][0].check(25,-25) )

def run():
    pass
ak.penup()



count=v-1
switch=True
ak.speed(0)
ak.goto(-195.0, -45.0)
for x in range(-2,2):
    
    for y in range(v,h):
        #print([x,y],[count])
        if count==h-1 and switch:
            switch=False
            count+=1
        if count==v and not switch:
            count-=1
            switch=True
        if switch:
            count+=1
        if  not switch:
            count-=1
        #print([x,y],[count],"finale",[y,count])
        if str(type(obj[x][count])) !="<class 'int'>":
            j,k=obj[x][count].getHalfpos()
            #print(j,k,obj[0][1].getposition())
            ak.pendown()
            ak.goto(j,k)
            ak.pendown()
            ak.pencolor("red")
            ak.circle(3)
            ak.pencolor("blue")
#         o1,o2=obj[x][y].getHalfpos()
#         ak.pendown()
#         ak.pencolor("red")
#         ak.goto(o1,o2)
done()
       