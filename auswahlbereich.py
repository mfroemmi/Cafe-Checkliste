from tkinter import *
import reinigungsplancheckliste as cl

def Auswahlbereich(tkFenster0):
    # Header
    global T0
    T0 = Label(master=tkFenster0, text="Cafe - Checklisten")
    T0.config(bg='#342216', fg="white", font=("bold", 26), borderwidth=0)
    T0.place(x=0, y=0, width=550, height=50)

    # Auswahlbereich-Text
    global T2
    T2 = Label(master=tkFenster0, text="Auswahlbereich")
    T2.config(bg='#403027', fg="white", font=("bold", 14), borderwidth=0)
    T2.place(x=0, y=60, width=550, height=50)

    # Button zum Reinigungsplan
    global button0
    button0 = Button(master=tkFenster0, text="Reinigungsplan", font=("bold", 14), command=lambda: [cl.checkliste(tkFenster0), rplan_button()])
    button0.place(x=175, y=175, width=200, height=50)

def rplan_button():
    print("Hallo")
    T2.destroy()
    button0.destroy()