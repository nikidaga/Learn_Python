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