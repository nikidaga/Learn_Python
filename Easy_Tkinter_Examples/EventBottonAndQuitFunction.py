from tkinter import *


class testButtons:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text="Print", command=self.printMessege)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)
    
    def printMessege(self):
        print("Just testing a button! Nothing to see here! :-)")


window = Tk()
test = testButtons(window)
window.mainloop()