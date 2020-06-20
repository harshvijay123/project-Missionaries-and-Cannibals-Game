import turtle
import tkinter as tk
from tkinter import messagebox

class Drawer():
    X=600
    Y=400
    def __init__(self):
        self.window=tk.Tk()
        self.window.focus()
        self.window.protocol("WM_DELETE_WINDOW",lambda :self.Popup_info('Exit','We are taking you\n out from this.',1))
        self.popup=None
        self.window.bind('<Button-1>',self.close_popup)
        self.window.configure(background='black')
        self.window.geometry('1600x700')
        self.window.attributes('-fullscreen',1)
        self.window.resizable(False,False)
        self.board = tk.Canvas(self.window,width=1200,height=600,bg='black')               
        self.board.pack(fill=tk.BOTH,side=tk.TOP,padx=0,pady=0)
        self.help_str='''Help the 3 Cannibals(Red) and Missionaries(Green) move to the
other side of the lake. If the number of Cannibals is
larger than the number of Missionaries on either side
of the lake, the Missionaries will be eaten. Only Last comer
in the boat can be gotton off from the boat first and
there must always be a sailor to move the boat.'''

        
        

    class Draw_It():
        def __init__(self,drawer_obj):
            self.pen=turtle.RawTurtle(drawer_obj.board)
            self.pen.getscreen().tracer(5,0)
            self.pen.pu()
            self.pen.setpos(-drawer_obj.X , -drawer_obj.Y)
            self.pen.pd()
            self.pen.speed(100)
            self.pen.color('black','black')
            self.pen.begin_fill()
            self.pen.hideturtle()

            ## field co-ordinates

            self.field_x=2*(drawer_obj.X)+330
            self.field_y=drawer_obj.Y+300
            
            ## river co-ordinates
            self.river_x=-drawer_obj.X+300
            self.river_y=-drawer_obj.Y

            ## sun co-ordinates
            self.sun_x= drawer_obj.X+100
            self.sun_y= drawer_obj.Y-200
            self.sun_radius= drawer_obj.Y//10+10

            ## left pleatue co-ordinates -X,-Y+270

            self.left_pX= -(drawer_obj.X)
            self.left_pY= -(drawer_obj.Y)+270

            ## right pleatue co-ordinates  X+328,-Y+270

            self.right_pX= drawer_obj.X+328
            self.right_pY= -(drawer_obj.Y)+270

            ## tree co-ordinates

            self.tree_x=-(drawer_obj.X)+150
            self.tree_y=-(drawer_obj.Y)+270

        def draw_field(self):
            
            for i in range(2):
                self.pen.forward(self.field_x)
                self.pen.left(90)
                self.pen.forward(self.field_y)
                self.pen.left(90)
            self.pen.end_fill()

                
        def draw_river(self):
            self.pen.pu()
            self.pen.setpos(self.river_x,self.river_y)
            self.pen.pd()
            self.pen.color("deepskyblue",'deepskyblue')
            self.pen.begin_fill()
            self.pen.setpos(100,298)
            self.pen.setpos(255,298)
            self.pen.setpos(self.river_x+800,self.river_y)
            self.pen.setpos(self.river_x,self.river_y)
            self.pen.end_fill()

    ## Moon
        def draw_moon(self):
            self.pen.pu()
            self.pen.setpos(self.sun_x,self.sun_y)
            self.pen.color('white','white')
            self.pen.pd()
            self.pen.begin_fill()
            self.pen.circle(30)
            self.pen.end_fill()

        ## pleatue left -X,-Y+270
        def draw_left_pleatue(self):
            self.pen.pu()
            self.pen.setpos(self.left_pX,self.left_pY)
            self.pen.pd()
            self.pen.color('springgreen','springgreen')
            self.pen.begin_fill()
            self.pen.setpos(self.left_pX+454,self.left_pY)
            self.pen.setpos(self.river_x,self.river_y)
            self.pen.setpos(self.left_pX,self.left_pY-200)
            self.pen.setpos(self.left_pX,self.left_pY)
            self.pen.end_fill()


        ## pleatue right   X,-Y+380
        def draw_right_pleatue(self):
            self.pen.pu()
            self.pen.setpos(self.right_pX,self.right_pY)
            self.pen.color('springgreen','springgreen')
            self.pen.begin_fill()
            self.pen.pd()
            self.pen.setpos(self.right_pX-522,self.right_pY)
            self.pen.setpos(self.river_x+800,self.river_y)
            self.pen.setpos(self.right_pX,self.right_pY-380)
            self.pen.setpos(self.right_pX,self.right_pY)
            self.pen.end_fill()


        ## draw tree

        def Draw_tree(self,length):
            self.pen.pu()
            self.pen.setpos(self.tree_x,self.tree_y)
            self.pen.pd()
            self.pen.pensize(10)
            self.pen.color('saddlebrown')
            self.pen.speed(0)
            self.pen.left(90)
            def draw(l):
                if(l<5):
                    return
                else:
                    self.pen.forward(l)
                    self.pen.pensize(l/10)
                    self.pen.left(35)
                    draw(2*l/3)
                    self.pen.right(70)
                    self.pen.pensize(l/10)
                    draw(2*l/3)
                    self.pen.left(35)
                    self.pen.backward(l)
            draw(length)


    def please_draw(self):
        obj=self.Draw_It(self)
        obj.draw_field()
        obj.draw_river()
        obj.draw_moon()
        obj.draw_left_pleatue()
        obj.draw_right_pleatue()
        
        obj.Draw_tree(100)
        return obj

    def draw_marks(self,mark_lists,ob):
        ob.pen.pensize(5)

        
        ob.pen.color('darkgreen')
        l=[1,2,3,1,2,3]
        for i,co in enumerate(mark_lists[0],start=0):
            ob.pen.pu()
            ob.pen.setpos(co)
            ob.pen.pd()
            ob.pen.write(str(l[i]),font=('candara',20,'bold'))
        l=[4,5,6,4,5,6]   
        ob.pen.color('red')
        for i,co in enumerate(mark_lists[1],start=0):
            ob.pen.pu()
            ob.pen.setpos(co)
            ob.pen.pd()
            ob.pen.write(str(l[i]),font=('candara',20,'bold'))

            
        self.info_btn=tk.Button(self.board,text='Help',font=('candara',20),padx=0,pady=0,width=7,
                                bg='black',fg='deepskyblue',command=self.Popup_info)
        self.info_btn.place(x=2,y=0)

        self.exit=tk.Button(self.board,text='Exit',font=('candara',20),padx=0,pady=0,width=7,
                                bg='black',fg='deepskyblue',command= lambda :self.Popup_info('Exit','We are taking you\n out from this.',s))
        self.exit.place(x=1420,y=0)

        s='''1. You can move
Missionaries or Cannibals
by  double-clicking
on that.
2. You can move the boat
by press Enter-Key.'''
        self.how_to_play=tk.Button(self.board,text='How to play..!',font=('candara',20),padx=0,pady=0,width=14,
                                bg='black',fg='deepskyblue',command= lambda :self.Popup_info('How to play..!',s))
        self.how_to_play.place(x=670,y=0)
        self.Popup_info()
        

        

    def Popup_info(self,title='Help',t=None,flag=None):
        self.window.bell()
        if self.popup:self.popup.destroy()
        if not t: t=self.help_str
        self.popup=tk.Toplevel(self.window)
        self.popup.protocol("WM_DELETE_WINDOW",self.fxn)
        self.popup.title(title)
        self.popup.configure(background='black')
        self.popup.geometry('600x300+450+100')
        self.info_btn['state']=tk.DISABLED
        self.exit['state']=tk.DISABLED
        self.how_to_play['state']=tk.DISABLED
        self.popup.transient(self.window)
        text_label=tk.Label(self.popup,text=t,bg='black',fg='deepskyblue',font=('candara',15,'bold'))
        text_label.pack(side='left',fill=tk.BOTH,expand=tk.YES)
        tk.Button(text_label,text='Okay',command=lambda : self.fxn(flag),font=('candara',15,'bold'),
                  bg='black',fg='darkgreen',width=10).pack(side='bottom',pady=5)
        self.popup.mainloop()


    def fxn(self,flag=None):
        if flag:
            self.window.destroy()
            return
        self.popup.destroy()
        self.info_btn['state']=tk.NORMAL
        self.exit['state']=tk.NORMAL
        self.how_to_play['state']=tk.NORMAL

    def close_popup(self,event):
        if self.popup:
            self.fxn()
