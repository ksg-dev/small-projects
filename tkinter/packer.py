import tkinter

window = tkinter.Tk()
window.title("Yee Yee")
window.minsize(width=500, height=300)

# Create Label
my_label = tkinter.Label(text="I am a label", font=("Corbel", 24, "bold"))
# Place object on screen and top center - Packer docs for ref args kwargs
my_label.pack()




# Keep screen up and listening
window.mainloop()
