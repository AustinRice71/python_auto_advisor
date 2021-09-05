from tkinter import *
import tkinter.filedialog
import os
import Grade

root = Tk()

coordsDict = {}

def openFile():
    with tkinter.filedialog.askopenfile(initialdir=os.getcwd(), filetypes=[('Text','*.txt')]) as f:
        for index, line in enumerate(f):
            fields = line.split('|')
            className = fields[0]
            creditHours = fields[1]
            prereqs = fields[2]
            Label(root, text=className, borderwidth=2).grid(row=index,column=0)
            coordsDict[(index,0)] = className
            Label(root, text=creditHours, borderwidth=2).grid(row=index,column=1)
            coordsDict[(index,1)] = creditHours
            Label(root, text=prereqs, borderwidth=2).grid(row=index,column=2)
            coordsDict[(index,2)] = prereqs
            term = StringVar(root, fields[3],)
            coordsDict[(index,3)] = term
            termMenu = OptionMenu(root, term, *{"Fall 2020", "Spring 2021", "Fall 2021"}).grid(row = index, column=3)
            grade = StringVar(root, fields[4])
            coordsDict[(index,4)] = grade
            gradeMenu = OptionMenu(root, grade, *[option.name for option in Grade.Grade]).grid(row=index,column=4)

def saveFile():
    gridSize = root.grid_size()
    with tkinter.filedialog.asksaveasfile(filetypes=[('Text','*.txt')]) as f:
        if f is None:
            return
        for row in range(gridSize[1]):
            # Currently writes random blank lines?
            f.write(f"{coordsDict[(row,0)]}|{coordsDict[(row,1)]}|{coordsDict[(row,2)]}|{coordsDict[(row,3)].get()}|{coordsDict[(row,4)].get()}\n")


def create_widgets():
    menu = Menu(root)
    root.config(menu=menu)

    fileMenu = Menu(menu)
    menu.add_cascade(label="File", menu=fileMenu)
    
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)

create_widgets()

mainloop()
