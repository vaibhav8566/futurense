import tkinter as tk
import datetime
import sqlite3
#from tkcalendar import Calendar
import re

import Flappy
import Pacman
import Pong
from Pacman import *
from Pong import *
from Flappy import *
import turtle


def validate_mail(mail_id):
    regex_name = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if re.search(regex_name, mail_id):
        return True
    else:
        return False


def cont_sign(a, b, nm, ag, em):
    any_var = 1
    if a.get() == b.get():
        db.execute(
            "CREATE TABLE IF NOT EXISTS gamer_details(name CHAR(30) NOT NULL, age TEXT NOT NULL, email CHAR(30) PRIMARY KEY NOT NULL, password CHAR(15) NOT NULL, packman varchar(50), pong varchar(50), floppy varchar(50))")
        data = db.execute("SELECT email FROM gamer_details").fetchall()
        result = []

        for t in data:
            result.append(t[0])
        temp_var = em.get()
        name_var = nm.get()

        fal = None
        if len(name_var) == 0:
            fal = tk.Label(text="The Name is not Valid give a nice name ", font=("Comic Sans", 16), bg="light green")
            em.delete(0, "end")
            a.delete(0, "end")
            b.delete(0, "end")
            fal.place(x=15, y=270)
        if validate_mail(temp_var):
            pass
        else:
            fal = tk.Label(text="The Email is not Valid give a nic email", font=("Comic Sans", 16), bg="light green")
            em.delete(0, "end")
            a.delete(0, "end")
            b.delete(0, "end")
            fal.place(x=15, y=270)

        if temp_var in result:
            fal = tk.Label(text="The email id is already registered  ", font=("Comic Sans", 16), bg="light green")
            em.delete(0, "end")
            a.delete(0, "end")
            b.delete(0, "end")
            fal.place(x=15, y=270)
        else:
            db.execute("INSERT INTO gamer_details(name, age, email, password) VALUES(?, ?, ?, ?)",
                       [nm.get(), ag.get(), em.get(), a.get()])
            db.commit()
            nm.delete(0, "end")
            ag.delete(0, "end")
            em.delete(0, "end")
            a.delete(0, "end")
            b.delete(0, "end")
            if fal:
                fal.destroy()
            tk.Label(text="Sign Up Successful", font=("Comic Sans", 16), bg="light green").place(x=15, y=270)

    else:
        lab = tk.Label(text="Please verify the correct password", font=("Comic Sans", 12), bg="light green", fg="red")
        lab.place(x=15, y=270)


def func(var1, var2):
    game = tk.Tk()
    game.geometry("500x350")
    game.resizable(False, False)
    game.config(bg="light green")
    data = db.execute("SELECT email FROM gamer_details").fetchall()

    res = []

    for t in data:
        res.append(t[0])
    temp_var1 = var1.get()

    if temp_var1 in res:
        info = db.execute(f"SELECT password FROM gamer_details WHERE email='{temp_var1}'").fetchall()
        if var2.get() == info[0][0]:

            game1 = tk.Label(game, text="Please Select a Game to Play", font=("Arial", 20), bg="light green")
            game1.pack(side="top")

            game1 = tk.Button(game, text="PACMAN", font=("Comic Sans", 12), bg="blue", fg="white", command=lambda: f_Pacman(temp_var1))
            game1.place(x=100, y=100)
            game1 = tk.Button(game, text="PONG", font=("Comic Sans", 12), bg="blue", fg="white", command=lambda: f_Pong(temp_var1))
            game1.place(x=100, y=150)
            game1 = tk.Button(game, text="FLAPPY", font=("Comic Sans", 12), bg="blue", fg="white", command=lambda: f_Flappy(temp_var1))
            game1.place(x=100, y=200)
            tk.mainloop()
            #Flappy.sc(temp_var1,score)
        else:
            inval = tk.Label(text="Plase enter valid password", bg="light green", fg="red")
            inval.pack()
    else:
        inval1 = tk.Label(text="Plase enter valid email", bg="light green", fg="red")
        inval1.pack()
    print("myyy",Flappy.score)
    Flappy.sm(temp_var1,Flappy.score)
    Pong.sm1(temp_var1,Pong.print_score)
    Pacman.fun(temp_var1, Pacman.state)



def log_in():
    global anyo
    root.destroy()
    anyo = tk.Tk()
    anyo.geometry("500x350")
    anyo.resizable(False, False)
    anyo.title("Login Page")
    anyo.config(bg="light green")
    tk.Label(bg="light green").pack()
    login = tk.Label(anyo, text="Welcome to the Login Page", font=("Comic Sans", 24, "bold"), bg="light green")
    login.pack(side="top")

    uname = tk.Label(anyo, text="Enter the email id", font=("Comic Sans", 16), bg="light green")
    uname.pack(side="top")
    utxt = tk.Entry()

    utxt.pack(side="top")
    utxt.bind("<Return>", lambda temp6: passw.focus())
    passw = tk.Label(anyo, text="Enter the password", font=("Comic Sans", 16), bg="light green")
    passw.pack(side="top")

    ptxt = tk.Entry(show="*")
    ptxt.pack(side="top")
    ptxt.bind("<Return>", lambda temp7: func(utxt, ptxt))
    blank = tk.Label(bg="light green")
    blank.pack(side="top")
    logbut = tk.Button(anyo, text="Click here to Login", font=("Comic Sans", 12), bg="blue", fg="white",
                       command=lambda: func(var1=utxt, var2=ptxt))
    logbut.pack(side="top")

    label = tk.Label(anyo, text="Time", font=("Comic Sans", 10, "bold"), bg="light blue")
    label.place(x=390, y=0)
    while True:
        time = str(datetime.datetime.now().time())
        label.config(text=time[:-7])
        anyo.update()


def sign_up():
    root.destroy()
    sign = tk.Tk()
    sign.geometry("500x350")
    sign.resizable(False, False)
    sign.config(bg="light green")

    tk.Label(sign, text="Create a Free Account", font=("Comic Sans", 20, "bold"), bg="light green").place(x=45, y=20)

    tk.Label(sign, text="Please enter your name", font=("Comic Sans", 16), bg="light green").place(x=15, y=70)

    name = tk.Entry(sign, width=20)
    name.place(x=300, y=70)

    name.bind("<Return>", lambda temp1: email.focus())

    tk.Label(sign, text="Please enter your age", font=("Comic Sans", 16), bg="light green").place(x=15, y=110)

    age = tk.Entry(sign, width=20)
    age.place(x=300, y=110)

    age.bind("<Return>", lambda temp2: email.focus())

    tk.Label(sign, text="Please enter your email id", font=("Comic Sans", 16), bg="light green").place(x=15, y=150)

    email = tk.Entry(sign, width=20)
    email.place(x=300, y=150)

    email.bind("<Return>", lambda temp3: password.focus())

    tk.Label(sign, text="Please enter the password", font=("Comic Sans", 16), bg="light green").place(x=15, y=190)

    password = tk.Entry(sign, show="*", width=20)
    password.place(x=300, y=190)

    password.bind("<Return>", lambda temp4: re_password.focus())

    tk.Label(sign, text="Please re-enter the password", font=("Comic Sans", 16), bg="light green").place(x=15, y=230)

    re_password = tk.Entry(sign, show="*", width=20)
    re_password.place(x=300, y=230)

    re_password.bind("<Return>", lambda temp5: cont_sign(a=password, b=re_password, nm=name, ag=age, em=email))

    sign_cont = tk.Button(sign, text="Sign Up", bg="light blue", font=("Comic Sans", 12, "bold"),
                          command=lambda: cont_sign(a=password, b=re_password, nm=name, ag=age, em=email))
    sign_cont.place(x=350, y=300)

    sign_cont = tk.Button(sign, text="Login", bg="light blue", font=("Comic Sans", 12, "bold"), command=log_in)
    sign_cont.place(x=100, y=300)

    label = tk.Label(sign, text="Time", font=("Comic Sans", 10, "bold"), bg="light blue")
    label.place(x=440, y=0)

    while True:
        time = str(datetime.datetime.now().time())
        label.config(text=time[:-7])
        sign.update()

    tk.mainloop()


root = tk.Tk()
root.geometry("400x250")
root.resizable(False, False)
root.title("Login Page")
root.config(bg="light green")
db = sqlite3.connect("data.db")

tk.Label(root, text="Please Sign Up to Login", font=("Comic Sans", 20, "bold"), bg="light green").place(x=45, y=20)

tk.Label(root, text="To create an account: ", font=("Comic Sans", 16), bg="light green").place(x=15, y=70)

sign_but = tk.Button(root, text="Sign Up", bg="light blue", font=("Comic Sans", 12, "bold"), command=sign_up)
sign_but.place(x=170, y=110)

tk.Label(root, text="For an existing account:", font=("Comic Sans", 16), bg="light green").place(x=15, y=150)

log_but = tk.Button(root, text="Login", bg="light blue", font=("Comic Sans", 12, "bold"), command=log_in)
log_but.place(x=175, y=190)

label = tk.Label(root, text="Time", font=("Comic Sans", 10, "bold"), bg="light blue")
label.place(x=340, y=0)

while True:
    time = str(datetime.datetime.now().time())
    label.config(text=time[:-7])
    root.update()
tk.mainloop()