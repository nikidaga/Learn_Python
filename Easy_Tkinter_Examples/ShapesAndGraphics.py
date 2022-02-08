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