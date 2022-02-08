from tkinter import *


def test():
    print("Just testing!")

window = Tk()

# ***** Main Menu *****

menu = Menu(window)
window.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New File...", command=test)
subMenu.add_command(label="New...", command=test)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=test)

anotherSubMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=anotherSubMenu)
anotherSubMenu.add_command(label="Redo", command=test)

# ***** Toolbar *****

toolBar = Frame(window, bg="blue")

insertButton = Button(toolBar ,text="Insert Image", command=test)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolBar, text="Print", command=test)
printButton.pack(side=LEFT, padx=2, pady=2)

toolBar.pack(side=TOP, fill=X)

# ***** Status Bar *****

status = Label(window, text="Praparing to test", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

window.mainloop()
from tkinter import *

window = Tk()

canvas = Canvas(window, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")

greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

#canvas.delete(redLine)
#canvas.delete(ALL) #Διαγράφει όλα τα γραφικά χωρίς να χρειάζεται να καλέσουμε την συνάρτηση delete για κάθε ένα ξεχωριστά

window.mainloop()
import win10toast

toaster = win10toast.ToastNotifier()

toaster.show_toast('Python', 'Success! This is working!', duration=10)
from tkinter import *

window = Tk()

photo = PhotoImage(file="clipart4288829.png")
label = Label(window, image=photo)
label.pack()

window.mainloop()
from tkinter import *

window = Tk()


def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")

frame = Frame(window, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)

frame.pack()

window.mainloop()
from tkinter import *
import tkinter.messagebox

window = Tk()

tkinter.messagebox.showinfo('Info', 'This is just a test!')

answer = tkinter.messagebox.askquestion('Question', 'This is a test. Just ansewr Yes or No')
if answer == 'yes':
    print(":-)")

window.mainloop()
from tkinter import *

window = Tk()

nameLabel = Label(window, text="Name")
passwordLabel = Label(window, text="Password")
nameEntry = Entry(window)
passwordEntry = Entry(window)

nameLabel.grid(row=0, sticky=E)
passwordLabel.grid(row=1, sticky=E)
nameEntry.grid(row=0, column=1)
passwordEntry.grid(row=1, column=1)

checkBox = Checkbutton(window, text="Keep me logged in.")
checkBox.grid(columnspan=2)

window = mainloop()
from tkinter import *

window = Tk()


topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text="Button 1", bg="green", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

label1 = Label(window, text="This is a label", bg="red", fg="white")
label1.pack()
label2 = Label(window, text="This is a label", bg="green", fg="black")
label2.pack(fill=X)
label3= Label(window, text="This is a label", bg="blue", fg="white")
label3.pack(side=LEFT, fill=Y)


window.mainloop()
from tkinter import *


def dropDownMenuTest():
    print("I'm just testing something!")


window = Tk()


menu = Menu(window)
window.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project", command=dropDownMenuTest)
subMenu.add_command(label="File", command=dropDownMenuTest)
subMenu.add_separator()
subMenu.add_command(label="New...", command=dropDownMenuTest)

anotherSubMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=anotherSubMenu)
anotherSubMenu.add_command(label="Undo", command=dropDownMenuTest)


window.mainloop()
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
