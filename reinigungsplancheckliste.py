from tkinter import *

import reinigungsplanspeichern as sp

def checkliste(tkFenster0):
    # Listen erstellen
    var = {}
    ausgabe= {}

    # Lesen der Checklisten-Einträge
    file = open('Reinigungsplan-Checkliste.txt', 'r')
    f0 = file.readlines()
    f0_len = (len(f0))
    file.close()

    # Header
    T1 = Label(master=tkFenster0, text="Cafe - Reinigungsplan")
    T1.config(bg='#342216', fg="white", font=("bold", 26), borderwidth=0)
    T1.place(x=0, y=0, width=550, height=50)

    # Eintrag des Mitarbeiters
    T2 = Label(master=tkFenster0, text="Mitarbeiter")
    T2.config(bg='#403027', fg="white", font=("bold", 14), borderwidth=0, anchor='w')
    T2.place(x=0, y=60, width=550, height=50)

    e1 = Entry(master=tkFenster0)
    e1.place(x=0, y=100, width=200, height=15)

    # ------ Checkliste ------
    T3 = Label(master=tkFenster0, text="Checkliste")
    T3.config(bg='#403027', fg="white", font=("bold", 14), borderwidth=0, anchor='w')
    T3.place(x=0, y=120)

    # Button zum Speichern
    button1 = Button(master=tkFenster0, text="Speichern", font=("bold", 14), command=lambda: sp.save(tkFenster0, e1, var, ausgabe, f0_len))
    button1.place(x=175, y=550, width=200, height=50)

    # Eintrag 1 der Checkliste
    for i in range(0, f0_len, 1):
        ausgabe[i] = str(f0[i])

        var[i] = IntVar()
        Check1 = Checkbutton(master=tkFenster0, variable=var[i])
        Check1.config(bg='#403027')
        Check1.place(x=0, y=150+(i*20))

        TCheck1 = Label(master=tkFenster0, text=f0[i-1])
        TCheck1.config(bg='#403027', fg="white", font=("bold", 12), borderwidth=0)
        TCheck1.place(x=30, y=152+(i*20))