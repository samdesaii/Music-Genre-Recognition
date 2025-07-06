# first base gui

import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import pickle

'''with open('model.pkl', 'rb') as f:,
    svm = pickle.load(f)'''

window = tkinter.Tk()
window.title("MusicGenreClassifier")
window.wm_iconbitmap('icon.ico')
window.resizable(False, False)
window.geometry("300x400")

label = tkinter.Label(window, text="Coming soon", pady='10').place(x=0, y=0)
opn = Button(window, text='Open', command=lambda: open_file()).place(x=0, y=50)


def open_file():
    file = askopenfile(mode='r')
    if file is not None:
        content = file.read()
        print(content)


window.mainloop()
