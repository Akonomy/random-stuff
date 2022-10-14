
#after run please press down , up , left and right key to move the point :)) also space , enter  and r will work 
#computer go find way
from turtle import*
import turtle as ak
from random import*
from operator import itemgetter

import random
ak.speed(0)
ak.hideturtle()

class cube:
    def __init__(self,x,y,size=10,PRESS=False,LOCK=False):
        self.x=x
        self.y=y
        self.size=size
        self.PRESS=PRESS
        self.LOCK=LOCK
        self.winner=True
        
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
        return [self.x*self.size,self.y*self.size,self.size]
    def getpositionxy(self):
        return [self.x,self.y,self.size]
    def getAllposition(self):
        return [(self.x*self.size,self.y*self.size),((self.x+1)*self.size,self.y*self.size),
                ((self.x+1)*self.size,(self.y+1)*self.size),(self.x*self.size,(self.y+1)*self.size)]
    def getHalfpos(self):
        return (self.x*self.size)+(self.size/2),(self.y*self.size)+(self.size/2)
  
    def press(self,PRESS):
        self.PRESS=PRESS
        return self.PRESS
    def ispress(self):
        return self.PRESS
    def lock(self,LOCK):
        self.LOCK=LOCK
    def islock(self):
        return self.LOCK
    def Setswin(self,state):
        self.winner=state
    def iswin(self):
        return self.winner
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
    def updateNode(self,path):
        self.top=path[0]
        self.bottom=path[2]
        self.right=path[1]
        self.left=path[3]
        
    def getWay(self,l=[0,0,0,0]):
        self.cale=[0,0,0,0,0]
        if not self.right:
            self.cale[1]=node.cale(l[1],0,False,False)
            self.list.append([self.cale[1].lv(),self.cale[1],1])
        if not self.bottom:
            self.cale[2]=node.cale(l[2],0,False,False)
            self.list.append([self.cale[2].lv(),self.cale[2],2])
        if not self.left:
            self.cale[3]=node.cale(l[3],0,False,False)
            self.list.append([self.cale[3].lv(),self.cale[3],3])
        if not self.top:
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
       
       
       
      
        
v,h=-4,4

obj=[[ 0 for x in range(-100,100)] for y in range(-100,100)]
nod=[[ 0 for x in range(-100,100)] for y in range(-100,100)]

for x in range(-5,5):
    for y in range(v,h):
        obj[x][y]=cube(x,y,45)
        obj[x][y].draw()
        



       


hower=ak.Turtle()
hower.penup()
hower.ht()
hower.speed(0)

hower1=ak.Turtle()
hower1.penup()
hower1.ht()
hower1.speed(0)

hower2=ak.Turtle()
hower2.penup()
hower2.ht()
hower2.speed(0)
class control:

            
            
    def __init__(self,control="none"):
        self.control=control
        self.firstRunPath=True
        self.size=45
        self.x=0
        self.y=0
        self.state="isFree"
        self.nodes={"null" : "null",}
        self.gasit=False
        self.block=0
        self.reset=True
        
    def resets(self):
        ak.clear()
        hower.clear()
        hower1.clear()
        hower2.clear()
        self.firstRunPath=True
        self.x=0
        self.y=0
        self.state="isreset"
        self.nodes={"null" : "null",}
        self.gasit=False
        self.block=0
        self.reset=False
        
        for x in range(-5,5):
            for y in range(-4,4):
                obj[x][y]=cube(x,y,45)
                obj[x][y].draw()    
    def setPos(self):
        self.position=obj[self.x][self.y].getposition()
        self.allpos=obj[self.x][self.y].getAllposition()
        self.half=obj[self.x][self.y].getHalfpos()
        
        print(self.position)
        print(self.allpos)
        print(self.half)
    
    
    def rightSet(self):
        if self.state=="isFree":
            try:
                self.x+=1
                self.position=(obj[self.x][self.y].getpositionxy())
                self.drawHower()
            except:
                print("invalid")
    def up(self):
        if self.state=="isFree":
            try:
                self.y+=1
                self.position=(obj[self.x][self.y].getpositionxy())
                self.drawHower()        
            except:
                print("invalid")    
    def down(self):
        if self.state=="isFree":
            try:
                self.y-=1
                self.position=(obj[self.x][self.y].getpositionxy())
                self.drawHower()
            except:
                print("invalid")
                
    def leftSet(self):
        if self.state=="isFree":
            try:
                self.x-=1
                self.position=(obj[self.x][self.y].getpositionxy())
                self.drawHower()
            except:
                print("invalid")

    def build(self,mode,color):
        if self.state=="isFree":
            self.mode=mode
            if self.mode=="True":
                print("a")
                obj[self.position[0]][self.position[1]].lock(True)
            elif self.mode=="False":    
                obj[self.position[0]][self.position[1]].lock(False)
            elif self.mode=="ako96":
                obj[self.position[0]][self.position[1]].Setswin(False)
            self.color=color
            hower1.penup()
            hower1.goto(self.position[0]*self.size,(self.position[1]+1)*self.size)
            hower1.pendown()
            
            hower1.fillcolor(self.color)
            hower1.begin_fill()
            hower1.goto(self.position[0]*self.size,self.position[1]*self.size)
            hower1.goto((self.position[0]+1)*self.size,self.position[1]*self.size)
            hower1.goto((self.position[0]+1)*self.size,(self.position[1]+1)*self.size)
            hower1.goto(self.position[0]*self.size,(self.position[1]+1)*self.size)
            hower1.goto(self.position[0]*self.size,(self.position[1]+1)*self.size)
            hower1.end_fill()
        
    def drawHower(self):
        hower.clear()
        print(self.position,obj[self.x][self.y].islock())
        hower.penup()
        hower.goto(self.position[0]*self.size,self.position[1]*self.size)
        hower.begin_fill()
        hower.fillcolor("red")
        hower.goto(self.position[0]*self.size,(self.position[1]+0.3)*self.size)
        hower.goto((self.position[0]+0.1)*self.size,(self.position[1]+0.3)*self.size)
        hower.goto((self.position[0]+0.1)*self.size,(self.position[1]+0.1)*self.size)
        hower.goto((self.position[0]+0.3)*self.size,(self.position[1]+0.1)*self.size)
        hower.goto((self.position[0]+0.3)*self.size,(self.position[1])*self.size)
        hower.goto(self.position[0]*self.size,self.position[1]*self.size)
        hower.end_fill()
        
        
        hower.penup()
        hower.goto(self.position[0]*self.size,(self.position[1]+1)*self.size)
        hower.begin_fill()
        hower.fillcolor("red")
        hower.goto((self.position[0]+0.3)*self.size,(self.position[1]+1)*self.size)
        hower.goto((self.position[0]+0.3)*self.size,(self.position[1]+0.9)*self.size)
        hower.goto((self.position[0]+0.1)*self.size,(self.position[1]+0.9)*self.size)
        hower.goto((self.position[0]+0.1)*self.size,(self.position[1]+0.7)*self.size)
        hower.goto((self.position[0]+0)*self.size,(self.position[1]+0.7)*self.size)
        hower.goto((self.position[0])*self.size,(self.position[1]+1)*self.size)
        hower.end_fill()
        
        
        
        hower.penup()
        hower.goto((self.position[0]+1)*self.size,(self.position[1])*self.size)
        hower.begin_fill()
        hower.fillcolor("red")
        hower.goto((self.position[0]+1)*self.size,(self.position[1]+0.3)*self.size)
        hower.goto((self.position[0]+0.9)*self.size,(self.position[1]+0.3)*self.size)
        hower.goto((self.position[0]+0.9)*self.size,(self.position[1]+0.1)*self.size)
        hower.goto((self.position[0]+0.7)*self.size,(self.position[1]+0.1)*self.size)
        hower.goto((self.position[0]+0.7)*self.size,(self.position[1]+0)*self.size)
        hower.goto((self.position[0]+1)*self.size,(self.position[1]+0)*self.size)
        hower.end_fill()
        
        
        hower.penup()
        hower.goto((self.position[0]+1)*self.size,(self.position[1]+1)*self.size)
        hower.begin_fill()
        hower.fillcolor("red")
        hower.goto((self.position[0]+1)*self.size,(self.position[1]+0.7)*self.size)
        hower.goto((self.position[0]+0.9)*self.size,(self.position[1]+0.7)*self.size)
        hower.goto((self.position[0]+0.9)*self.size,(self.position[1]+0.9)*self.size)
        hower.goto((self.position[0]+0.7)*self.size,(self.position[1]+0.9)*self.size)
        hower.goto((self.position[0]+0.7)*self.size,(self.position[1]+1)*self.size)
        hower.goto((self.position[0]+1)*self.size,(self.position[1]+1)*self.size)
        hower.end_fill()

        
    def buildPath(self,color,x,y):
        if True:
            self.position=[x,y]
            self.color=color
            hower2.penup()
            hower2.goto(self.position[0]*self.size,(self.position[1]+1)*self.size)
            hower2.pendown()
            
            hower2.fillcolor(self.color)
            hower2.begin_fill()
            hower2.goto(self.position[0]*self.size,self.position[1]*self.size)
            hower2.goto((self.position[0]+1)*self.size,self.position[1]*self.size)
            hower2.goto((self.position[0]+1)*self.size,(self.position[1]+1)*self.size)
            hower2.goto(self.position[0]*self.size,(self.position[1]+1)*self.size)
            hower2.goto(self.position[0]*self.size,(self.position[1]+1)*self.size)
            hower2.end_fill()
     
     
    def restate(self):
        self.x=0
        self.y=0
        
    def run(self,stated):
        self.buildPath("red",self.x,self.y)
        self.state="isRun"
        self.reset=stated
        while True:
            
            if self.reset==False:
                break
            
            if not obj[self.x][self.y].iswin():
                for x in range(-5,5):
                        for y in range(-4,4):
                            if obj[x][y].ispress() and not obj[x][y].islock():
                                self.buildPath("red",x,y)
                                
                break  
            
            if self.firstRunPath:
                self.memx=self.x
                self.memy=self.y
                self.firstRunPath=False
            hower.clear()
            try:
                self.top=(obj[self.x][self.y+1].islock())
                if not self.top:
                    self.top=(obj[self.x][self.y+1].ispress())
            except:
                self.top=True        
            
            try:
                self.right=(obj[self.x+1][self.y].islock())
                if not self.right:
                    self.right=(obj[self.x+1][self.y].ispress())
            except:
                self.right=True        
            
            try:
                self.bottom=(obj[self.x][self.y-1].islock())
                if not self.bottom:
                    self.bottom=(obj[self.x][self.y-1].ispress())
            except:
                self.bottom=True
            
            try:
                self.left=(obj[self.x-1][self.y].islock())
                if not self.left:
                    self.left=(obj[self.x-1][self.y].ispress())
            except:
                self.left=True
                
            """we got a full cover of area by check islock  or is press"""
            
            self.statesPath=[self.top,self.right,self.bottom,self.left]
            
            self.copyPath=self.statesPath.copy()
            self.stari=0
            
            nrmax=len(self.copyPath)
            
            for x in range(nrmax):
                d = self.copyPath.pop()
                if not d:
                    self.stari+=1
            if self.stari>=1:
                #print("node",self.statesPath)
                for c in self.nodes.keys():
                    #print((self.x,self.y),c)
                    if c==(self.x,self.y):
                        self.nodes[c].updateNode(self.statesPath)
                        self.next=self.nodes[c].gotWay()
                        self.gasit=True
                        break
                    else:
                        self.gasit=False
                      
                if not self.gasit:
                    
                    self.nodes[self.x,self.y]=node(self.x,self.y,self.statesPath)
                    self.next=self.nodes[self.x,self.y].gotWay()
                    
                
                if self.next==0:
                    #print("top")
                    #self.buildPath("red",self.x,self.y)
                    obj[self.x][self.y].press(True)
                    self.y+=1
                    #self.buildPath("red",self.x,self.y)
                    
                elif self.next==1:
                    #print("right")
                    #self.buildPath("red",self.x,self.y)
                    obj[self.x][self.y].press(True)
                    self.x+=1
                    #self.buildPath("red",self.x,self.y)
                    
                elif self.next==2:
                    #print("bottom")
                    #self.buildPath("red",self.x,self.y)
                    obj[self.x][self.y].press(True)
                    self.y-=1
                    #self.buildPath("red",self.x,self.y)
                    
                elif self.next==3:
                    #print("left")
                    #self.buildPath("red",self.x,self.y)
                    obj[self.x][self.y].press(True)
                    self.x-=1
                    #self.buildPath("red",self.x,self.y)
                    
                    
        
                # check a dict for node , if exist then run gotway
                #if doesn't exist then create one and update the dict or something
                

                
                
                #self.stari=0
            elif self.stari==0:
                self.block+=1
                self.nodes[c].updateNode(self.statesPath)
                self.next=self.nodes[c].gotWay()
                
                if self.block==3:
                    self.block=0    
                    #print("blocked",self.statesPath)
                    self.stari=0
                    for x in range(-5,5):
                        for y in range(-4,4):
                            if obj[x][y].ispress() and not obj[x][y].islock():
                                #self.buildPath("gray",x,y)
                                obj[x][y].press(False)
                                self.x=self.memx
                                self.y=self.memy
                        
                        
            else:
                print("cale libera",self.statesPath)
                self.stari=0
                
            self.state="isFree"    
            if self.reset==False:
                hower.clear()
                hower1.clear()
                hower2.clear()
"""work ,but to increase speed of progress we need to recommend free path ,or checked already paths .. 
    if a path is blocked then remove it from node and made it looks like is press or something     """
    
                                                        
        
al=control()
al.setPos()
al.drawHower()

def sus():
    al.up()
def jos():
    al.down()
def dreapta():
    al.rightSet()
def stanga():
    al.leftSet()
def space():
    al.build("True","cyan")
def remo():
    al.build("False","white")
def start():
    al.run(True)
def reset():
    al.resets()
def winner():
    al.build("ako96","green")
def restate():
    al.restate()
    
# run, reset 
#
# 
#
#


ak.onkeypress(sus,"Up")
ak.onkeypress(jos,"Down")
ak.onkeypress(stanga,"Left")
ak.onkeypress(dreapta,"Right")
ak.onkeypress(space,"space")
ak.onkeypress(remo,"r")
ak.onkeypress(start,"Return")
ak.onkeypress(winner,"w")
ak.onkeypress(restate,"l")
ak.onkeypress(reset,"e")

ak.listen()    
    
        
done()        