#database- busdb
from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk
import pymysql
#functionality

#back to page 2
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
        root.destroy()
        backwin()
    else:
        pass
#update
def update():
            
    def upd():
        id_inp = identry.get()
        desinp = desentry.get()
        depinp = depentry.get()
        arvinp = arventry.get()
        tripinp = tripidentry.get()
        fareinp=fareentry.get()
        if id_inp=='' or desinp=='' or depinp=='' or arvinp=='' or tripinp=='' or fareinp=='':
            messagebox.showerror('ERROR','All fields are required',parent=upd_win )
        elif id_inp.isalpha():
            messagebox.showerror('ERROR','Bus Id should be INTEGER',parent=upd_win )
        elif desinp.isdigit():
            messagebox.showerror('ERROR','Destination should be STRING',parent=upd_win)
        elif tripinp.isalpha():
            messagebox.showerror('ERROR','TripID should be INTEGER',parent=upd_win )
        elif fareinp.isalpha():
            messagebox.showerror('ERROR','Fare must be a NUMBER',parent=upd_win )
        else:   
            query = 'update busmain set Destination=%s,DeptDate=%s,ArrivalDate=%s where BusId=%s'
            values = (desinp,depinp,arvinp,id_inp)
            mycursor.execute(query,values)
            query = 'update busdetail set TripID=%s,BusFare=%s where BusId=%s'
            values = (tripinp,fareinp,id_inp)
            mycursor.execute(query,values)
            con.commit()
            messagebox.showinfo('Notification','UPDATED SUCCESSFULLY')
            bustable.delete(*bustable.get_children())
            query = 'Select * from busmain natural join busdetail'
            mycursor.execute(query)
            res = mycursor.fetchall()
            bustable.delete(*bustable.get_children())
            for data in res:
                datalist=list(data)
                bustable.insert('',END,values=datalist)
            upd_win.destroy()
                                                
    upd_win=Toplevel()
    upd_win.grab_set()
    color='#FFBA86'
    upd_win.configure(bg=color)
    upd_win.resizable(False,False)
    idlb=Label(upd_win,text='Bus ID',font=('Times New Roman',15,'bold'),bg=color)
    idlb.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    identry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    identry.grid(row=0,column=1,padx=10,pady=20)

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

    farelb=Label(upd_win,text='Bus Fare',font=('Times New Roman',15,'bold'),bg=color)
    farelb.grid(row=8,column=0,padx=30,pady=15,sticky=W)
    fareentry=Entry(upd_win,font=('Consolas',15,'bold'),width=25)
    fareentry.grid(row=8,column=1,padx=10,pady=20)


    updbt=Button(upd_win,text='UPDATE DATA',font=('Times new roman',12,'bold'),width=15,fg='black',bg='#C23373',command=upd)
    updbt.grid(row=11,column=0,padx=30,pady=15,sticky=W)


#delete
def delete_data():
    def delete():
        messagebox.showwarning('confirm','do you want to delete it?',parent=del_win)
        query='delete from busmain where BusId = %s'
        value=int(identry.get())
        mycursor.execute(query,value)
        res = mycursor.fetchall()
        bustable.delete(*bustable.get_children())
        for data in res:
            datalist=list(data)
            bustable.insert('',END,values=datalist)
        del_win.destroy()


    del_win=Toplevel()
    del_win.grab_set()
    color='#FFBA86'
    del_win.configure(bg=color)
    del_win.resizable(False,False)
    idlb=Label(del_win,text='Bus ID',font=('Times New Roman',15,'bold'),bg=color)
    idlb.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    identry=Entry(del_win,font=('Consolas',15,'bold'),width=25)
    identry.grid(row=0,column=1,padx=10,pady=20)

    delbt=Button(del_win,text='Delete',font=('Times new roman',12,'bold'),width=15,fg='black',bg='#C23373',command=delete)
    delbt.grid(row=11,column=0,padx=30,pady=15,sticky=W)

#search
def search():
    def ser():
        query='select * from busmain natural join busdetail where BusId=%s or Destination=%s or DeptDate=%s or ArrivalDate=%s or DriverName=%s'
        value=(identry.get(),desentry.get(),depentry.get(),arventry.get(),driverentry.get())
        mycursor.execute(query,value)
        bustable.delete(*bustable.get_children())
        fetched_data=mycursor.fetchall()
        for i in fetched_data:
            bustable.insert('',END,values=i)
    
    search_win=Toplevel()
    search_win.grab_set()
    color='#FFBA86'
    search_win.configure(bg=color)
    search_win.resizable(False,False)
    idlb=Label(search_win,text='Bus ID',font=('Times New Roman',15,'bold'),bg=color)
    idlb.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    identry=Entry(search_win,font=('Consolas',15,'bold'),width=25)
    identry.grid(row=0,column=1,padx=10,pady=20)

    deslb=Label(search_win,text='Destination',font=('Times New Roman',15,'bold'),bg=color)
    deslb.grid(row=3,column=0,sticky=W,padx=30,pady=15)
    desentry=Entry(search_win,font=('Consolas',15,'bold'),width=25)
    desentry.grid(row=3,column=1,padx=1,pady=2)

    
    deplb=Label(search_win,text='Departure',font=('Times New Roman',15,'bold'),bg=color)
    deplb.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    depentry=Entry(search_win,font=('Consolas',15,'bold'),width=25)
    depentry.grid(row=4,column=1,padx=1,pady=2)

    
    arvlb=Label(search_win,text='Arrival',font=('Times New Roman',15,'bold'),bg=color)
    arvlb.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    arventry=Entry(search_win,font=('Consolas',15,'bold'),width=25)
    arventry.grid(row=5,column=1,padx=10,pady=20)


    driverlb=Label(search_win,text='Driver Name',font=('Times New Roman',15,'bold'),bg=color)
    driverlb.grid(row=7,column=0,padx=30,pady=15,sticky=W)
    driverentry=Entry(search_win,font=('Consolas',15,'bold'),width=25)
    driverentry.grid(row=7,column=1,padx=10,pady=20)

    
    

    searchbt=Button(search_win,text='SEARCH',font=('Times new roman',12,'bold'),width=15,fg='black',bg='#C23373',command=ser)
    searchbt.grid(row=11,column=0,padx=30,pady=15,sticky=W)

    
#display    
def dis():
    query='select * from busmain natural join busdetail order by BusId'
    mycursor.execute(query)
    data=mycursor.fetchall()
    bustable.delete (*bustable.get_children())
    for i in data:
        datalist=list(i)
        bustable.insert('',END,values=datalist)

#add
def add():
    def insertdt():
        if identry.get()=='' or nameentry.get()=='' or tanentry.get()=='' or desentry.get()=='' or depentry.get()=='' or arventry.get()=='' or tripidentry.get()=='' or driverentry.get()=='' or fareentry.get()=='' or driconentry.get()=='' or agconentry.get()=='':
            messagebox.showerror('ERROR','All fields are required',parent=add_win )
        elif identry.get().isalpha():
            messagebox.showerror('ERROR','BUS ID MUST BE INTEGER',parent=add_win )
        elif nameentry.get().isdigit():
            messagebox.showerror('ERROR','NAME MUST BE STRING',parent=add_win)
        elif tanentry.get().isdigit():
            messagebox.showerror('ERROR','travel agency name must be string',parent=add_win )
        elif desentry.get().isdigit():
            messagebox.showerror('ERROR','DESTINATION MUST BE STRING',parent=add_win )
        elif depentry.get().isdigit():
            messagebox.showerror('ERROR','DEPARTURE DATE MUST BE STRING',parent=add_win )
        elif arventry.get().isdigit():
            messagebox.showerror('ERROR','ARRIVAL DATE MUST BE STRING',parent=add_win )
        elif tripidentry.get().isalpha():
            messagebox.showerror('ERROR','TRIP ID MUST BE INTEGER',parent=add_win )
        elif driverentry.get().isdigit():
            messagebox.showerror('ERROR','DRIVER NAME MUST BE STRING',parent=add_win )
        elif fareentry.get().isalpha():
            messagebox.showerror('ERROR','FARE MUST BE INTEGER',parent=add_win )
        elif driconentry.get().isalpha():
            messagebox.showerror('ERROR','DRIVER CONTACT MUST BE INTEGER',parent=add_win )
        elif agconentry.get().isalpha():
            messagebox.showerror('ERROR','AGENCY CONTACT MUST BE INTEGER',parent=add_win ) 
        else:
            query='insert into busmain values(%s,%s,%s,%s,%s,%s)'
            values=(identry.get(),nameentry.get(),tanentry.get(),desentry.get(),depentry.get(),arventry.get())
            mycursor.execute(query,values)
            query1='insert into busdetail values(%s,%s,%s,%s,%s,%s)'
            con.commit()
            values1=(tripidentry.get(),identry.get(),driverentry.get(),fareentry.get(),driconentry.get(),agconentry.get())
            mycursor.execute(query1,values1)
            con.commit()

            result=messagebox.askyesno('Confirm','Data added sucessfully.Do you want to clear the form?',parent=add_win)
            if result:
                identry.delete(0,END)
                nameentry.delete(0,END)
                tanentry.delete(0,END)
                desentry.delete(0,END)
                depentry.delete(0,END)
                arventry.delete(0,END)
                tripidentry.delete(0,END)
                driverentry.delete(0,END)
                fareentry.delete(0,END)
                driconentry.delete(0,END)
                agconentry.delete(0,END)
            else:
                pass
            
    add_win=Toplevel()
    add_win.grab_set()
    color='#FFBA86'
    add_win.configure(bg=color)
    add_win.resizable(False,False)
    add_win.geometry('500x600+0+0')

    idlb=Label(add_win,text='Bus ID',font=('Times New Roman',12,'bold'),bg=color)
    idlb.grid(row=0,column=0,padx=30,pady=10,sticky=W)
    identry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    identry.grid(row=0,column=1,padx=10,pady=10)

    namelb=Label(add_win,text='Bus Name',font=('Times New Roman',12,'bold'),bg=color)
    namelb.grid(row=1,column=0,padx=30,pady=10,sticky=W)
    nameentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    nameentry.grid(row=1,column=1,padx=10,pady=10)

    tanlb=Label(add_win,text='Travel Agency Name',font=('Times New Roman',12,'bold'),bg=color)
    tanlb.grid(row=2,column=0,padx=30,pady=10,sticky=W)
    tanentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    tanentry.grid(row=2,column=1,padx=10,pady=10)

    deslb=Label(add_win,text='Destination',font=('Times New Roman',12,'bold'),bg=color)
    deslb.grid(row=3,column=0,sticky=W,padx=30,pady=10)
    desentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    desentry.grid(row=3,column=1,padx=10,pady=10)

    
    deplb=Label(add_win,text='Departure Date',font=('Times New Roman',12,'bold'),bg=color)
    deplb.grid(row=4,column=0,padx=30,pady=10,sticky=W)
    depentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    depentry.grid(row=4,column=1,padx=10,pady=10)

    
    arvlb=Label(add_win,text='Arrival Date',font=('Times New Roman',12,'bold'),bg=color)
    arvlb.grid(row=5,column=0,padx=30,pady=10,sticky=W)
    arventry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    arventry.grid(row=5,column=1,padx=10,pady=10)

    tripidlb=Label(add_win,text='Trip Id',font=('Times New Roman',12,'bold'),bg=color)
    tripidlb.grid(row=6,column=0,padx=30,pady=10,sticky=W)
    tripidentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    tripidentry.grid(row=6,column=1,padx=10,pady=10)

    driverlb=Label(add_win,text='Driver Name',font=('Times New Roman',12,'bold'),bg=color)
    driverlb.grid(row=7,column=0,padx=30,pady=10,sticky=W)
    driverentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    driverentry.grid(row=7,column=1,padx=10,pady=10)

    farelb=Label(add_win,text='Bus Fare',font=('Times New Roman',12,'bold'),bg=color)
    farelb.grid(row=8,column=0,padx=30,pady=10,sticky=W)
    fareentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    fareentry.grid(row=8,column=1,padx=10,pady=10)

    driconlb=Label(add_win,text='Driver Contact',font=('Times New Roman',12,'bold'),bg=color)
    driconlb.grid(row=9,column=0,padx=30,pady=10,sticky=W)
    driconentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    driconentry.grid(row=9,column=1,padx=10,pady=10)

    agconlb=Label(add_win,text='Agency Contact',font=('Times New Roman',12,'bold'),bg=color)
    agconlb.grid(row=10,column=0,padx=30,pady=10,sticky=W)
    agconentry=Entry(add_win,font=('Consolas',12,'bold'),width=20)
    agconentry.grid(row=10,column=1,padx=10,pady=10)


    submitbt=Button(add_win,text='ADD DATA',font=('Times new roman',15,'bold'),width=15,fg='black',bg='#C23373',command=insertdt)
    submitbt.grid(row=11,column=0,padx=30,pady=10,sticky=W)

    
def condb():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostentry.get(),user=userentry.get(),passwd=passentry.get())
            mycursor=con.cursor()
            
        except:
            messagebox.showerror('Error','Inavlid details',parent=conwin)
        try:
            query='create database busdb'
            mycursor.execute(query)
            query='use busdb'
            mycursor.execute(query)
            query='create table busmain(BusId int not null primary key,BusName varchar(30),TravelAgency varchar(30),Destination varchar(20),DeptDate varchar(20),ArrivalDate varchar(20))'
            mycursor.execute(query)
            query='create table busdetail(TripID int not null primary key,BusId int not null,DriverName varchar(30),BusFare int,Contact_driver varchar(20),Contact_Agency varchar(20),constraint fk foreign key(BusId) references busmain(BusId) on delete cascade on update cascade)'
            mycursor.execute(query)
        except:
            query='use busdb'
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
    color='#FFBA86'
    conwin.configure(bg=color)
    conwin.geometry('400x250+300+200')
    conwin.title('Connect your database')
    conwin.resizable(False,False)

    #creating labels for the pop-up window of the connection to database
    hostlb=Label(conwin,text='Host Name',font=('Times new roman',18,'bold'),bg=color)
    hostlb.grid(row=0,column=0)

    hostentry=Entry(conwin,font=('Consolas',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=10,pady=20)
    
    userlb=Label(conwin,text='Username',font=('Times new roman',20,'bold'),bg=color)
    userlb.grid(row=1,column=0)

    userentry=Entry(conwin,font=('Consolas',15,'bold'),bd=2)
    userentry.grid(row=1,column=1,padx=10,pady=10)

    passlb=Label(conwin,text='Password',font=('Times new roman',20,'bold'),bg=color)
    passlb.grid(row=2,column=0)

    passentry=Entry(conwin,font=('Consolas',15,'bold'),bd=2,show='*')
    passentry.grid(row=2,column=1,padx=10,pady=20)

    conbt=Button(conwin,text='Connect',font=('Times new roman',12,'bold'),width=10,fg='#C23373',bg='white',command=connect)
    conbt.grid(row=3,column=0)
    


#GUI Part
root=Tk()
root.geometry('1010x700+0+0')
color='#F6635C'
root.configure(bg=color)
root.resizable(False,False)
root.title('Bus Query System')
slb=Label(root,text='Bus Query System',font=('Times new roman',30,'bold'),bg=color) #title
slb.place(x=400,y=2)

connectbt=Button(root,text='Connect to database',font=('times new roman',12,'bold'),width=18,fg='black',bg='#FFBA86',command=condb)
connectbt.place(x=800,y=10)

lframe=Frame(root,bg=color)
lframe.place(x=50,y=20,width=300,height=600)

logoimg=PhotoImage(file='bus.png')
logoimglb=Label(lframe,image=logoimg)
logoimglb.grid(row=0,column=0)

addbt=Button(lframe,text='Add Bus',font=('times new roman',14,'bold'),width=15,fg='#C23373',bg='#FFBA86',state=DISABLED,command=add)
addbt.grid(row=1,column=0,pady=20)

disbt=Button(lframe,text='Display Buses',font=('times new roman',14,'bold'),width=15,fg='#C23373',bg='#FFBA86',state=DISABLED,command=dis)
disbt.grid(row=2,column=0,pady=20)

searchbt=Button(lframe,text='Search Bus',font=('times new roman',14,'bold'),width=15,fg='#C23373',bg='#FFBA86',state=DISABLED,command=search)
searchbt.grid(row=3,column=0,pady=20)

modbt=Button(lframe,text='Modify bus',font=('times new roman',14,'bold'),width=15,fg='#C23373',bg='#FFBA86',state=DISABLED,command=update)
modbt.grid(row=4,column=0,pady=20)

delbt=Button(lframe,text='Delete bus',font=('times new roman',14,'bold'),width=15,fg='#C23373',bg='#FFBA86',state=DISABLED,command=delete_data)
delbt.grid(row=5,column=0,pady=20)

exit=Button(lframe,text='Exit',font=('times new roman',14,'bold'),width=15,fg='#C23373',bg='#FFBA86',command=exit)
exit.grid(row=6,column=0,pady=20)


rframe=Frame(root,bg='#FF731D')
rframe.place(x=300,y=70,width=670,height=600)

scrollx=Scrollbar(rframe,orient=HORIZONTAL)
scrolly=Scrollbar(rframe,orient=VERTICAL)


bustable=ttk.Treeview(rframe,columns=('Bus Id','Bus Name','Travel Agency Name','Destination','Departure Date','Arrival Date'
                             ,'TripId','Driver Name','Bus Fare','Contact No.(Driver)','Contact No.(Agency)'),
                             xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.config(command=bustable.xview)
scrolly.config(command=bustable.yview)

scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)

bustable.pack(fill=BOTH,expand=1)

bustable.heading('Bus Id',text='Bus Id')
bustable.heading('Bus Name',text='Bus Name')
bustable.heading('Travel Agency Name',text='Travel Agency Name')
bustable.heading('Destination',text='Destination')
bustable.heading('Departure Date',text='Departure')
bustable.heading('Arrival Date',text='Arrival')
bustable.heading('TripId',text='TripId')
bustable.heading('Driver Name',text='Driver Name')
bustable.heading('Bus Fare',text='Bus Fare')
bustable.heading('Contact No.(Driver)',text='Contact No.(Driver)')
bustable.heading('Contact No.(Agency)',text='Contact No.(Agency)')
bustable.config(show='headings')

bustable.column('Bus Id',width=80,anchor=CENTER)
bustable.column('Bus Name',width=150,anchor=CENTER)
bustable.column('Travel Agency Name',width=200,anchor=CENTER)
bustable.column('Destination',width=100,anchor=CENTER)
bustable.column('Departure Date',width=100,anchor=CENTER)
bustable.column('Arrival Date',width=100,anchor=CENTER)
bustable.column('TripId',width=80,anchor=CENTER)
bustable.column('Driver Name',width=150,anchor=CENTER)
bustable.column('Bus Fare',width=80,anchor=CENTER)
bustable.column('Contact No.(Driver)',width=150,anchor=CENTER)
bustable.column('Contact No.(Agency)',width=150,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('Times New Roman',10,'bold'),foreground='black')
style.configure('Treeview.Heading',font=('Times New Roman',12,'bold'))


root.mainloop()
