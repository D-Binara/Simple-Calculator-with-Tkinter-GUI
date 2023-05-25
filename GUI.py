
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

but2=Button(l, text="Click",command=Click)
but2.pack( fill=BOTH , expand=1)

l.mainloop()

print("HEllo")