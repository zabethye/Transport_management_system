from tkinter import *
from tkinter import messagebox

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

#Creating validation method and register button

def validation():
    str_username = username.get()
    str_password = password.get()
    if len(str_username) > 3:
        if len(str_password) > 4:
            register_page.destroy()
            import main_window
            main_window
            return
        messagebox.showerror("Error!", "Your password must be at least 5 characters!")
        return
    messagebox.showerror("Error!", "Your username must be at least 4 characters!")

register_btn = Button(register_page, text="Register!", command=validation, font=5).grid(row=4, column=1)

register_page.mainloop()