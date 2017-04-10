from tkinter import *

def weight():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)
# Creates the window
window = Tk()

# Creates a label field
label = Label(window, text="KG")
label.grid(row=0, column=0)

# Creates an entry field
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Creates a button
b1 = Button(window, text="Convert", command=weight)
b1.grid(row=0, column=2)


# Creates text field
t1 = Text(window,height=1,width=20)
t1.grid(row=1, column=0)

t2 = Text(window,height=1,width=20)
t2.grid(row=1, column=1)

t3 = Text(window,height=1,width=20)
t3.grid(row=1, column=2)



# Keeps the window open
window.mainloop()
