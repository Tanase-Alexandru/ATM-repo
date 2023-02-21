import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial
sumatot=1000
def quitt():
    quit()
def withtop():
    suma=int(sumae.get())
    global sumatot
    sumatot-=suma
    sumae.delete(0, END)
    back()

def deposittop():
    suma=int(deposite.get())
    global sumatot
    sumatot+=suma
    deposite.delete(0, END)
    back()

def back():
    raise_frame(f2).pack()

def withdraw():
    raise_frame(f5).pack()

def deposit():
    raise_frame(f4).pack()

def sold():
    global sumatot
    Label(f6,text='Actual balance is :' +str(sumatot) +'ron',background="#000099",font=('Arial',20)).place(x=width/2-150,y=height/2-100)
    raise_frame(f6).pack()



def checkpin():
    pinn=entry_pin.get()
    if (len(pinn) ==4):
        raise_frame(f2).pack()
    else:
        messagebox.showwarning(title='WARNING!',message='You must enter 4 digit pin!')

def raise_frame(frame):
    frame.tkraise()
def fastwithr(amount):
    suma = int(amount)
    global sumatot
    sumatot -= suma
    back()

def fastdepr(amount):
    suma = int(amount)
    global sumatot
    sumatot += suma
    back()
def fastwith():
    raise_frame(f3).pack()
def fastdep():
    raise_frame(f7).pack()


root = Tk()
root.title("Tanase Alexandru ATM")
root.state('zoomed')
img=PhotoImage(file='C:\\Users\\Bia Dilia\\PycharmProjects\\ATM\\atm-machine.png')
root.iconphoto(False,img)

width= root.winfo_screenwidth()
height= root.winfo_screenheight()

f1 = Frame(root,bd=5,relief=SUNKEN,width=width, height=height, background="#000099")
f2 = Frame(root,bd=5,relief=SUNKEN,width=width, height=height, background="#000099")
f3 = Frame(root,bd=5,relief=SUNKEN,width=width, height=height, background="#000099")
f4 = Frame(root,bd=5,relief=SUNKEN,width=width, height=height, background="#000099")
f5 = Frame(root,bd=5,relief=SUNKEN,width=width, height=height, background="#000099")
f6 = Frame(root,bd=5,relief=SUNKEN,width=width, height=height, background="#000099")
f7 = Frame(root,bd=5,relief=SUNKEN,width=width, height=500, background="#000099")

for frame in (f1, f2, f3, f4, f5, f6 ,f7):
    frame.grid(row=0, column=0, sticky='news')

Label(f1, text='ATM PROJECT BY TANASE ALEXANDRU-GABRIEL',background="#000099").place(x=width/2,y=0,anchor=CENTER)
Label(f1, text='Welcome to ATM',background="#000099",font=('Ink free',25)).place(x=width/2,y=40,anchor=CENTER)
Label(f2, text='ATM PROJECT BY TANASE ALEXANDRU-GABRIEL',background="#000099").place(x=width/2,y=0,anchor=CENTER)
Label(f3, text='ATM PROJECT BY TANASE ALEXANDRU-GABRIEL',background="#000099").place(x=width/2,y=0,anchor=CENTER)
Label(f5, text='ATM PROJECT BY TANASE ALEXANDRU-GABRIEL',background="#000099").place(x=width/2,y=0,anchor=CENTER)
Label(f6, text='ATM PROJECT BY TANASE ALEXANDRU-GABRIEL',background="#000099").place(x=width/2,y=0,anchor=CENTER)
Label(f7, text='ATM PROJECT BY TANASE ALEXANDRU-GABRIEL',background="#000099").place(x=width/2,y=0,anchor=CENTER)

label1=Label(f1, text='Enter your pin:',background="#000099")
entry_pin= Entry(f1,font='Arial',show='*')
check=Button(f1,text='Check pin',command=checkpin,activebackground='blue',relief='raised',borderwidth=3)
label1.place(x=width/2,y=height/2-40,anchor=CENTER)
check.place(x=width/2,y=height/2+20,anchor=CENTER)
entry_pin.place(x=width/2,y=height/2-10,anchor=CENTER)

Button(f2, text='Withdraw', command=withdraw,relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=100)
Button(f2, text='Deposit', command=deposit,relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=300)
Button(f2, text='Check sold', command=sold,relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=500)
Button(f2, text='Quit', command=quitt,relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=700)
Button(f2, text='Fast withdraw', command=fastwith,relief='raised',borderwidth=3,width=40,height=3).place(x=width-301,y=250)
Button(f2, text='Fast deposit', command=fastdep,relief='raised',borderwidth=3,width=40,height=3).place(x=width-301,y=500)

#f5=withdraw page
Button(f5,text='Withdraw amount',command=withtop,relief='raised',borderwidth=3,width=15,height=3).place(x=width/2-35,y=height/2+30)
sumae= Entry(f5,font='Arial')
sumae.place(x=width/2-90,y=height/2)
Label(f5,text='Type the amount you want to withdraw: ',background="#000099").place(x=width/2-90,y=height/2-30)
#butoane intoarcere
Button(f6, text='BACK TO MAIN MENIU', command=back,relief='raised',borderwidth=3).place(x=width/2-45,y=height/2+320)
Button(f5, text='BACK TO MAIN MENIU', command=back,relief='raised',borderwidth=3).place(x=width/2-45,y=height/2+320)
Button(f4, text='BACK TO MAIN MENIU', command=back,relief='raised',borderwidth=3).place(x=width/2-45,y=height/2+320)
Button(f3, text='BACK TO MAIN MENIU', command=back,relief='raised',borderwidth=3).place(x=width/2-45,y=height/2+320)
Button(f7, text='BACK TO MAIN MENIU', command=back,relief='raised',borderwidth=3).place(x=width/2-45,y=height/2+320)
#f4=deposit page
Button(f4,text='Deposit amount',command=deposittop,relief='raised',borderwidth=3,width=15,height=3).place(x=width/2-35,y=height/2+30)
deposite= Entry(f4,font='Arial')
deposite.place(x=width/2-90,y=height/2)
Label(f4,text='Type the amount you want to deposit: ',background="#000099").place(x=width/2-90,y=height/2-30)
#f3=fastwith page
Button(f3, text='10RON', command=lambda :fastwithr(10),relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=100)
Button(f3, text='20RON', command=lambda :fastwithr(20),relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=300)
Button(f3, text='50RON', command=lambda :fastwithr(50),relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=500)
Button(f3, text='100RON', command=lambda :fastwithr(100),relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=700)
Button(f3, text='200RON', command=lambda :fastwithr(200),relief='raised',borderwidth=3,width=40,height=3).place(x=width-301,y=250)
Button(f3, text='500RON', command=lambda :fastwithr(500),relief='raised',borderwidth=3,width=40,height=3).place(x=width-301,y=500)
#f7=fastdep page
Button(f7, text='10RON', command=lambda :fastdepr(10),relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=100)
Button(f7, text='20RON', command=lambda :fastdepr(20),relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=300)
Button(f7, text='50RON', command=lambda :fastdepr(50),relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=500)
Button(f7, text='100RON', command=lambda :fastdepr(100),relief='raised',borderwidth=3,width=40,height=3).place(x=0,y=700)
Button(f7, text='200RON', command=lambda :fastdepr(200),relief='raised',borderwidth=3,width=40,height=3).place(x=width-301,y=250)
Button(f7, text='500RON', command=lambda :fastdepr(500),relief='raised',borderwidth=3,width=40,height=3).place(x=width-301,y=500)
raise_frame(f1)
root.mainloop()