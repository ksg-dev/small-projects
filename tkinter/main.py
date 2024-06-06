from tkinter import *

def button_clicked():
    print("I got clicked")
    message = input.get()
    my_label["text"] = message

window = Tk()
window.title("My GUI")
window.minsize(width=500, height=300)
# add padding to all widgets in window
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I am a label", font=("Corbel", 24, "bold"))
my_label.config(text="New label")
# my_label.pack()

# use place instead of pack for better position control - very specific
# TOP LEFT IS (0, 0)
# my_label.place(x=10, y=0)

# use grid to organize without having to know the exact position of everything
# layout is relative to everyone
# start with first thing in top left and make that col 0, row 0 then go from there
my_label.grid(column=0, row=0)
# add padding only to specific widget
my_label.config(padx=50, pady=50)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Button
button = Button(text="Party Button", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
