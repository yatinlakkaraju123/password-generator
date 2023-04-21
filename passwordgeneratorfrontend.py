
from tkinter import *
import pyclip
from passwordgenerator import passwordgenerator
from passwordchecker import passwordchecker
root = Tk()
root.title("password generator")
r = IntVar()
# r is length of password

def copy():
    global p
    pyclip.copy(p)





def getlength():
    o = r.get()
    global opt
    opt = o
    e = inp.get()
    global length
    global p

    length = int(e)
    password = passwordgenerator(length,opt)
    p = password
    Label(root,text=password).grid(row=8,column=0)
def getstrength():
    p = inp2.get()
    global password
    password = str(p)
    strength = passwordchecker(password)
    if strength==0:
        Label(root,text="weak password").grid(row=13,column=0)
    elif strength==1:
        Label(root, text="strong  password").grid(row=13, column=0)
label1 = Label(root,text="select the following options:")
cb1 = Radiobutton(root,text="password which only consists of alphabets",variable=r,value=1)
cb2 = Radiobutton(root,text="password which consists of a combination of alphabets and letters",variable=r,value=2)
cb3 = Radiobutton(root,text="password of combination of alphabets,letters and symbols",variable=r,value=3)
#submit_btn = Button(root,text='submit',command=lambda:getoption())
btn = Button(root,text="copy to clipboard",command=copy)
label2 = Label(root,text="enter the length of the password required")
label3 = Label(root,text="enter password to check whether it is strong or weak:")
inp2 = Entry(root)
inp = Entry(root)
label1.grid(row=0,column=0)
cb1.grid(row=1,column=0)
cb2.grid(row=2,column=0)
cb3.grid(row=3,column=0)
#submit_btn.grid(row=5,column=0)
inp.grid(row=6,column=0)
Button(root,text='submit',command=getlength).grid(row=7,column=0)
btn.grid(row=9,column=0)
label3.grid(row=10,column=0)
inp2.grid(row=11,column=0)
Button(root,text='submit',command=getstrength).grid(row=12,column=0)
root.mainloop()