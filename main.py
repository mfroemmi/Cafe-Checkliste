from tkinter import *

import auswahlbereich as ab

tkFenster0 = Tk()
tkFenster0.title('Checkliste')
tkFenster0.geometry('550x700')
tkFenster0.config(background='#403027')

ab.Auswahlbereich(tkFenster0)

tkFenster0.mainloop()