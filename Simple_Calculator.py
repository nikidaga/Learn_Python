from tkinter import *


def buttonClick(number):
    current = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, str(current)+str(number))


def buttonClear():
    myEntry.delete(0, END)


def buttonAdd():
    firstNumber = myEntry.get()
    global fnum
    global math
    math = "Addition"
    fnum = int(firstNumber)
    myEntry.delete(0, END)


def buttonSubtract():
    firstNumber = myEntry.get()
    global fnum
    global math
    math = "Subtraction"
    fnum = int(firstNumber)
    myEntry.delete(0, END)


def buttonMultiply():
    firstNumber = myEntry.get()
    global fnum
    global math
    math = "Multiplication"
    fnum = int(firstNumber)
    myEntry.delete(0, END)


def buttonDivide():
    firstNumber = myEntry.get()
    global fnum
    global math
    math = "Division"
    fnum = int(firstNumber)
    myEntry.delete(0, END)


def buttonEqual():
    secondNumber = myEntry.get()
    myEntry.delete(0, END)
    if math == "Addition":
        myEntry.insert(0, fnum+int(secondNumber))

    if math == "Subtraction":
        myEntry.insert(0, fnum-int(secondNumber))

    if math == "Multiplication":
        myEntry.insert(0, fnum*int(secondNumber))

    if math == "Division":
        myEntry.insert(0, fnum/int(secondNumber))


root = Tk()
root.title("Simple Calculator")

myEntry = Entry(root, width=25, borderwidth=5)
myEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define buttons

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))

addButton = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
subtractButton = Button(root, text="-", padx=40, pady=20, command=buttonSubtract)
multiplyButton = Button(root, text="*", padx=43, pady=20, command=buttonMultiply)
divideButton = Button(root, text="/", padx=41, pady=20, command=buttonDivide)
equalButton = Button(root, text="=", padx=90, pady=20, command=buttonEqual)
clearButton = Button(root, text="Clear", padx=80, pady=20, command=buttonClear)

# Put buttons on screen

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button0.grid(row=4, column=0)
clearButton.grid(row=4, column=1, columnspan=2)

addButton.grid(row=5, column=0)
equalButton.grid(row=5, column=1, columnspan=2)

subtractButton.grid(row=6, column=0)
multiplyButton.grid(row=6, column=1)
divideButton.grid(row=6, column=2)

root.mainloop()
