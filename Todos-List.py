from tkinter import *
import tkinter.messagebox as msgbox
import os


class Main(Tk):
    def __init__(self, name):
        super().__init__()

        self.geometry("900x700")
        self.title("Todos-List | Welcome")
        self.name = name
    
    def headers(self):
        Label(self, text="Todos-List", font="Arial 20").pack()
        Label(self, text=f"Welcome {self.name}").pack()
    
    def todos(self):
        title = StringVar()
        task = StringVar()

        frame = Frame(self)
        Label(frame, text="Title").grid(row=1, column=0)
        Label(frame, text="Task").grid(row=1, column=1)

        Entry(frame, textvariable=title).grid(row=2, column=0)
        Entry(frame, width=100, textvariable=task).grid(row=2, column=1)

        def reset():
            title.set("")
            task.set("")
        
        def submit():
            with open("Todos.txt", "a") as f:
                f.write(f"Title: {title.get()} Task: {task.get()}\n")
            
            msgbox.showinfo("Todo-List", "Todo set. Please Check your documents and restart the app.")

        Button(frame, text="Submit", command=submit).grid(row=6, column=0, pady=20)
        Button(frame, text="Reset", command=reset).grid(row=6, column=1, pady=20)

        frame.pack(pady=30, anchor='nw', padx=10)

        try:
            with open("Todos.txt", "r") as f:
                r = f.read().splitlines()
            
            if len(r) == 0:
                Label(self, text="No Todos Yet!").pack()
            
            for item in r:
                Label(self, text=item, bg="light grey", padx=20, pady=10).pack(pady=10)

        except Exception:
            Label(self, text="No Todos Yet!").pack()


class Register(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x500")
        self.title("Todos-List | Register")

    def headers(self):
        Label(self, text="Todos-List", font="Arial 20").pack()
        Label(self, text="Register", font="Arial 12").pack()
    
    def inputs(self):
        name = StringVar()
        password = StringVar()

        frame1 = Frame(self)
        Label(frame1, text="Name: ").grid(row=1, column=0)
        Entry(frame1, textvariable=name).grid(row=1, column=1)

        Label(frame1, text="Set Password: ").grid(row=2, column=0)
        Entry(frame1, textvariable=password).grid(row=2, column=1)

        def submit():
            os.chdir(f"C:/Users/{os.getlogin()}/Documents")

            try:
                os.makedirs("Todo-List")
                os.chdir(f'C:/Users/{os.getlogin()}/Documents/Todo-list')

                try:
                    os.makedirs(name.get())
                    os.chdir(f"C:/Users/{os.getlogin()}/Documents/Todo-list/{name.get()}")

                    with open("User.txt", "a") as file:
                        file.write(f"Username: {name.get()}\nPassword: {password.get()}")
                        msgbox.showinfo("Todo-List", f"Username created for {name.get()}")

                except FileExistsError:
                    msgbox.showerror("Todo-list", "This username is already there")

            except Exception:
                os.chdir(f'C:/Users/{os.getlogin()}/Documents/Todo-list')

                try:
                    os.makedirs(name.get())
                except FileExistsError:
                    msgbox.showerror("Todo-list", "This username is already there")
                else:
                    os.chdir(f"C:/Users/{os.getlogin()}/Documents/Todo-list/{name.get()}")

                    with open("User.txt", "a") as file:
                        file.write(f"Username: {name.get()}\nPassword: {password.get()}")
                        msgbox.showinfo("Todo-List", f"Username created for {name.get()}")

        def login():
            self.destroy()

            app = Login()
            app.headers()
            app.inputs()
            app.mainloop()

        Button(frame1, text="Submit", command=submit).grid(pady=10, row=3, column=0)
        Button(frame1, text="Login", command=login).grid(pady=10, row=3, column=1)

        frame1.pack(pady=20)


class Login(Tk):
    def __init__(self):
        super().__init__()

        self.title("Todos-List | Login")
        self.geometry("400x500")
    
    def headers(self):
        Label(self, text="Todos-List", font="Arial 20").pack()
        Label(self, text="Login", font="Arial 12").pack()
    
    def inputs(self):
        name = StringVar()
        password = StringVar()

        frame1 = Frame(self)
        Label(frame1, text="Name: ").grid(row=1, column=0)
        Entry(frame1, textvariable=name).grid(row=1, column=1)

        Label(frame1, text="Password: ").grid(row=2, column=0)
        Entry(frame1, textvariable=password).grid(row=2, column=1)

        def register():
            self.destroy()
            reg = Register()
            reg.headers()
            reg.inputs()
            reg.mainloop()
        
        def submit():
            try:
                os.chdir(f"C:/Users/{os.getlogin()}/Documents/Todo-list/{name.get()}")

                with open("User.txt", "r") as f:
                    r = f.read().splitlines()
                
                if r[0] != f"Username: {name.get()}":
                    msgbox.showerror("Todo-List", "Username is invalid")
                elif r[1] != f"Password: {password.get()}":
                    msgbox.showerror("Todo-List", "Password is not correct")
                else:
                    msgbox.showinfo("Todo-list", "All things done!")
                    self.destroy()

                    main = Main(name.get())
                    main.headers()
                    main.todos()
                    main.mainloop()

            except Exception:
                msgbox.showerror("Todo-list", "No username found")

        Button(frame1, text="Submit", padx=3, command=submit).grid(row=3, column=0, padx=20, pady=10)
        Button(frame1, text="Register", padx=3, command=register).grid(row=3, column=1, padx=20, pady=10)
        frame1.pack(pady=20)


app = Login()
app.headers()
app.inputs()
app.mainloop()