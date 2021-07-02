from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x450")
        self.title("Atlas Simulator")
        self.configure(bg="black")
    
    def headers(self):
        Label(self, text="Atlas Simulator", font="Arial 20", fg="white", bg="red", width=1000, pady=10).pack()
    
    def searchArea(self):
        searchVar = StringVar()
        CountryVar = StringVar()
        CountryVar.set("")

        frm = Frame(self, bg="black")
        Label(frm, text="Enter The Letter", bg="black", fg="white", font="Goldman 14").pack()
        Entry(frm, textvariable=searchVar, width=50).pack()
        c = Label(frm, bg="black", fg="white", textvariable=CountryVar)
        c.pack()
        frm.pack(pady=40)

        def search():
            with open("Countries.txt", "r") as f:
                r = f.read().lower().splitlines()
            
            ls = []
            for item in r:
                if item.startswith(searchVar.get().lower()):
                    item = item.replace("\t\t\t", "")
                    ls.append(item)
            
            CountryVar.set(str(ls))
            c.update()

        Button(self, text="Search", bg="light blue", font="arial 11", command=search).pack()


if __name__ == "__main__":
    app = GUI()
    app.headers()
    app.searchArea()
    app.mainloop()