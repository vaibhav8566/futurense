"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
"""
import turtle
from random import *
#from py_tkinter import func
from turtle import *
import time
from freegames import vector
import sqlite3
import smtplib
import maskpass
# global flappy_score

#
def sm(email,score):
    #print(type(score),score)
    sd=str(score)
    if sd!="":
        db = sqlite3.connect("data.db")
        # query=f'''UPDATE gamer_details set floppy={sd} where email={email}'''
        db.execute(f"UPDATE gamer_details set floppy='{sd}' where email='{email}'")
        db.commit()
        send_add = "ap9213479@gmail.com"
        rec_add = str(email)
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        # pwd = maskpass.askpass(mask="")
        s.login(send_add,'GameUpdates*123')

        # message to be sent
        SUBJECT='FLAPPY SCORE'
        TEXT = f"Your flappy score is {sd}"
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # sending the mail
        s.sendmail(send_add, rec_add, message)

        # terminating the session
        s.quit()
        print("Mail Sent")
    #print("myy",score)
    #print("hello",type(email),email)
    #print("hello",type(sd),sd)


k=0
e_l=""
score=''
def f_Flappy(email):
    global score
    global e_l
    e_l=email
    bird = vector(0, 0)
    balls = []
    global k

    #unit='seconds'
    start_time = time.time()
    minutes = 0
    second = 0
    print_score = ""


    def tap(x, y):
        """Move bird up in response to screen tap."""
        up = vector(0, 30)
        bird.move(up)


    def inside(point):
        """Return True if point on screen."""
        return -200 < point.x < 200 and -200 < point.y < 200


    def draw(alive):
        """Draw screen objects."""
        clear()
        global score

        goto(bird.x, bird.y)

        if alive:
            dot(10, 'green')
        else:
            dot(10, 'red')
            score = time.time() - start_time
            if score > 60:
                minutes = score//60
                second = round((score - minutes*60),2)
                print_score = f"Score : {minutes} minutes and {second} seconds"
                # flappy_score=print_score

                #unit='minutes'
                #print("rty",score)
                # return score
            else:
                print_score = f"Score : {round(score,2)} seconds"
                print(print_score)
                #print(temp_var1)
                # return score
                #print("adf",score)
            print("aadf",print_score)
            #k=print_score
            #print("asd",k)




        for ball in balls:
            goto(ball.x, ball.y)
            dot(20, 'black')

        update()


    def move():
        """Update object positions."""
        bird.y -= 5

        for ball in balls:
            ball.x -= 3

        if randrange(10) == 0:
            y = randrange(-199, 199)
            ball = vector(199, y)
            balls.append(ball)

        while len(balls) > 0 and not inside(balls[0]):
            balls.pop(0)

        if not inside(bird):
            draw(False)
            return

        for ball in balls:
            if abs(ball - bird) < 15:
                draw(False)
                return

        draw(True)
        ontimer(move, 50)
    #print(email)


    setup(420, 420, 370, 0)
    hideturtle()

    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()

    # turtle.reset()
    # turtle.Terminator()
    # turtle.exitonclick()
#f_Flappy("vt8566@gmail.com")
#sm(e_l,score)
#print(turtle.Terminator)

