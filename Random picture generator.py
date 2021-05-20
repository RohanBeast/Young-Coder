from math import pi
from tkinter import *
import tkinter.messagebox as msgbox
import os
from PIL import Image, ImageTk
import random


def picturePlace():
    root = Tk()
    files = os.listdir()
        
    images = []

    for item in files:
        ext = os.path.splitext(item)[1].lower()

        if ext == ".jpg" or ext == ".png":
                images.append(item)
        else:
            pass
        
    selected = random.choices(images)[0]
    extS = os.path.splitext(selected)[1].lower()

    def back():
        root.destroy()

        app = WelcomeScreen()
        app.headers()
        app.inputs()
        app.mainloop()
    
    def refresh():
        root.destroy()
        picturePlace()

    Button(root, width=20, text="Back", command=back).pack()
    Button(root, width=20, text="Refresh", command=refresh).pack()

    if extS == ".png":
        pic = PhotoImage(file=selected)
        Label(root, image=pic).pack()
    elif extS == ".jpg":
        img = ImageTk.PhotoImage(Image.open(selected))
        Label(root, image=img).pack()

    root.title("Tk Graphics")
    root.geometry("1000x700")
    root.mainloop()


class WelcomeScreen(Tk):
    def __init__(self):
        super().__init__()

        self.loc = os.getcwd()
        self.geometry("660x440")
        self.title("Tk Graphics")
        self.config(borderwidth=1, relief=SUNKEN)
    
    def headers(self):
        Label(self, text=f"Welcome {os.getlogin()}", font="Ebrima 17", fg="black", width=1000, bg="light blue").pack()
        Label(self, text="Give a directory name to locate pictures!", fg="black", width=1000, font="Ebrima 13", bg="light blue").pack()
    
    def inputs(self):
        dirVar = StringVar()
        area = Frame(self)

        Label(area, text="Directory: ", font='Ebrima 13').grid(row=0, column=0)
        Entry(area, textvariable=dirVar, width=40).grid(row=0, column=1)
        area.pack(pady=40)

        def submit():
            directory = dirVar.get()
            if len(directory) == 0:
                msgbox.showinfo("Tk Graphics", "Please Give a folder location")
            else:
                try:
                    os.chdir(directory)
                except FileNotFoundError:
                    msgbox.showinfo("Tk Graphics", "This location was not found on your system")
                else:
                    self.destroy()

                    picturePlace()

        Button(self, text="Submit", bg="light green", relief=RIDGE, command=submit).pack()


if __name__ == "__main__":
    app = WelcomeScreen()
    app.headers()
    app.inputs()
    app.mainloop()