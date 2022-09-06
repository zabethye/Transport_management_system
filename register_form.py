from tkinter import *
from tkinter import messagebox, ttk

#Creating register window

register_page = Tk()
register_page.geometry("700x400")
register_page.title("Register User")

#Adding registration title onpage
registration_label = Label(register_page, text="Register New User", font=('Helvetica 20 underline'))
registration_label.grid(row=0, column=1)

#Creating empty lane
empty_lane = Label(register_page, text=" ")
empty_lane.grid(row=1, column=0)

#Creating username box
username_label = Label(register_page, text="Enter your username:     ", font=5)
username_label.grid(row=2, column=0)
username = StringVar()
username_entry = ttk.Entry(register_page, textvariable=username, font=5)
username_entry.grid(row=2, column=1)

#Creating password box
password_label = Label(register_page, text="Enter your password:     ", font=5)
password_label.grid(row=3, column=0)
password = StringVar()
password_entry = ttk.Entry(register_page, textvariable=password, show="*", font=5)
password_entry.grid(row=3, column=1)

#Creating email box
email_label = Label(register_page, text="Enter your E-mail:          ", font=5)
email_label.grid(row=4, column=0)
email = StringVar()
email_entry = ttk.Entry(register_page, text=email, font=5)
email_entry.grid(row=4, column=1)

#Creating first name box
first_name_label = Label(register_page, text="Enter your first name:     ", font=5)
first_name_label.grid(row=6, column=0)
first_name = StringVar()
first_name_entry = ttk.Entry(register_page, text=first_name, font=5)
first_name_entry.grid(row=6, column=1)

#Creating last name box
last_name_label = Label(register_page, text="Enter your last name:      ", font=5)
last_name_label.grid(row=7, column=0)
last_name = StringVar()
last_name_entry = ttk.Entry(register_page, text=last_name, font=5)
last_name_entry.grid(row=7, column=1)

#Creating position box
position_label = Label(register_page, text="Enter your position:         ", font=5)
position_label.grid(row=8, column=0)
position = StringVar()
position_entry = ttk.Entry(register_page, text=position, font=5)
position_entry.grid(row=8, column=1)

#Creating telephone number box
phone_number_label = Label(register_page, text="Enter your phone number:", font=5)
phone_number_label.grid(row=9, column=0)
phone_number = StringVar()
phone_number_entry = ttk.Entry(register_page, text=phone_number, font=5)
phone_number_entry.grid(row=9, column=1)

#Creating validation method and register button

def registration_validation(event=None):
    str_username = username.get()
    str_password = password.get()
    str_email = email.get()
    str_phone_number = phone_number.get()
    if len(str_username) > 3:
        if len(str_password) > 4:
            if not email.get():
                messagebox.showerror("Error!", "Please, enter your E-mail address!")
                return
            elif not first_name.get():
                messagebox.showerror("Error!", "Please, enter your first name!")
                return
            elif not last_name.get():
                messagebox.showerror("Error!", "Please, enter your last name!")
                return
            elif not position.get():
                messagebox.showerror("Error!", "Please, enter your position!")
                return
            elif len(str_phone_number) != 10:
                messagebox.showerror("Error!", "Please, enter a valid phone number!")
                return
            import re
            regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            if re.fullmatch(regex, str_email):
                register_page.destroy()
                import main_window
                main_window
                return
            messagebox.showerror("Error!", "Enter a valid E-mail address!")
            return
        messagebox.showerror("Error!", "Your password must be at least 5 characters!")
        return
    messagebox.showerror("Error!", "Your username must be at least 4 characters!")

register_btn = Button(register_page, text="Register!", command=registration_validation, font=5)
register_btn.grid(row=10, column=1)
register_page.bind('<Return>', registration_validation)

register_page.mainloop()