from tkinter import *
#Creating Main window


login_page = Tk()
login_page.geometry("740x370")
login_page.title("Transport Management System v.0.1")


login_or_register_label = Label(login_page, text = "Log in to your account", font=('Helvetica 20 underline')).grid(row= 0, column= 1)

#Putting empty lines and Log In text
empty_line = Label(login_page, text = " ", font=5).grid(row = 1, column = 0)
log_in_text = Label(login_page, text = "You have an account? Log In", font=('Helvetica 15 italic')).grid(row = 2, column = 0)
empty_line = Label(login_page, text = " ").grid(row = 3, column = 0)

#Creating username box
username_label = Label(login_page, text = "Enter Your Username:  ", font=5).grid(row = 4, column = 0)
username = StringVar()
username_entry = Entry(login_page, textvariable=username, font=5).grid(row=4, column=1)

#Creating password box
password_label = Label(login_page, text = "Enter Your Password: ", font=5). grid(row=5, column=0)
password = StringVar()
password_entry = Entry(login_page, textvariable=password, show="*", font=5). grid(row=5, column=1)

#Creating Log In button and forwarding to transport management system
log_in_btn = Button(login_page, text="Log In", font=5).grid(row=6, column=2)
empty_line = Label(login_page, text = " ", font=5).grid(row = 7, column = 0)

#Putting Register text
empty_line = Label(login_page, text = " ").grid(row = 8, column = 0)
register_text = Label(login_page, text = "Don't have an account?       \n Let's make one!", font=('Helvetica 15 italic')).grid(row=9, column=0)

#Forwarding to register window with button
def when_clicked():
    login_page.destroy()
    import register_form
    register_form

forward_to_registration_window = Button(login_page, text="Register New User!", command=when_clicked, font=5).grid(row=10, column=2)

login_page.mainloop()
