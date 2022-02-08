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