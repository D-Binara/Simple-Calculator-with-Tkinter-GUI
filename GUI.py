
from tkinter import *

def Click():
    print("Testing")

l=Tk() 

l.title('Test 1')
l.geometry("300x400+700+50")
l.config(background="#732941")

Label1=Label(l,text="Hello, Test 1")
Label1.pack()

but=Button(l, text="Click",command=Click)
but.pack(side=TOP , fill=X, pady=10)

but2=Button(l, text="Click2",command=Click)
but2.pack( fill=BOTH , expand=1)

fr=Frame(l)
fr.pack(fill=BOTH)

butf=Button(fr,text="1")
butf.pack(side=LEFT)

butf2=Button(fr,text="2")
butf2.pack(side=LEFT)

butf3=Button(fr,text="3")
butf3.pack(side=LEFT)

butf4=Button(fr,text="4")
butf4.pack(padx=10,pady=10,side=LEFT)

butf5=Button(fr,text="5")
butf5.pack(pady=10,side=LEFT)

butf6=Button(fr,text="6")
butf6.pack(pady=10,side=LEFT)

l.mainloop()

print("HEllo")