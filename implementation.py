import turtle
import tkinter as tk


class Implementation():
    def __init__(self,obj):
        self.Draw_it_obj=obj
        self.Turtle=turtle.RawTurtle(obj.board)
        self.Turtle.getscreen().tracer(1,0)
        self.Turtle.hideturtle()
        self.Turtle.shape('triangle')
        self.start_x=obj.X-260
        self.start_y=-obj.Y+280
        self.Turtle.pu()
        self.Turtle.setpos(self.start_x,self.start_y)
        self.Turtle.turtlesize(6)
        self.Turtle.right(180)
        self.Turtle.speed(1)
        self.is_last=False
        self.Turtle.showturtle()
        self.draw_objects()


    def draw_objects(self):        
        self.boat_status='right'
        self.count=0

        self.result_data={'right':([],[]),'left':([],[])}
        self.boat_member=[]        
        self.Missionaries=[]
        p=0
        q=60
        for i in range(3):
            m=turtle.RawTurtle(self.Draw_it_obj.board)
            m.hideturtle()
            m.speed(10)
            m.right(180)
            m.shape('circle')
            m.color('green')
            m.turtlesize(1)
            m.pu()
            m.setpos(self.start_x+100+p,self.start_y)
            m.showturtle()
            m.speed(500)
            d={}
            d['missionaries '+str(i+1)]=m
            d['right']=(self.start_x+100+p,self.start_y)
            d['left']=(self.start_x-600+q,self.start_y)
            d['pos']='right'
            d['type']='M'
            self.Missionaries.append(d)
            self.result_data['right'][0].append('M')
            p+=30
            q-=30
               
        self.Cannibals=[]
        for i in range(3):
            
            c=turtle.RawTurtle(self.Draw_it_obj.board)
            c.hideturtle()
            c.speed(10)
            c.right(180)
            c.shape('circle')
            c.color('Red')
            c.turtlesize(1)
            c.pu()
            c.setpos(self.start_x+100+p,self.start_y)  # side :-  x+=110,y+=5   side 2:-  x-=900,y-=70
            c.showturtle()

            d={}
            d['cannibals '+str(i+1)]=c
            d['right']=(self.start_x+100+p,self.start_y)
            d['left']=(self.start_x-600+q,self.start_y)
            d['pos']='right'
            d['type']='C'
            self.Cannibals.append(d)
            self.result_data['right'][1].append('C')
            p+=30
            q-=30

        self.Miss_mark_list=[]
        self.Cannib_mark_list=[]

        
        for i in self.Missionaries:
            co=i['right']
            co=co[0],co[1]-40
            self.Miss_mark_list.append(co)
        
        for i in self.Cannibals:
            co=i['right']
            co=co[0],co[1]-40
            self.Cannib_mark_list.append(co)  
            
        for i in self.Missionaries:
            co=i['left']
            co=co[0],co[1]-40
            self.Miss_mark_list.append(co)
        
        for i in self.Cannibals:
            co=i['left']
            co=co[0],co[1]-40
            self.Cannib_mark_list.append(co)

        self.Turtle.getscreen().tracer(1,5)

    def Popup_info(self,title,t):
        self.Draw_it_obj.window.bell()
        self.popup=tk.Toplevel(self.Draw_it_obj.window)
        self.popup.title(title)
        self.popup.protocol("WM_DELETE_WINDOW",self.fxn1)
        self.popup.configure(background='black')
        self.popup.geometry('600x300+450+100')
        self.popup.transient(self.Draw_it_obj.window)
        text_label=tk.Label(self.popup,text=t,bg='black',fg='deepskyblue',font=('candara',15,'bold'))
        text_label.pack(side='right',fill=tk.BOTH,expand=tk.YES)

        tk.Button(text_label,text='Reset',command=self.fxn2,font=('candara',15,'bold'),
                  bg='black',fg='darkgreen',width=10).place(x=150,y=230)
        tk.Button(text_label,text='Exit',command=self.fxn1,font=('candara',15,'bold'),
                  bg='black',fg='darkgreen',width=10).place(x=300,y=230)
        self.popup.mainloop()


        

    def fxn1(self):
        self.Draw_it_obj.window.destroy()




        
    def fxn2(self):
        self.Turtle.getscreen().tracer(1,0)
        self.popup.destroy()
        self.Turtle.hideturtle()
        self.Turtle.setpos(self.start_x,self.start_y)
        self.Turtle.right(180)
        self.boat_status='right'
        self.count=0
        self.Turtle.showturtle()

        for index,i in enumerate(self.Missionaries):
            i['missionaries '+str(index+1)].hideturtle()

        for index,i in enumerate(self.Cannibals):
            i['cannibals '+str(index+1)].hideturtle()
        self.draw_objects()
        
        
        
    def Is_win(self,pre):
        a = len(self.result_data[pre][0])
        b = len(self.result_data[pre][1])
        if a>0 and a < b:
            self.Popup_info('Game Over','Oops..!!\n{} Missionary(/ies) of side {}\ngonna be eaten by\n {} Cannibal(/s).'.format(a,pre,b))
            

            
        
    def Move(self):
        if 2<=len(self.boat_member)<5:                                  
            self.Turtle.speed(5)
            p=-40
            for i in self.boat_member[::2]:
                i.hideturtle()
                i.forward(400+p)
                p+=60
            self.Turtle.forward(400)
            self.Turtle.right(180)
            for i in self.boat_member[::2]:
                i.right(180)
                i.showturtle()

            pre=self.boat_status
            if self.boat_status=='right':
                self.boat_status='left'
            else:
                self.boat_status='right'
                
            self.Is_win(pre)


            
    def Shift(self,event):
        x=event.x
        y=event.y
        x1,y1=self.Turtle.position()
        if self.boat_status=='right':
            self.boat_pos=[(x1-20,y1),(x1+10,y1)]
        else:
            self.boat_pos=[(x1+20,y1),(x1-10,y1)]

        '''these are the condition when boat is on the righr side and
            cannibals and missionaries are allowed to get into boat for at most two of them'''

        

        #for first Missionaries
        if ((x>=1033 and x<=1053) or (x>=392 and x<=412))  and (y>=414 and  y<=430) and (self.count<2) and (self.boat_status==self.Missionaries[0]['pos']):
            self.Missionaries[0]['missionaries 1'].setpos(self.boat_pos[self.count])
            self.Missionaries[0]['pos']='boat'
            self.boat_member.append(self.Missionaries[0]['missionaries 1'])
            self.boat_member.append(self.Missionaries[0])
            self.count+=1
            self.result_data[self.boat_status][0].pop(-1)
                
                    
        #for second Missionaries   
        elif ((x>=1062 and x<=1082) or (x>=362 and x<=382)) and (y>=414 and y<=430) and (self.count<2) and (self.boat_status==self.Missionaries[1]['pos']):
            self.Missionaries[1]['missionaries 2'].setpos(self.boat_pos[self.count])
            self.Missionaries[1]['pos']='boat'
            self.boat_member.append(self.Missionaries[1]['missionaries 2'])
            self.boat_member.append(self.Missionaries[1])
            self.result_data[self.boat_status][0].pop(-1)
            
            self.count+=1
            

            

        #for third Missionaries
        elif ((x>=1092 and x<1112) or (x>=332 and x<=352)) and (y>=414 and y<=430) and (self.count<2) and (self.boat_status==self.Missionaries[2]['pos']):
            self.Missionaries[2]['missionaries 3'].setpos(self.boat_pos[self.count])
            self.Missionaries[2]['pos']='boat'
            self.boat_member.append(self.Missionaries[2]['missionaries 3'])
            self.boat_member.append(self.Missionaries[2])
            self.result_data[self.boat_status][0].pop(-1)

            self.count+=1
            
            


        #for first cannibals
        elif ((x>=1122 and x<1142) or (x>=302 and x<=322)) and (y>=414 and y<=430) and (self.count<2) and (self.boat_status==self.Cannibals[0]['pos']):
            self.Cannibals[0]['cannibals 1'].setpos(self.boat_pos[self.count])
            self.Cannibals[0]['pos']='boat'
            self.boat_member.append(self.Cannibals[0]['cannibals 1'])
            self.boat_member.append(self.Cannibals[0])
            self.result_data[self.boat_status][1].pop(-1)
            
            self.count+=1
            

            

        #for second cannibals
        elif ((x>=1152 and x<=1172) or (x>=272 and x<=292)) and (y>=414 and y<=430) and (self.count<2) and (self.boat_status==self.Cannibals[1]['pos']):

            self.Cannibals[1]['cannibals 2'].setpos(self.boat_pos[self.count])
            self.Cannibals[1]['pos']='boat'
            self.boat_member.append(self.Cannibals[1]['cannibals 2'])
            self.boat_member.append(self.Cannibals[1])
            self.result_data[self.boat_status][1].pop(-1)
            
            self.count+=1
            


            
        #for third cannibals
        elif ((x>=1182 and x<=1202) or (x>=242 and x<=262)) and (y>=414 and y<=430) and (self.count<2) and (self.boat_status==self.Cannibals[2]['pos']):
            self.Cannibals[2]['cannibals 3'].setpos(self.boat_pos[self.count])
            self.Cannibals[2]['pos']='boat'
            self.boat_member.append(self.Cannibals[2]['cannibals 3'])
            self.boat_member.append(self.Cannibals[2])
            self.result_data[self.boat_status][1].pop(-1)
            
            self.count+=1

        '''this code is get invoked when user wants to get down missionaries or cannibals from the boat'''


        if ((x>=912 and x<=932) or (x>=552 and x<=582)) and (y>=414 and y<=430) and len(self.boat_member)!=4:
            
            self.boat_member[0].setpos(self.boat_member[1][self.boat_status])
            self.boat_member[1]['pos']=self.boat_status

            
            if self.boat_member[1]['type']=='M' : self.result_data[self.boat_status][0].append('M')
            else : self.result_data[self.boat_status][1].append('C')

            self.boat_member.pop(0)
            self.boat_member.pop(0)
            self.count-=1

            if len(self.result_data['left'][0])==3 and len(self.result_data['left'][1])==3:
                self.Popup_info('Congratulation','Yeah...!\nYou won.')
            
        elif ((x>=942 and x<=962) or (x>=522 and x<=542)) and (y>=414 and y<=430) and len(self.boat_member)>0:
            self.boat_member[-2].setpos(self.boat_member[-1][self.boat_status])
            self.boat_member[-1]['pos']=self.boat_status

            if self.boat_member[-1]['type']=='M' : self.result_data[self.boat_status][0].append('M')
            else : self.result_data[self.boat_status][1].append('C')

            self.boat_member.pop(-1)
            self.boat_member.pop(-1)
            self.count-=1


            if len(self.result_data['left'][0])==3 and len(self.result_data['left'][1])==3:
                self.Popup_info('Congratulation','Yeah...!\nYou won.')
            

            

    def Start(self,obj):
        obj.window.bind('<Return>',lambda event:self.Move())
        obj.board.bind('<Double-1>',lambda event:self.Shift(event))
        return self.Miss_mark_list,self.Cannib_mark_list
            
        
     
