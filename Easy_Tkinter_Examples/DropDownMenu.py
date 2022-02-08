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