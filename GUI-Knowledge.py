from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title('ตาราง OR')
GUI.geometry('650x400')




L1 = Label(GUI,text='Mon',font=('MS Sans Sarif',18),fg='tomato')
L1.place(x=100,y=20)
L2 = Label(GUI,text='Tue',font=('MS Sans Sarif',18),fg='tomato')
L2.place(x=200,y=20)
L3 = Label(GUI,text='Wed',font=('MS Sans Sarif',18),fg='tomato')
L3.place(x=300,y=20)
L4 = Label(GUI,text='Thu',font=('MS Sans Sarif',18),fg='tomato')
L4.place(x=400,y=20)
L5 = Label(GUI,text='Fri',font=('MS Sans Sarif',18),fg='tomato')
L5.place(x=500,y=20)



def Button1():
    text = 'Total repair TOF'
    messagebox.showinfo('409',text)
    
FB1 = Frame(GUI)
FB1.place(x=80,y=100)
B1 = ttk.Button(FB1,text='409',command=Button1)
B1.pack(ipadx=4,ipady=10)



def Button2():
    text = 'VSD closure'
    messagebox.showinfo('410',text)

FB2 = Frame(GUI)
FB2.place(x=80,y=200)
B2 = ttk.Button(FB2,text ='410',command=Button2)
B2.pack(ipadx=4,ipady=10)


def Button3():
    text = 'RUL lobectomy, CABGx4'
    messagebox.showinfo('411',text)

FB3 = Frame(GUI)
FB3.place(x=80,y=300)
B3 = ttk.Button(FB3,text ='411',command=Button3)
B3.pack(ipadx=4,ipady=10)




GUI.mainloop()
