from tkinter import *
#Creating register window
register_page = Tk()
register_page.geometry("700x300")
register_page.title("Register User")

#Adding registration title onpage
registration_label = Label(register_page, text="Register New User", font=('Helvetica 20 underline')).grid(row=0, column=1)

#Creating empty lane
empty_lane = Label(register_page, text=" ").grid(row=1, column=0)

#Creating username box
username_label = Label(register_page, text="Enter your username: ", font=5).grid(row=2, column=0)
username = StringVar()
username_entry = Entry(register_page, textvariable=username, font=5).grid(row=2, column=1)

#Creating password box
password_label = Label(register_page, text="Enter your password: ", font=5).grid(row=3, column=0)
password = StringVar()
password_entry = Entry(register_page, textvariable=password, show="*", font=5).grid(row=3, column=1)

#Creating register button
register_btn = Button(register_page, text="Register!", font=5).grid(row=4, column=1)



register_page.mainloop()