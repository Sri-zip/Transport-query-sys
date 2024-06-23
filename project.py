from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk,messagebox
import pymysql


#defining the fuctions udes in the code
def traintqs():
    win2.destroy()
    import TrainTQS

def bustqs():
    win2.destroy()
    import BusTQ
    

def loginfn():
    global win
    if userentry.get()=='' or passentry.get()=='':
        messagebox.showerror('ERROR','Fields cannot be empty')
    elif userentry.get()=='a' and passentry.get()=='12345':
        messagebox.showinfo('Welcome','You have successfully logged in')
        win.destroy()
        global win2
        def about():
            def info():
                f=open('info.txt','w')
                f.write('The Transport Query System with MySQL-Python Connectivity is an application project designed to streamline and simplify the process of managing and querying transportation-related data.\n This system will provide a user-friendly interface for users to interact with a MySQL database through a Python application. \n It aims to improve the efficiency of handling transportation data, such as routes, schedules, and vehicle information,\n while also enabling users to retrieve relevant information quickly and accurately..\n This project consists of 2 separate databases, one for Bus Transport and the other for Train Transport. Both the databases contain 2 tables which are related to each other.\n Using the interface user can Add data, Display data, Search data, Delete data, Update data.\n This project addresses the need for better transportation data management, benefiting both transportation authorities and the general public.')
                f.close()
                f=open('info.txt','r')
                s=f.read()
                bi_window=Toplevel(win2)
                Label(bi_window,text=s,font=('times new roman',13),bg='#FEFFAC').pack()
                Button(bi_window,text='CLOSE',bg='#FEFFAC',fg='black',width=20,command=lambda:[bi_window.destroy()]).pack()
                f.close()
            info()

        def trainTQ():
            messagebox.showinfo('Confirm','Do you confirm to choose Train Transport?')
            traintqs()
        def busTQ():
            messagebox.showinfo('Confirm','Do you confirm to choose Bus Transport?')
            bustqs()
        #choose window
        win2=Tk()
        win2.geometry('1280x700+0+0')
        win2.title('Transport Query System')
        win2.resizable(False,False) #disabling the maximise button

        bgimg=ImageTk.PhotoImage(file='Fhomepg.jpg') #importimg the background image
        bglabel=Label(win2,image=bgimg) #added the background image
        bglabel.place(x=0,y=0)

        busbt=Button(win2,text='Bus Transport',font=('times new roman',17,'bold'),width=15  #Button for the bus transport
             ,fg='white',bg='#501511',cursor='hand2',command=busTQ)
        busbt.place(x=250,y=250)
        trainbt=Button(win2,text='Train Transport',font=('times new roman',17,'bold'),width=15  #Button for the train transport
             ,fg='white',bg='#501511',cursor='hand2',command=trainTQ)
        trainbt.place(x=900,y=250)


        info=Button(win2,text='About',font=('times new roman',17,'bold'),width=5  #Button for the bus transport
             ,fg='white',bg='#501511',cursor='hand2',command=about)
        info.place(x=1150,y=600)
        win2.mainloop()
    else:
        messagebox.showerror('ERROR','Wrong password or username')


win=Tk() #creation of a window
win.geometry('1280x700+0+0')
win.title('LOGIN')
win.resizable(False,False) #disabling the maximise button

bgimg=ImageTk.PhotoImage(file='image-1280x700.jpg') #importimg the background image
bglabel=Label(win,image=bgimg) #added the background image
bglabel.place(x=0,y=0) #placing of the background image

#the username,password and the other used images on the login page needs a frame
#creation of the frame
login=Frame(win,bg='#FB9E39')
login.place(x=400,y=150)

    #uploading the user image
logoimg=PhotoImage(file='usernew.png')
logolabel=Label(login,image=logoimg)
logolabel.grid(row=0,column=0,columnspan=2,pady=10)

    #creation of user label
userimg=PhotoImage(file='profile.png')
userlabel=Label(login,image=userimg,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='#FB9E39')
userlabel.grid(row=1,column=0,pady=10,padx=20)

userentry=Entry(login,font=('consolas',20,'bold'),bd=5)
userentry.grid(row=1,column=1,pady=10,padx=20)

    #creation of pass label
passimg=PhotoImage(file='lock.png')
passlabel=Label(login,image=passimg,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='#FB9E39')
passlabel.grid(row=2,column=0,pady=10,padx=20)

passentry=Entry(login,font=('consolas',20,'bold'),bd=5,show='*')
passentry.grid(row=2,column=1,pady=10,padx=20)

    #creation of login label
logbt=Button(login,text='Login',font=('times new roman',17,'bold'),width=15
                ,fg='white',bg='#501511',cursor='hand2',command=loginfn)
logbt.grid(row=3,column=1,pady=10)

win.mainloop() 
