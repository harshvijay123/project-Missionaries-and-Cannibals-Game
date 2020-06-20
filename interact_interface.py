from tkinter import *

class Interact():
    background="black"
    foreground="deepskyblue"
    font='Arial'
    def __init__(self):

        
        self.count=0
        self.root=Tk()
        self.root.attributes('-fullscreen',1)
        self.root.protocol("WM_DELETE_WINDOW",self.Popup_info)
        self.f1=Frame(self.root)

                                                                   
        self.label=Label(self.root,bg=self.background,text='Missionaries And Cannibals\n'+"_"*100,height=100,width=100,
                fg=self.foreground,font=('candara',70,'bold'),anchor='n',pady=20,padx=100)                                                                                                                     
        self.label.pack(fill=BOTH,expand=YES)
                                                                   
        self.listbox=Listbox(self.root)
        #Double press Right-Button 
        self.label.bind('<Double-3>',lambda event:self.f(event) if self.count==0 else self.place(event))
        self.label.bind('<Button-1>',lambda event:self.listbox.destroy())
        self.label.bind('<Alt-Key-F4>',lambda event: self.close_it)

        self.skip=Label(self.root,text='Skip(Alt+F4)',font=('candara',20),padx=0,pady=0,width=20,
                                bg='black',fg='deepskyblue')
        self.skip.place(x=1300,y=0)




        self.Interact_frame=Frame(self.root,bg=self.background,height=500,width=400)
        self.Interact_frame.place(x=550,y=200)


        
        self.frame1=Frame(self.Interact_frame,bg=self.background,height=60,width=400)

        self.login=Button(self.frame1,text='Login',bg=self.background,fg=self.foreground,height=2,width=15,
                          font=(self.font,15,'bold'),command=self.Login_fxn)
        self.login.pack(side='left')
        self.sign_up=Button(self.frame1,text='Sign-up',bg=self.background,fg=self.foreground,height=2,width=15,
                            font=(self.font,15,'bold'),command =self.Signup_fxn)
        self.sign_up.pack(side='left')
        self.frame1.pack(side='top',padx=0,pady=0)
        self.f0=None
        self.f3=None

        self.root.mainloop()
            


    def destroy(self,event):
        d={0:self.root.destroy,1:self.root.iconify}
        d[self.listbox.curselection()[0]]()
        return


    def f(self,event):
        self.listbox=Listbox(self.root)
        self.count=1
        self.listbox.place(x=event.x,y=event.y)
        l=[]
        self.listbox.insert(1,'Exit')
        self.listbox.insert(2,'minimize')
        self.listbox.bind('<<ListboxSelect>>',self.destroy)

        
    def place(self,event):
        self.listbox.destroy()
        self.f(event)


    def Popup_info(self):
        t='Without being logged-in\nyou won\'t be able\nto see the answer.'
        self.root.bell()
        self.popup=Toplevel(self.root)
        self.popup.title('Skip')
        self.popup.configure(background='black')
        self.popup.geometry('600x300+450+100')
        self.popup.transient(self.root)
        text_label=Label(self.popup,text=t,bg='black',fg='deepskyblue',font=('candara',15,'bold'))
        text_label.pack(side='right',fill=BOTH,expand=YES)
        Button(text_label,text='Okay',command=self.fxn,font=('candara',15,'bold'),
                  bg='black',fg='darkgreen',width=10).pack(side='bottom',pady=5)
        self.popup.mainloop()


    def fxn(self):
        self.popup.destroy()
        import Animation
        Animation.main(self.root)
        self.root.destroy()

    def Login_fxn(self):
        global login,sign_up,Interact_frame
        self.login.destroy()
        self.sign_up.destroy()
        self.Interact_frame.destroy()
    
        self.Interact_frame=Frame(self.root,bg=self.background,height=500,width=400)
        self.Interact_frame.place(x=550,y=200)
    


        self.f0=Frame(self.Interact_frame,height=400,width=400,bg=self.background)
        self.label=Label(self.f0,text='Login-page',font=(self.font,25),bg=self.foreground,fg="white")
        self.label.pack(fill=BOTH,side='top')
        self.f0.pack(fill=BOTH)



        self.f1=Frame(self.Interact_frame,height=400,width=400,bg=self.background)
        self.name_label=Label(self.f1,text='User-name',font=(self.font,15),bg=self.background,justify='left',fg=self.foreground)
        self.name_label.pack(fill=BOTH,pady=10,side='left')
        self.name_entry=Entry(self.f1,font=(self.font,15),bg=self.background,fg=self.foreground,bd=2,
                              insertbackground=self.foreground)
        self.name_entry.pack(fill=BOTH,pady=10,side='left',padx=10)
        self.f1.pack(fill=BOTH,padx=5,pady=5)



        self.f2=Frame(self.Interact_frame,height=400,width=400,bg=self.background)

        self.password_label=Label(self.f2,text='Password ',font=(self.font,15),bg=self.background,justify='left',fg=self.foreground)
        self.password_label.pack(fill=BOTH,side='left',pady=10)

        self.password_entry=Entry(self.f2,show='\a',bd=2,bg=self.background,font=(self.font,15),fg=self.foreground,
                                  insertbackground=self.foreground)
        self.password_entry.pack(fill=BOTH,pady=10,side='left',padx=10)

        self.login_button=Button(self.f2,text='Login',justify='center',height=1,width=7,font=(self.font,12,'bold'),
                                bg=self.background,fg=self.foreground,padx=0,pady=0)
        self.login_button.pack(side='left',padx=10,pady=10)

        self.Sign_up=Button(self.Interact_frame,text='Wanna Signup..?',justify='center',height=2,width=7,padx=0,pady=0,
                           font=(self.font,12,'bold'),bg=self.background,fg=self.foreground,command=self.Signup_fxn)
        self.Sign_up.pack(side='bottom',padx=100,pady=10,fill=BOTH)

        self.f2.pack(fill=BOTH,padx=5,pady=5)

    


    def Signup_fxn(self):
        self.login.destroy()
        self.sign_up.destroy()
        self.Interact_frame.destroy()
    
        self.Interact_frame=Frame(self.root,bg=self.background,height=500,width=400)
        self.Interact_frame.place(x=550,y=200)
    


        self.f0=Frame(self.Interact_frame,height=400,width=400,bg=self.background)
        self.label=Label(self.f0,text='Sign-up page',font=(self.font,25),bg=self.foreground,fg="white")
        self.label.pack(fill=BOTH,side='top')
        self.f0.pack(fill=BOTH)



        self.f1=Frame(self.Interact_frame,height=400,width=400,bg=self.background)
        self.name_label=Label(self.f1,text='User-name',font=(self.font,15),bg=self.background,justify='left',fg=self.foreground)
        self.name_label.pack(fill=BOTH,pady=10,side='left')
        self.name_entry=Entry(self.f1,bd=2,font=(self.font,15),bg=self.background,fg=self.foreground,insertbackground='white')
        self.name_entry.pack(fill=BOTH,pady=10,side='left',padx=10)
        self.f1.pack(fill=BOTH,padx=5,pady=5)



        self.f2=Frame(self.Interact_frame,height=400,width=400,bg=self.background)

        self.mobile_label=Label(self.f2,text='Phone      ',font=(self.font,15),bg=self.background,justify='left',fg=self.foreground)
        self.mobile_label.pack(fill=BOTH,pady=10,side='left')
        self.mobile_entry=Entry(self.f2,bd=2,font=(self.font,15),bg=self.background,fg=self.foreground,insertbackground='white')
        self.mobile_entry.pack(fill=BOTH,pady=10,side='left',padx=10)

        self.f2.pack(fill=BOTH,padx=5,pady=5)


        self.f3=Frame(self.Interact_frame,height=400,width=400,bg=self.background)

        self.email_label=Label(self.f3,text='e-mail      ',font=(self.font,15),bg=self.background,justify='left',fg=self.foreground)
        self.email_label.pack(fill=BOTH,side='left',pady=10)

        self.email_entry=Entry(self.f3,bd=2,bg=self.background,font=(self.font,15),fg=self.foreground,insertbackground='white')
        self.email_entry.pack(fill=BOTH,pady=10,side='left',padx=10)


    
        self.f3.pack(fill=BOTH,padx=5,pady=5)
    

        self.f4=Frame(self.Interact_frame,height=400,width=400,bg=self.background)

        self.password_label=Label(self.f4,text='Password ',font=(self.font,15),bg=self.background,justify='left',fg=self.foreground)
        self.password_label.pack(fill=BOTH,side='left',pady=10)

        self.password_entry=Entry(self.f4,show='.',bd=2,bg=self.background,font=(self.font,15,'bold'),fg=self.foreground,insertbackground='white')
        self.password_entry.pack(fill=BOTH,pady=10,side='left',padx=10)

    
        self.done_button=Button(self.f4,text='Done',justify='center',height=1,width=7,font=(self.font,12,'bold'),bg=self.background,
                       fg=self.foreground,command=self.Login_fxn)
        self.done_button.pack(side='left',padx=10,pady=10)
    


        self.Sign_up=Button(self.Interact_frame,text='Wanna Login..?',justify='center',height=2,width=7,
                            font=(self.font,12,'bold'),bg=self.background,fg=self.foreground,command=self.Login_fxn)
        self.Sign_up.pack(side='bottom',padx=100,pady=10,fill=BOTH)

        self.f4.pack(fill=BOTH,padx=5,pady=5)
    

if __name__=="__main__":
    i=Interact()
