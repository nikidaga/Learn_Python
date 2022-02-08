from tkinter import *
import tkinter.messagebox

window = Tk()

tkinter.messagebox.showinfo('Info', 'This is just a test!')

answer = tkinter.messagebox.askquestion('Question', 'This is a test. Just ansewr Yes or No')
if answer == 'yes':
    print(":-)")

window.mainloop()