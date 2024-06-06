# import this way if using multiple classes
from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# Create Label
my_label = Label(text="I am a label", font=("Corbel", 24, "bold"))
# Place object on screen and top center - Packer docs for ref args kwargs
my_label.pack()

# getting object attribute to change its value
my_label["text"] = "Howdy"

# using config to change value
my_label.config(text="Ay yo")



# Create Buttons
# Function for click
# GOAL: change label text when button is clicked
# def button_click():
#     my_label["text"] = "I got clicked"
#
# # add command to object - no ()
# button = Button(text="Party Button", command=button_click)
#
# # use pack to add to screen
# button.pack()




# Entry Component
input = Entry()
input.pack()

# GOAL: change label to entered text on button click
def button_msg():
    message = input.get()
    my_label["text"] = message

button = Button(text="Click me", command=button_msg)
button.pack()


# Keep screen up and listening
window.mainloop()
