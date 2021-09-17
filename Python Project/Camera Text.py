import cv2
from tkinter import *

class Cam:
    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        self.text = text

    def cam(self):
        cam = cv2.VideoCapture(0)

        while True:
            ret, frame = cam.read()
            a = cv2.putText(frame, self.text, (self.x, self.y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (0, 0, 255), 5)
            cv2.imshow("Window", a)

            k = cv2.waitKey(1)
            if k == ord("a"):
                break
            elif k == ord("q"):
                cv2.imwrite("Capture.png", a)

        cam.release()
        cv2.destroyAllWindows()

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("CamText")


    def main(self):
        xVar = IntVar()
        yVar = IntVar()
        textVar = StringVar()

        Label(self, text="CamText", font="Arial 20").pack()
        fra = Frame(self)
        
        Label(fra, text="X").grid(row=1, column=0)
        Entry(fra, textvariable=xVar).grid(row=1, column=1)

        Label(fra, text="Y").grid(row=2, column=0)
        Entry(fra, textvariable=yVar).grid(row=2, column=1)

        Label(fra, text="Text").grid(row=3, column=0)
        Entry(fra, textvariable=textVar).grid(row=3, column=1)
        fra.pack()

        def submit():
            app = Cam(textVar.get(), xVar.get(), yVar.get())
            app.cam()

        Button(self, command=submit, text="Submit").pack()

if __name__ == "__main__":
    app = GUI()
    app.main()
    app.mainloop()