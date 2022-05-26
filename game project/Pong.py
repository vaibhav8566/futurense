

"""Pong, classic arcade game.

Exercises

1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.
"""

from turtle import *
from random import choice, random
import time
from freegames import vector
import sqlite3
import smtplib
import maskpass
import smtplib
import maskpass
def sm1(email,score):
    if(score[8:12] !=""):
        db = sqlite3.connect("data.db")
        # query=f'''UPDATE gamer_details set floppy={sd} where email={email}'''
        db.execute(f"UPDATE gamer_details set pong='{score}' where email='{email}'")
        db.commit()
        send_add = "ap9213479@gmail.com"
        rec_add = str(email)
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        # pwd = maskpass.askpass(mask="")
        s.login(send_add, 'GameUpdates*123')

        # message to be sent
        subject='Pong Score'
        message = f"Your pong score is {score}"

        # sending the mail
        s.sendmail(send_add, rec_add, message)

        # terminating the session
        s.quit()
        print("pong Mail Sent")

        print("myypong",score,email)
print_score=""
po_em=""

def f_Pong(email):
    start_time = time.time()
    minutes = 0
    second = 0
    global print_score
    global po_em
    po_em=email

    def value():
        """Randomly generate value between (-5, -3) or (3, 5)."""
        return (3 + random() * 2) * choice([1, -1])


    ball = vector(0, 0)
    aim = vector(value(), value())
    state = {1: 0, 2: 0}


    def move(player, change):
        """Move player position by change."""
        state[player] += change


    def rectangle(x, y, width, height):
        """Draw rectangle at (x, y) with given width and height."""
        up()
        goto(x, y)
        down()
        begin_fill()
        for count in range(2):
            forward(width)
            left(90)
            forward(height)
            left(90)
        end_fill()


    def draw():
        """Draw game and move pong ball."""
        clear()
        global print_score
        rectangle(-200, state[1], 10, 50)
        rectangle(190, state[2], 10, 50)

        ball.move(aim)
        x = ball.x
        y = ball.y

        up()
        goto(x, y)
        dot(10)
        update()

        if y < -200 or y > 200:
            aim.y = -aim.y

        if x < -185:
            low = state[1]
            high = state[1] + 50

            if low <= y <= high:
                aim.x = -aim.x
            else:


                score = time.time() - start_time
                if score > 60:
                    minutes = score//60
                    second = round((score - minutes*60),2)
                    print_score = f"Score : {minutes} minutes and {second} seconds"
                    print(print_score)
                    #unit='minutes'
                else:
                    print_score = f"Score : {round(score,2)} seconds"
                    print(print_score)
                return

        if x > 185:
            low = state[2]
            high = state[2] + 50

            if low <= y <= high:
                aim.x = -aim.x
            else:

                score = time.time() - start_time
                if score > 60:
                    minutes = score//60
                    second = round((score - minutes*60),2)
                    print_score = f"Score : {minutes} minutes and {second} seconds"
                    print(print_score)
                    #unit='minutes'
                else:
                    print_score = f"Score : {round(score,2)} seconds"
                    print(print_score)
                return

        ontimer(draw, 50)


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: move(1, 20), 'w')
    onkey(lambda: move(1, -20), 's')
    onkey(lambda: move(2, 20), 'i')
    onkey(lambda: move(2, -20), 'k')
    draw()
    done()
    # turtle.reset()
    # turtle.Terminator()
    # turtle.exitonclick()

#f_Pong("vt8566@gmail.com")
#sm1(po_em,print_score)