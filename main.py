# Nopad GUI application using Python Tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def helpfun():
    showinfo('Notepad', 'Notepad by Dipak Chandrakant Mali')


def newfun():
    global fp
    root.title("Untitled - Notepad")
    fp = None
    textArea.delete(1.0, END)


def openfun():
    global fp
    fp = askopenfilename(defaultextension=".txt", filetype=[
                         ("All Files", "*.*"), ("Text Document", "*.txt")])
    if fp == "":
        fp = None
    else:
        root.title(os.path.basename(fp) + " - Notepad")
        textArea.delete(1.0, END)
        n = open(fp, 'r')
        textArea.insert(1.0, n.read())
        n.close()


def savefun():
    global fp
    if fp == None:
        fp = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetype=[
            ("All Files", "*.*"), ("Text Document", "*.txt")])

        if fp == "":
            fp = None
        else:
            # Save as new file
            n = open(fp, "w")
            n.write(textArea.get(1.0, END))
            n.close()
            root.title(os.path.basename(fp) + " - Notepad")
    else:
        # Save file
        n = open(fp, "w")
        n.write(textArea.get(1.0, END))
        n.close()


def cutfun():
    textArea.event_generate(("<<Cut>>"))


def copyfun():
    textArea.event_generate(("<<Copy>>"))


def pastefun():
    textArea.event_generate(("<<Paste>>"))


if __name__ == '__main__':

    root = Tk()

    fp = None

    root.title("Notepad : By Dipak Mali")
    root.iconbitmap('icon.ico')
    root.geometry("500x400")

    # Text Area
    sbr = Scrollbar(root, orient=VERTICAL)
    sbr.pack(side=RIGHT, fill=Y)
    textArea = Text(root, font='Lucida 15 bold', yscrollcommand=sbr.set)
    textArea.pack(fill=BOTH)

    # Scroll Bar
    sbr.config(command=textArea.yview)

    # Menu Bar
    menuBar = Menu(root)

    file = Menu(menuBar, tearoff=0)
    file.add_command(label="New", command=newfun)
    file.add_command(label="Open", command=openfun)
    file.add_command(label="Save", command=savefun)
    file.add_separator()
    file.add_command(label='Exit', command=root.destroy)
    menuBar.add_cascade(label='File', menu=file)

    edit = Menu(menuBar, tearoff=0)
    edit.add_command(label="Cut", command=cutfun)
    edit.add_command(label="Copy", command=copyfun)
    edit.add_command(label="Paste", command=pastefun)
    menuBar.add_cascade(label='Edit', menu=edit)

    h = Menu(menuBar, tearoff=0)
    h.add_command(label='View Help', command=helpfun)
    menuBar.add_cascade(label='Help', menu=h)

    root.config(menu=menuBar)

    root.mainloop()
