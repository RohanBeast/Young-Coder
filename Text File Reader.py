from tkinter import *
import tkinter.messagebox as msgbox
import pyttsx3
import os


class Reader(Tk):
    def __init__(self, content, fileName):
        super().__init__()

        self.geometry("900x700")
        self.title("Text File Reader")
        self.content = content
        self.fileName = fileName
    
    def headers(self):
        Label(self, text=f"{self.fileName}", anchor="nw", bg="black", fg="white", width=self.winfo_screenwidth(), font="Arial 20").pack(anchor="nw")
        Label(self, text="Opened...", anchor="nw", font="Arial 12", bg="black", fg="white", width=self.winfo_screenwidth()).pack(anchor="nw")
    
    def Content(self):
        Label(self, text=self.content,  bg="white", width=self.winfo_screenwidth(), height=self.winfo_screenheight(), anchor="nw", padx=10, pady=10, justify=LEFT).pack()


class HomeScreen(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("Text File Reader")
    
    def headers(self):
        Label(self, text="Text File Reader", font="Arial 20").pack()
    
    def Fileinput(self):
        dirVar = StringVar()

        frame = Frame(self)
        Label(frame, text="Enter File name: ").grid(row=1, column=0)
        Entry(frame, textvariable=dirVar).grid(row=1, column=1)
        frame.pack(pady=30)

        def Submit():
            content = dirVar.get()
            
            try:
                with open(content) as f:
                    r = f.read()

                self.destroy()
                app = Reader(fileName=content, content=r)
                app.headers()
                app.Content()
                app.mainloop()
            
            except FileNotFoundError:
                msgbox.showerror("Text File Reader", "The file is not in this directory, please enter a valid file")

        Button(self, text="Submit", command=Submit).pack()
    

app = HomeScreen()
app.headers()
app.Fileinput()
app.mainloop()