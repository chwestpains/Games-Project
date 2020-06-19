from tkinter import *
import random

window = Tk()
window.title('Burger Dash!')

canvas = Canvas(window, width=400, height=400, bg="black")
canvas.pack()

title = canvas.create_text(200, 200, text="Burger Dash!", fill="white", font=("Helvetica", 30))

directions = canvas.create_text(200, 300, text="Avoid the rotton burgers!", fill="white", font = ("Helvetica", 20))

score = 0

score_display = Label(window, text="Score :" + str(score))
score_display.pack()

level = 1
level_display = Label(window, text="Level :" + str(level))
level_display.pack()

player_image = PhotoImage(file="bobstill.png")

mychar = canvas.create_image(200, 360, image=player_image)


goodBurger_image = PhotoImage(fill="burger3.png")

goodBurger = canvas.create_image((200,200), image=goodBurger_image)

burger_list = []
bad_burger_list = []
burger_speed = 2


def make_burger():
    xposition = random.randint(1,400)

    goodBurger = canvas.create_image((xposition,xposition +30), image=goodBurger_image)

    candy_list.append(candy)

    if candy_color == "red":
        bad_candy_list.append(candy)

    window.after(1000, make_candy)

def move_burger():
    for burger in burger_list:
        canvas.move(burger, 0, burger_speed)

        if canvas.coords(burger)[1] > 400:
            xposition = random.randint(1,400)
            canvas.coords(burger, xposition, 0, xposition+30,30)
    window.after(50, move_burger)

def update_score_level():
    global score, level, burger_speed
    score += 1
    score_display.config(text="Score :" + str(score))

    if score > 5 and score <= 10:
        burger_speed += 1
        level = 2
        level_display.config(text="Level :" + str(level))
    elif score > 10:
        burger_speed += 1
        level = 3
        level_display.config(text="Level :" + str(level))

def end_game_over():
    window.destroy()

def end_title():
    canvas.delete(title)
    canvas.delete(directions)

def collisions(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap

def check_hits():
    for burger in bad_burger_list:
        if collisions(mychar, burger, 50):
            game_over = canvas.create_text(200, 200, text="Game Over", fill="red", font=("Helvetica", 30))
            window.after(2000,end_game_over)
            return

    for burger in burger_list:
        if collisions(mychar, burger, 50):
            canvas.delete(burger)
            burger_list.remove(burger)
            update_score_level()

    window.after(100, check_hits)

move_direction = 0

def check_input(event):
    global move_direction
    key = event.keysym
    if key == "Right":
        move_direction = "Right"
    elif key == "Left":
        move_direction = "Left"

def end_input(event):
    global move_direction
    move_direction = "None"

def move_character():
    if move_direction == "Right" and canvas.coords(mychar)[0] < 400:
        canvas.move(mychar, 10,0)
    if move_direction == "Left" and canvas.coords(mychar)[0] > 0 :
        canvas.move(mychar, -10,0)
    window.after(16, move_character)

canvas.bind_all("<KeyPress>",check_input)
canvas.bind_all("<KeyRelease>", end_input)

window.after(1000, end_title)
window.after(1000, make_burger)
window.after(1000, move_burger)
window.after(1000, check_hits)
window.after(1000, move_character)


window.mainloop()
