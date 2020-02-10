from tkinter import *
import os

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("400x500")
    screen.title("First Screen")
    Text = Label(text="CHOOSE ONE", bg="Red",height=2,width=50,font="Bold").grid(row=1,column=1)
    Label(text="").grid()
    Log = Button(text="LOG IN",height=2,width=10,command=login).grid(row=3,column=1)
    Label(text="").grid()
    Reg = Button(text="Register",height=2,width=10,command=register).grid(row=5,column=1)
    Label(text="").grid()
    Button(text="EXIT",command=exit).grid(row=9,column=1)
    screen.mainloop()



def register():
    global screen1

    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("350x300")

    global username
    global password
    global user_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter the details below:", fg="green").grid(padx=20)
    Label(screen1, text="").grid()
    Label(screen1, text="Username").grid(padx=20)
    user_entry = Entry(screen1, textvariable=username)
    user_entry.grid()
    Label(screen1, text="Password").grid(padx=20)
    password_entry = Entry(screen1, textvariable=password, show="#")
    password_entry.grid()
    Label(screen1, text="Confirm Password").grid(padx=20)
    password_entry2 = Entry(screen1, textvariable=password, show="#")
    password_entry2.grid()
    Label(screen1, text="").grid()
    Button(screen1, text="Register", command=register_user).grid(padx=30)
    Label(screen1, text="").grid()
    Button(screen1, text="Exit", command=exit).grid(row=9, column=3, padx=30)

def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info+".txt","a")
    file.write(username_info+"\n")
    file.write(password_info+"\n")
    file.close()

    user_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Successfull.", fg="Green").grid()



def login():
    global screen2

    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x250")

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global user_entry
    global password_entry

    Label(screen2, text="Please enter the details below to login:",fg="green").grid(padx=20)
    Label(screen2, text="").grid()
    Label(screen2, text="Username").grid(padx=20)
    user_entry = Entry(screen2, textvariable=username_verify)
    user_entry.grid()
    Label(screen2, text="Password").grid(padx=20)
    password_entry = Entry(screen2, textvariable=password_verify, show="#")
    password_entry.grid()
    Label(screen2, text="").grid()
    Button(screen2, text="Login", command=login_verify).grid(padx=30)
    Label(text="").grid()
    Button(screen2, text="Exit", command=exit).grid(row=7, column=3, padx=30)

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    user_entry.delete(0, END)
    password_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Label(screen2,text="Login successfully.",fg="Green",font="bold").grid()
        else:
            Label(screen2,text="Password doesnot match.",fg="red",font="Bold").grid()
    else:
        Label(screen2,text="User not found.",fg="red",font="Bold").grid()

main_screen()