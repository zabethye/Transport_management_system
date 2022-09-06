from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector

#Creating Main window
login_page = Tk()
login_page.geometry("740x370")
login_page.title("Transport Management System v.0.1")

login_or_register_label = Label(login_page, text = "Log in to your account", font=('Helvetica 20 underline'))
login_or_register_label.grid(row= 0, column= 1)

###LOG_IN=============LOG_IN==============LOG_IN###
#Putting empty lines and Log In text
empty_line = Label(login_page, text = " ", font=5)
empty_line.grid(row = 1, column = 0)
log_in_text = Label(login_page, text = "You have an account? Log In", font=('Helvetica 15 italic'))
log_in_text.grid(row = 2, column = 0)
empty_line = Label(login_page, text = " ")
empty_line.grid(row = 3, column = 0)

#Creating username box
username_label = Label(login_page, text = "Enter Your Username:  ", font=5)
username_label.grid(row = 4, column = 0)
username = StringVar()
username_entry = ttk.Entry(login_page, textvariable=username, font=5)
username_entry.grid(row=4, column=1)

#Creating password box
password_label = Label(login_page, text = "Enter Your Password:  ", font=5)
password_label.grid(row=5, column=0)
password = StringVar()
password_entry = ttk.Entry(login_page, textvariable=password, show="*", font=5)
password_entry.grid(row=5, column=1)

#Creating Log In button and forwarding to transport management system
def log_in():
    #MySQL connection
    from test import connect_password
    db = mysql.connector.connect(host='localhost', user='root', password=connect_password,
                                 database="transport_management_system")
    mycursor = db.cursor()
    mycursor.execute("select * FROM users where username = '"+ username.get() +"' and password = '"+ password.get() +"';")
    my_result = mycursor.fetchone()
    if my_result == None:
        messagebox.showerror("Error!", "Invalid username or password!")
    else:
        messagebox.showinfo("Success!", "Successfully Login!")
        db.close()
        mycursor.close()
        login_page.destroy()
        import main_window
        main_window

log_in_btn = Button(login_page, text="Log In", command=log_in, font=5)
log_in_btn.grid(row=6, column=2)
empty_line = Label(login_page, text = " ", font=5)
empty_line.grid(row = 7, column = 0)


###REGISTER=============REGISTER==============REGISTER###
#Putting Register text
empty_line = Label(login_page, text = " ").grid(row = 8, column = 0)
register_text = Label(login_page, text = "Don't have an account?       \n Let's make one!", font=('Helvetica 15 italic'))
register_text.grid(row=9, column=0)

#Forwarding to register window with button
def register_click():
    login_page.destroy()
    import register_form
    register_form

forward_to_registration_window = Button(login_page, text="Register New User!", command=register_click, font=5)
forward_to_registration_window.grid(row=10, column=2)

login_page.mainloop()
