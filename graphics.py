import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import *

tkWindow = Tk()
def dashboard():

    global dashboardPage
    dashboardpage = Toplevel(tkWindow)
    dashboardpage.title("Dashboard")
    dashboardpage.geometry("300x300")

    user_button = Button(register_page, text="Register", width=10, height=1, bg="black", command=new_user)
    user_button.pack()

    employee_button = Button(register_page, text="Register", width=10, height=1, bg="black", command=new_user)
    employee_button.pack()

    product_button = Button(register_page, text="Register", width=10, height=1, bg="black", command=new_user)
    product_button.pack()

    category_button = Button(register_page, text="Register", width=10, height=1, bg="black", command=new_user)
    category_button.pack()

    brands_button = Button(register_page, text="Register", width=10, height=1, bg="black", command=new_user)
    brands_button.pack()

def register():
    global register_page
    register_page = Toplevel(tkWindow)
    register_page.title("Register")
    register_page.geometry("300x300")

    global userid
    global username
    global password
    global username_enter
    global password_enter
    global userid
    userid = IntVar()
    username = StringVar()
    password = StringVar()
    Label(register_page, text="Please enter User Details", bg="grey").pack()
    Label(register_page, text="").pack()
    Label(register_page, text="Userid:-").pack()
    username_enter = Entry(register_page, textvariable=userid).pack()
    Label(register_page, text="Username:-").pack()
    username_enter = Entry(register_page, textvariable=username).pack()
    Label(register_page, text="Password:-").pack()
    password_enter = Entry(register_page, textvariable=password, show="*").pack()
    Label(register_page, text="").pack()
    register_button = Button(register_page, text="Register", width=10, height=1, bg="black", command=new_user)
    register_button.pack()

def new_user():
    user = USER()
    userId = userid.get()
    userName = username.get()
    pwd = password.get()
    print(userName)
    print(pwd)
    user.insert_user(userId, userName, pwd)

def display_U():
    user = USER()
    users = user.display_users()
    global user_table
    global display_user
    # display_user = Toplevel(display_list)
    display_user.title("Users")
    display_user.geometry("300x250")
    # Button(display_user,text="Add").pack()
    # Button(display_user,text="delete").pack()
    user_table = ttk.Treeview(display_user, column=("c1", "c2", "c3"), show='headings')

    for user in users:
        user_table.insert("", tk.END, values=user)
        # print("password: " + user[2])
    user_table.column("#1", anchor=tk.CENTER)
    user_table.heading("#1", text="userid")
    user_table.column("#2", anchor=tk.CENTER)
    user_table.heading("#2", text="username")
    user_table.column("#3", anchor=tk.CENTER)
    user_table.heading("#3", text="password")
    user_table.bind('<ButtonRelease-1>', selectUsr)
    user_table.grid()
    user_table.pack()

# def login():
#     global login_page
#     login_page = Toplevel(tkWindow)
#     login_page.title("Login")
#     login_page.geometry("300x250")
#
#     global login_username
#     global login_password
#     global login_username_enter
#     global login_password_enter
#     global userid
#     userid = 1
#     login_username = StringVar()
#     login_password = StringVar()
#
#     Label(login_page, text="Please detail if you already registerd", bg="grey").pack()
#     Label(login_page, text="").pack()
#     Label(login_page, text="Username:-").pack()
#     login_username_enter = Entry(login_page, textvariable=login_username).pack()
#     Label(login_page, text="Password:-").pack()
#     login_password_enter = Entry(login_page, textvariable=login_password, show="*").pack()
#     Label(login_page, text="").pack()
#     Button(login_page, text="Login", width=10, height=1, bg="blue", command=exist_user).pack()

def main():
    tkWindow.geometry("300x250")
    tkWindow.title("Account Login")
    Button(text="login", height="2", width="30", command=register).pack()
    tkWindow.mainloop()

if __name__ == "__main__":
    main()