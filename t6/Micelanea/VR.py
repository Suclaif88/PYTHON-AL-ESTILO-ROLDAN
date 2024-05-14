from tkinter  import *
from tkinter import messagebox
import random
def no():
 messagebox.showinfo(' ', 'LO SABIA BRO' '\U0001F92B')
 quit()

def motionMouse (event):
  btnYes.place(x=random.randint(0,  500), y=random.randint(0, 500))


root = Tk()
root.geometry('600x600')
root.title('SOBREVIVE')
root.resizable(width=False, height=False)
root[ 'bg' ] = 'white'

label = Label(root, text='ERES GAY?', font='Arial 20 bold', bg='white').pack()
btnYes = Button(root, text='NO', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='SI', font='Arial 20 bold', command=no).place(x=350, y=100)

root.mainloop()