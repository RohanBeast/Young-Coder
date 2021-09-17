from tkinter import *
from tkinter import messagebox as msg
import os
from pygame import mixer


class Main(Tk):
    def __init__(self):
        super().__init__()

        self.title("VOX: Music Player")
        self.geometry("1200x670")
    
    def head(self):
        Label(self, text="VOX", font="Arial 25").pack()
        Label(self, text="Music Player", font="Arial 15").pack()

    def music_list(self):
        try:
            os.chdir(f"C:/Users/{os.getlogin()}/Music")
            files = os.listdir()

            lst = Listbox()

            for item in files:
                lst.insert(END, item)

            lst.pack(fill=X, padx=10)
        except FileNotFoundError:
            msg.showerror("Your Windows Directory is not C:")

    def playArea(self):
        name = StringVar()
        i = StringVar()
        i.set("||")


        def play():
            track = name.get()
            if track != "":
                mixer.init()
                mixer.music.load(track)
                mixer.music.play(10)

        fr = Frame()
        Label(fr, text="Enter The Name ").grid(row=1, column=0)
        Entry(fr, textvariable=name).grid(row=1, column=1)
        Button(fr, command=play, text="Play", padx=5).grid(row=2, column=0)

        fr.pack(anchor="nw", pady=20, padx=10)

        def playP():
            if i.get() == "||":
                i.set("|>")
                mixer.music.pause()
                btn.update()
            elif i.get() == "|>":
                i.set("||")
                mixer.music.unpause()
                btn.update()

        btn = Button(self, padx=10, pady=3, textvariable=i, command=playP)
        btn.pack(side=BOTTOM, pady=30)

if __name__ == "__main__":
    app = Main()
    app.head()
    app.music_list()
    app.playArea()
    app.mainloop()
