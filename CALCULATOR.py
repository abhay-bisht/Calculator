#creating a calculator using tkinter:-
from tkinter import *
root=Tk()
root.geometry("300x600")
root.title("CALCULATOR by ABHAY BISHT")
root.wm_iconbitmap("Marcus-Roberto-Google-Play-Google-Drive.ico")
root.configure(background="thistle")

scvalue =StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue ,font = "lucide 20 bold",bg="lightcyan")
screen.pack(fill=X,padx=6,pady=6)
def click(event):
    global scvalue
    text=event.widget.cget("text")    #.cget()    ek button se text kaise nikala jae 
    print(text)
    if(text=="="):
        if (scvalue.get().isdigit()):
            value = int(scvalue.get())
        else:
            value = eval(screen.get()) 
        scvalue.set(value)
        screen.update()        
    elif(text=="C"):
        scvalue.set("") 
        screen.update()        
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
f = Frame(root,bg="orchid",borderwidth=4,relief=SUNKEN)
b = Button(f,text="9",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15 , pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="8",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15 , pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="7",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15 , pady=5)
b.bind("<Button-1>",click)
f.pack()
f = Frame(root,bg="lightpink",borderwidth=4,relief=SUNKEN)
b = Button(f,text="6",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="5",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15 , pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="4",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15 , pady=5)
b.bind("<Button-1>",click)
f.pack()
f = Frame(root,bg="orchid",borderwidth=4,relief=SUNKEN)
b = Button(f,text="3",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15 , pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="2",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15 , pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="1",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15 , pady=5)
b.bind("<Button-1>",click)
f.pack()
f = Frame(root,bg="lightpink",borderwidth=4,relief=SUNKEN)
b = Button(f,text="%",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="-",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text=".",font="lucida 24 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f.pack()
f = Frame(root,bg="orchid",borderwidth=4,relief=SUNKEN)
b = Button(f,text="+",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=14 ,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="0",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="C",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=14,pady=5)
b.bind("<Button-1>",click) 
f.pack()
f = Frame(root,bg="lightpink",borderwidth=4,relief=SUNKEN)
b = Button(f,text="=",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="/",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="*",font="lucida 20 bold",bg="lightsteelblue")
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()