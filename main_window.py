import tkinter
from tkinter import *
from tkinter import ttk
#Make main window
home_window = tkinter.Tk()
home_window.state('zoomed')
home_window.title("Transport Management System v.0.1")

#colours
top_label_colour = "#2222A0"
background_colour = "#CBCBCB"
buttons_backround = "#E3E3E3"
#Make top frame with 2 labels with text
top_frame = Frame(home_window, width=1536, height=100, bg=top_label_colour, borderwidth=4, relief="ridge")
top_frame.place(x=0, y=0)

label_on_top = Label(top_frame, text="Transport Management System", bg=top_label_colour, fg="white",
                     font="Helvetica 25 bold")
label_on_top.place(x=15, y=15)

second_label_on_top = Label(top_frame, text="For the Future...", bg=top_label_colour, fg="white",
                            font="Helvetica 20 italic")
second_label_on_top.place(x=400, y=55)

#made main frame
main_frame = Frame(home_window, width=1692, height=700, bg=background_colour)
main_frame.place(x=0, y=100)

#made button frame
buttons_frame = Frame(main_frame, width=1536, height=50, borderwidth=4, bg=background_colour, relief="raised")
buttons_frame.place(x=0, y=0)

trucks_button = Button(buttons_frame, text="Автомобили", font="Helvetica 15 ", bg=buttons_backround, relief='raised')
trucks_button.place(x=0, y=0)

destinations_button = Button(buttons_frame, text="Курсове", font="Helvetica 15 ", bg=buttons_backround, relief='raised')
destinations_button.place(x=130, y=0)

drivers_button = Button(buttons_frame, text="Водачи", font="Helvetica 15", bg=buttons_backround, relief='raised')
drivers_button.place(x=226, y=0)

finance_button = Button(buttons_frame, text="Финанси", font="Helvetica 15", bg=buttons_backround, relief='raised')
finance_button.place(x=313, y=0)

settings_button = Button(buttons_frame, text="Настройки", font="Helvetica 15", bg=buttons_backround, relief='raised')
settings_button.place(x=1415, y=0)

home_window.mainloop()