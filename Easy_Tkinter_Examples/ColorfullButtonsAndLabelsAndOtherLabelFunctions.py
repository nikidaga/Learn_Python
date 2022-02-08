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