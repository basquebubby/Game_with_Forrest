from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=1200,height=600, background='grey')
drawpad.grid(row=0, column=0)

player_3d = drawpad.create_polygon  ((535,590),(535,490),(560,465),(585,465),(585,450),(575,440),(575,400),(585,390),                                                                                                                                                                     (635,390),(((625,400)),(635,390)),(645,400),(((635,410)),(645,400)),(645,440),(635,450),(635,465),(((625,475)),(635,465)),(660,465),(((650,475)),(660,465)),(685,490),(((675,500)),(685,490)),(685,590),(675,599), fill='darkgrey',outline='black')
player_main = drawpad.create_polygon((525,600),(525,500),(550,475),(575,475),(575,460),(565,450),(565,410),(575,400),((590,400),(590,420),(588,420),(588,424),(592,424),(592,420),(590,420),(590,400)),((610,400),(610,420),(608,420),(608,424),(612,424),(612,420),(610,420),(610,400)), (625,400),                        (635,410),                        (635,450),(625,460),(625,475),                        (650,475),                        (675,500),                        (675,600), fill='black')
#x1,x2,x3,x4,x29,x30,x31,and x32 are the body
#x5,x6,x7,x8,,x9,x16,x17,x24,x25,x26,x27, and x28 are the head w/out the eyes
#x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y16,x17,y17,x18,y18,x19,y19,x20,y20,x21,y21,x22,y22,x23,x24,y24,x25,y25,x26,y26,x27,y27,x28,y28,x29,y29,x30,y30,x31,y31,x32,y32 = drawpad.coords(player_main)
#dx1,dy1,dx2,dy2,dx3,dy3,dx4,dy4,dx5,dy5,dx6,dy6,dx7,dy7,dx8,dy8,dx9,dy9,dx10,dy10,dx11,dy11,dx12,dy12,dx13,dy13,dx14,dy14,dx15,dy16,dx17,dy17,dx18,dy18,dx19,dy19,dx20,dy20,dx21,dy21,dx22,dy22,dx23,dy23,dx24,dy24,dx25,dy25,dx26,dy26,dx27,dy27 = drawpad.coords(player_3d)

enemy_3d = drawpad.create_polygon(((((860,290),(810,240)),((810,140),(860,90)))),     ((910,90),   ((910,115),((885,165)),(835,190),((885,215)),(910,265),((935,215)),(985,190),((935,165)),(910,115)),  (910,90)),     ((((960,90) ,(1010,140)),((1010,240),(960,290)))),fill='white')
enemy_main = drawpad.create_polygon  (((((850,300),(800,250)),((800,150),(850,100)))),    ((900,100),  ((900,125),((875,175)),(825,200),((875,225)),(900,275),((925,225)),(975,200),((925,175)),(900,125)),  (900,100)),    ((((950,100),(1000,150)),((1000,250),(950,300)))),fill='black')


fireball = drawpad.create_oval(0,0,30,30, fill='red',outline='yellow')
sword = drawpad.create_polygon((0,100),(0,90),(5,90),(30,65),(15,55),(20,50),(30,60),(100,0),(40,70),(50,80),(45,85),(35,70),(10,95),(10,100),(0,100))
# need bag, score, health, 

class MyApp:
	playerHealth = 100
	enemyHealth = 100
	swordDamge = 5
	fireballDamage = 15
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    self.button = Button(self.myContainer1)
       	    self.button.configure(text="botton", background= "green")
       	    self.button.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.button.bind("<Button-1>", self.button)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
            self.animatefireball()
            self.animatesword()
	
	def animatefireball(self):
	    global drawpad
	    global player_main
	    global player_3d
	    global enemy_main
	    global enemy_3d
	    global fireball
	    
        def animatesword(self):
            global drawpdad
            global player_main
            global player_3d
            global enemy_main
	    global enemy_3d
            global sword
            
	def button(self, event):   
	    
        while playerHealth >= 0:
            #bla bla bla
            #game stuff
            #Whats goin' on         
        
#app = MyApp(root)

root.mainloop()