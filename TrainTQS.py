#database- traindb
from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk
import pymysql
#functionality
#backwin
global win2
def backwin():
    def traintqs():
        win2.destroy()
        import TrainTQS
    def bustqs():
        win2.destroy()
        import BusTQ
    win2=Tk()
    win2.geometry('1280x700+0+0')
    win2.title('Transport Query System')
    win2.resizable(False,False) #disabling the maximise button

    bgimg=ImageTk.PhotoImage(file='Fhomepg.jpg') #importimg the background image
    bglabel=Label(win2,image=bgimg) #added the background image
    bglabel.place(x=0,y=0)

    busbt=Button(win2,text='Bus Transport',font=('times new roman',17,'bold'),width=15  #Button for the bus transport
             ,fg='white',bg='#501511',cursor='hand2',command=bustqs)
    busbt.place(x=250,y=250)
    trainbt=Button(win2,text='Train Transport',font=('times new roman',17,'bold'),width=15  #Button for the train transport
             ,fg='white',bg='#501511',cursor='hand2',command=traintqs)
    trainbt.place(x=900,y=250)


    info=Button(win2,text='About',font=('times new roman',17,'bold'),width=5  #Button for the bus transport
             ,fg='white',bg='#501511',cursor='hand2')
    info.place(x=1150,y=600)
    win2.mainloop()
#exit
def exit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root1.destroy()
        backwin()
    else:
        pass
#update
def update():
            
    def upd():
        id_inp = identry.get()
        name_inp=nameentry.get()
        ori_inp=orientry.get()
        desinp = desentry.get()
        depinp = depentry.get()
        arvinp = arventry.get()
        tripinp = tripidentry.get()
        fareinp=fareentry.get()
        
        query = 'update trainmain set TrainName=%s,Source=%s,Destination=%s,DeptDate=%s,ArrivalDate=%s where TrainNo=%s'
        values = (name_inp,ori_inp,desinp,depinp,arvinp,id_inp)
        mycursor.execute(query,values)
        query = 'update traindetail set TripID=%s,TrainFare=%s where TrainNo=%s'
        values = (tripinp,fareinp,id_inp)
        mycursor.execute(query,values)
        con.commit()
        messagebox.showinfo('Notification','UPDATED SUCCESSFULLY')
        traintable.delete(*traintable.get_children())
        query = 'Select * from trainmain natural join traindetail'
        mycursor.execute(query)
        res = mycursor.fetchall()
        traintable.delete(*traintable.get_children())
        for data in res:
            datalist=list(data)
            traintable.insert('',END,values=datalist)
        upd_win.destroy()
                                                
    upd_win=Toplevel()
    upd_win.grab_set()
    color='#FEFFAC'
    upd_win.configure(bg=color)
    upd_win.resizable(False,False)
    idlb=Label(upd_win,text='TrainNo',font=('Times New Roman',15,'bold'),bg=color)
    idlb.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    identry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    identry.grid(row=0,column=1,padx=10,pady=20)

    namelb=Label(upd_win,text='Train Name',font=('Times New Roman',15,'bold'),bg=color)
    namelb.grid(row=1,column=0,sticky=W,padx=30,pady=15)
    nameentry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    nameentry.grid(row=1,column=1,padx=10,pady=20)

    orilb=Label(upd_win,text='Origin',font=('Times New Roman',15,'bold'),bg=color)
    orilb.grid(row=2,column=0,sticky=W,padx=30,pady=15)
    orientry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    orientry.grid(row=2,column=1,padx=10,pady=20)

    deslb=Label(upd_win,text='Destination',font=('Times New Roman',15,'bold'),bg=color)
    deslb.grid(row=3,column=0,sticky=W,padx=30,pady=15)
    desentry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    desentry.grid(row=3,column=1,padx=10,pady=20)

    
    deplb=Label(upd_win,text='Departure Date',font=('Times New Roman',15,'bold'),bg=color)
    deplb.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    depentry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    depentry.grid(row=4,column=1,padx=10,pady=20)

    
    arvlb=Label(upd_win,text='Arrival Date',font=('Times New Roman',15,'bold'),bg=color)
    arvlb.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    arventry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    arventry.grid(row=5,column=1,padx=10,pady=20)

    tripidlb=Label(upd_win,text='Trip Id',font=('Times New Roman',15,'bold'),bg=color)
    tripidlb.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    tripidentry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    tripidentry.grid(row=6,column=1,padx=10,pady=20)

    farelb=Label(upd_win,text='Train Fare',font=('Times New Roman',15,'bold'),bg=color)
    farelb.grid(row=7,column=0,padx=30,pady=15,sticky=W)
    fareentry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    fareentry.grid(row=7,column=1,padx=10,pady=20)


    updbt=Button(upd_win,text='UPDATE DATA',font=('Times new roman',12,'bold'),width=15,fg='black',bg='#C23373',command=upd)
    updbt.grid(row=9,column=0,padx=30,pady=15,sticky=W)


#delete
def delete_data():
    def delete():
        messagebox.showwarning('confirm','do you want to delete it?',parent=del_win)    
        query='delete from trainmain where TrainNo=%s'
        value=noentry.get()
        mycursor.execute(query,value)
        traintable.delete(*traintable.get_children())
        query = 'Select * from trainmain natural join traindetail'
        mycursor.execute(query)
        res = mycursor.fetchall()
        traintable.delete(*traintable.get_children())
        for data in res:
            datalist=list(data)
            traintable.insert('',END,values=datalist)
        del_win.destroy()

    del_win=Toplevel()
    del_win.grab_set()
    color='#FEFFAC'
    del_win.configure(bg=color)
    del_win.resizable(False,False)
    nolb=Label(del_win,text='Train No',font=('Times New Roman',15,'bold'),bg=color)
    nolb.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    noentry=Entry(del_win,font=('Consolas',15,'bold'),width=25)
    noentry.grid(row=0,column=1,padx=10,pady=20)

    delbt=Button(del_win,text='Delete',font=('Times new roman',12,'bold'),width=15,fg='black',bg='#45FFCA',command=delete)
    delbt.grid(row=11,column=0,padx=30,pady=15,sticky=W)

#search
def search():
    def ser():
        query='select * from trainmain natural join traindetail where TrainNo=%s'
        value=(noentry.get())
        mycursor.execute(query,value)
        traintable.delete(*traintable.get_children())
        fetched_data=mycursor.fetchall()
        for i in fetched_data:
            traintable.insert('',END,values=i)
    
    search_win=Toplevel()
    search_win.grab_set()
    color='#FEFFAC'
    search_win.configure(bg=color)
    search_win.resizable(False,False)

    nolb=Label(search_win,text='Train No',font=('Times New Roman',15,'bold'),bg=color)
    nolb.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    noentry=Entry(search_win,font=('Consolas',15,'bold'),width=25)
    noentry.grid(row=0,column=1,padx=10,pady=20)    
    
    searchbt=Button(search_win,text='SEARCH',font=('Times new roman',12,'bold'),width=15,fg='black',bg='#45FFCA',command=ser)
    searchbt.grid(row=6,column=0,padx=30,pady=15,sticky=W)

    
#display    
def dis():
    query='select * from trainmain natural join traindetail order by TrainNo'
    mycursor.execute(query)
    data=mycursor.fetchall()
    traintable.delete (*traintable.get_children())
    for i in data:
        datalist=list(i)
        traintable.insert('',END,values=datalist)

#add
def add():
    def insertdt():
        if noentry.get()=='' or nameentry.get()=='' or orientry.get()=='' or desentry.get()=='' or depentry.get()=='' or arventry.get()=='' or tripidentry.get()=='' or fareentry.get()=='' or irconentry.get()=='':
            messagebox.showerror('ERROR','All fields are required',parent=add_win )
        else:
            query='insert into trainmain values(%s,%s,%s,%s,%s,%s)'
            values=(noentry.get(),nameentry.get(),orientry.get(),desentry.get(),depentry.get(),arventry.get())
            mycursor.execute(query,values)
            con.commit()
            query1='insert into traindetail values(%s,%s,%s,%s)'
            values1=(tripidentry.get(),noentry.get(),fareentry.get(),irconentry.get())
            mycursor.execute(query1,values1)
            con.commit()

            result=messagebox.askyesno('Confirm','Data added sucessfully.Do you want to clear the form?',parent=add_win)
            if result:
                noentry.delete(0,END)
                nameentry.delete(0,END)
                orientry.delete(0,END)
                desentry.delete(0,END)
                depentry.delete(0,END)
                arventry.delete(0,END)
                tripidentry.delete(0,END)
                fareentry.delete(0,END)
                irconentry.delete(0,END)
            else:
                pass    

    add_win=Toplevel()
    add_win.grab_set()
    color='#FEFFAC'
    add_win.configure(bg=color)
    add_win.resizable(False,False)
    nolb=Label(add_win,text='Train No.',font=('Times New Roman',15,'bold'),bg=color)
    nolb.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    noentry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    noentry.grid(row=0,column=1,padx=10,pady=20)

    namelb=Label(add_win,text='Train Name',font=('Times New Roman',15,'bold'),bg=color)
    namelb.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameentry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    nameentry.grid(row=1,column=1,padx=10,pady=20)

    orilb=Label(add_win,text='From Station',font=('Times New Roman',15,'bold'),bg=color)
    orilb.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    orientry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    orientry.grid(row=2,column=1,padx=10,pady=20)

    deslb=Label(add_win,text='To Station',font=('Times New Roman',15,'bold'),bg=color)
    deslb.grid(row=3,column=0,sticky=W,padx=30,pady=15)
    desentry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    desentry.grid(row=3,column=1,padx=10,pady=20)

    
    deplb=Label(add_win,text='Departure Date',font=('Times New Roman',15,'bold'),bg=color)
    deplb.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    depentry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    depentry.grid(row=4,column=1,padx=10,pady=20)

    
    arvlb=Label(add_win,text='Arrival Date',font=('Times New Roman',15,'bold'),bg=color)
    arvlb.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    arventry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    arventry.grid(row=5,column=1,padx=10,pady=20)

    tripidlb=Label(add_win,text='Trip Id',font=('Times New Roman',15,'bold'),bg=color)
    tripidlb.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    tripidentry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    tripidentry.grid(row=6,column=1,padx=10,pady=20)

    farelb=Label(add_win,text='Train Fare',font=('Times New Roman',15,'bold'),bg=color)
    farelb.grid(row=8,column=0,padx=30,pady=15,sticky=W)
    fareentry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    fareentry.grid(row=8,column=1,padx=10,pady=20)

    irconlb=Label(add_win,text='Contact(IR)',font=('Times New Roman',15,'bold'),bg=color)
    irconlb.grid(row=9,column=0,padx=30,pady=15,sticky=W)
    irconentry=Entry(add_win,font=('Consolas',15,'bold'),width=25)
    irconentry.grid(row=9,column=1,padx=10,pady=20)

    submitbt=Button(add_win,text='ADD DATA',font=('Times new roman',12,'bold'),width=15,fg='black',bg='#45FFCA',command=insertdt)
    submitbt.grid(row=11,column=0,padx=30,pady=15,sticky=W)

    
def condb():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostentry.get(),user=userentry.get(),passwd=passentry.get())
            mycursor=con.cursor()
            
        except:
            messagebox.showerror('Error','Inavlid details',parent=conwin)
        try:
            query='create database traindb'
            mycursor.execute(query)
            query='use traindb'
            mycursor.execute(query)
        except:
            query='use traindb'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database connection successfull',parent=conwin)
        conwin.destroy()
        addbt.config(state=NORMAL)
        disbt.config(state=NORMAL)
        searchbt.config(state=NORMAL)
        modbt.config(state=NORMAL)
        delbt.config(state=NORMAL)



    #inorder to create a new GUI window on top of our exsisting GUI we need toplevel class.
    conwin=Toplevel()
    conwin.grab_set()
    color='#45FFCA'
    conwin.configure(bg=color)
    conwin.geometry('450x250+700+200')
    conwin.title('Connect your database')
    conwin.resizable(False,False)

    #creating labels for the pop-up window of the connection to database
    hostlb=Label(conwin,text='Host Name',font=('Times new roman',25,'bold'),bg=color)
    hostlb.grid(row=0,column=0)

    hostentry=Entry(conwin,font=('Consolas',18,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=10,pady=20)
    
    userlb=Label(conwin,text='Username',font=('Times new roman',25,'bold'),bg=color)
    userlb.grid(row=1,column=0)

    userentry=Entry(conwin,font=('Consolas',18,'bold'),bd=2)
    userentry.grid(row=1,column=1,padx=10,pady=10)

    passlb=Label(conwin,text='Password',font=('Times new roman',25,'bold'),bg=color)
    passlb.grid(row=2,column=0)

    passentry=Entry(conwin,font=('Consolas',18,'bold'),bd=2,show='*')
    passentry.grid(row=2,column=1,padx=10,pady=20)

    conbt=Button(conwin,text='Connect',font=('Times new roman',12,'bold'),width=15,fg='black',bg='#FEFFAC',command=connect)
    conbt.grid(row=3,column=0)
    


#GUI Part
root1=Tk()
color='#FEFFAC'
root1.configure(bg=color)
root1.geometry('1280x700+0+0')
root1.resizable(False,False)
root1.title('Train Query System')
tlb=Label(root1,text='Train Query System',font=('Times new roman',30,'bold'),bg=color) #title
tlb.place(x=500,y=2)

connectbt=Button(root1,text='Connect to database',font=('times new roman',12,'bold'),width=18,fg='black',bg='#45FFCA',command=condb)
connectbt.place(x=1050,y=10)

lframe=Frame(root1,bg='#FEFFAC')
lframe.place(x=50,y=20,width=300,height=600)

logoimg=PhotoImage(file='trian.png')
logoimglb=Label(lframe,image=logoimg)
logoimglb.grid(row=0,column=0)

addbt=Button(lframe,text='Add Train',font=('times new roman',14,'bold'),fg='black',bg='#45FFCA',width=25,state=DISABLED,command=add)
addbt.grid(row=1,column=0,pady=18)

disbt=Button(lframe,text='Display Trains',font=('times new roman',14,'bold'),fg='black',bg='#45FFCA',width=25,state=DISABLED,command=dis)
disbt.grid(row=2,column=0,pady=18)

searchbt=Button(lframe,text='Search Train',font=('times new roman',14,'bold'),fg='black',bg='#45FFCA',width=25,state=DISABLED,command=search)
searchbt.grid(row=3,column=0,pady=18)

modbt=Button(lframe,text='Update details',font=('times new roman',14,'bold'),fg='black',bg='#45FFCA',width=25,state=DISABLED,command=update)
modbt.grid(row=4,column=0,pady=18)

delbt=Button(lframe,text='Delete Train',font=('times new roman',14,'bold'),fg='black',bg='#45FFCA',width=25,state=DISABLED,command=delete_data)
delbt.grid(row=5,column=0,pady=18)

exit=Button(lframe,text='Exit',font=('times new roman',14,'bold'),fg='black',bg='#45FFCA',width=25,command=exit)
exit.grid(row=6,column=0,pady=18)


rframe=Frame(root1,bg='#45FFCA')
rframe.place(x=350,y=60,width=870,height=600)

scrollx=Scrollbar(rframe,orient=HORIZONTAL)
scrolly=Scrollbar(rframe,orient=VERTICAL)


traintable=ttk.Treeview(rframe,columns=('Train.No','Train Name','origin','Destination','Departure Date','Arrival Date'
                             ,'TripId','Train Fare','Contact(Indian Railways)'),
                             xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.config(command=traintable.xview)
scrolly.config(command=traintable.yview)

scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)

traintable.pack(fill=BOTH,expand=1)

traintable.heading('Train.No',text='Train No.')
traintable.heading('Train Name',text='Train Name')
traintable.heading('origin',text='Origin')
traintable.heading('Destination',text='Destination')
traintable.heading('Departure Date',text='Departure')
traintable.heading('Arrival Date',text='Arrival')
traintable.heading('TripId',text='TripId')
traintable.heading('Train Fare',text='Train Fare')
traintable.heading('Contact(Indian Railways)',text='Contact(Indian Railways)')
traintable.config(show='headings')

traintable.column('Train.No',width=80,anchor=CENTER)
traintable.column('Train Name',width=150,anchor=CENTER)
traintable.column('origin',width=160,anchor=CENTER)
traintable.column('Destination',width=180,anchor=CENTER)
traintable.column('Departure Date',width=100,anchor=CENTER)
traintable.column('Arrival Date',width=100,anchor=CENTER)
traintable.column('TripId',width=80,anchor=CENTER)
traintable.column('Train Fare',width=80,anchor=CENTER)
traintable.column('Contact(Indian Railways)',width=150,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('Times New Roman',10,'bold'),foreground='black')
style.configure('Treeview.Heading',font=('Times New Roman',12,'bold'))

root1.mainloop()