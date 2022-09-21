import tkinter
from tkinter import *
from tkinter import ttk
#Make main window
home_window = tkinter.Tk()
home_window.state('zoomed')
home_window.title("Transport Management System v.0.1")

#Make top frame with 2 labels with text
top_label_colour = "#2222A0"
background_colour = "#CBCBCB"
top_frame1 = Frame(home_window, width=1536, height=100, bg=top_label_colour, borderwidth=4, relief="ridge")
top_frame1.place(x=0, y=0)

label_on_top = Label(top_frame1, text="Transport Management System", bg=top_label_colour, fg="white",
                     font="Helvetica 25 bold")
label_on_top.place(x=15, y=15)

second_label_on_top = Label(top_frame1, text="For the Future...", bg=top_label_colour, fg="white",
                            font="Helvetica 20 italic")
second_label_on_top.place(x=400, y=55)

# make frame for the buttons
buttons_frame = Frame(home_window, width=1692, height=700, bg=background_colour)
buttons_frame.place(x=0, y=100)

home_window.mainloop()