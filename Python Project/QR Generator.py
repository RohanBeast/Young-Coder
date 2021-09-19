from tkinter import *
from os import startfile
import qrcode

class GUI(Tk):
    def __init__(self):
        super().__init__()

        self.title("QR Code Generator")
        self.geometry("300x250")

    def data(self):
        data = StringVar()

        fr = Frame()
        Label(fr, text="Enter the data: ").grid()
        Entry(fr, textvariable=data).grid()
        fr.pack()

        def sub():
            dataG = data.get()

            qr = qrcode.make(data=dataG)
            qr.save("QR.png")
            startfile("QR.png")

        Button(self, text="Submit", command=sub).pack()

if __name__ == "__main__":
    app = GUI()
    app.data()
    app.mainloop()