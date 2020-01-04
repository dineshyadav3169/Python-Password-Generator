from tkinter import  *
from string import *
import random
import pyperclip

class MyGui:
    def __init__(self,window):
        self.window = window
        window.title('Password Generator')
        window.config(bg='lightblue')

        self.button = Button(window, text='Generate',font=('blod',12) , command=passGen, padx=10)
        self.button_quit = Button(window, text ='Quit', command=quitapp)
        self.button.grid(row=5,column=4,pady=4,padx=5)
        self.button_quit.grid(row=6,column=4)


def quitapp():
    quit()

def passGen():
    ranpass = "".join([random.choice(ascii_letters + digits) for n in range(12)])
    label1 = Label(window, text=f'   {ranpass}    ',font=('italic',9), bg='green')
    label1.grid(column=6,row=5)
    pyperclip.copy(ranpass)
    copy_btu = Button(window, text='Copy')
    copy_btu.grid(row=6,column=5)

window = Tk()
gui=MyGui(window)
window.geometry('350x100')
window.mainloop()