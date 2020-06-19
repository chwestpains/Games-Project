##To Do:
#Fix size of hearts and life count down
from tkinter import *
import random

window = Tk()
window.title('Burger Dash!')

canvas = Canvas(window, width=750, height=750, bg="black")

canvas.pack()

background = PhotoImage(file="background.png")
canvas.create_image(375,375, image=background)

title = canvas.create_text(375,375, text="Burger Dash!", fill="white", font=("Helvetica", 30))

directions = canvas.create_text(375,475, text="Avoid the rotton burgers!", fill="white", font = ("Helvetica", 20))

score = 0
hearts = 0
heartsImages = ["3hearts.png", "2hearts.png", "1heart.png"]
hearts_image = PhotoImage(file=heartsImages[hearts])
heartsLevel = canvas.create_image(650, 40, image=hearts_image)

score_display = canvas.create_text(60, 20, text="Score: " + str(score), fill="white", font=("Helvetica", 20))


level = 1
level_display = canvas.create_text(60, 60, text="Level: " + str(level), fill="white", font=("Helvetica", 20))


player_image = PhotoImage(file="bobstill2.png")

mychar = canvas.create_image(375, 710, image=player_image)


goodBurger_image = PhotoImage(file="burger4.png")
badBurger_image = PhotoImage(file="badburger1.png")


burger_list = []
bad_burger_list = []
burger_speed = 2
burger_type = [goodBurger_image,goodBurger_image,goodBurger_image,goodBurger_image,goodBurger_image,badBurger_image]

def make_burger():
    global burger_type
    xposition = random.randint(1,750)

    thisBurger = random.choice(burger_type)
    burger = canvas.create_image(xposition,0, image=thisBurger)

    burger_list.append(burger)

    if thisBurger == burger_type[5]:
        bad_burger_list.append(burger)


    window.after(1000, make_burger)

def move_burger():
    for burger in burger_list:
        canvas.move(burger, 0, burger_speed)

        if canvas.coords(burger)[1] > 750:
            xposition = random.randint(1,750)
            canvas.coords(burger, xposition, 0)

    window.after(50, move_burger)

def update_score_level():
    global score, level, burger_speed, score_display, level_display
    score += 1
    canvas.delete(score_display)
    score_display = canvas.create_text(60, 40, text=("Score: " + str(score)), fill="white", font=("Helvetica", 20))

    if score > 5 and score <= 10:
        burger_speed += 1
        level = 2
        canvas.delete(level_display)
        level_display = canvas.create_text(60, 60, text="Level: " + str(level), fill="white", font=("Helvetica", 20))
    elif score > 10:
        burger_speed += 1
        level = 3
        canvas.delete(level_display)
        level_display = canvas.create_text(60, 60, text="Level: " + str(level), fill="white", font=("Helvetica", 20))

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

def update_hearts(burger):
    canvas.delete(burger)
    burger_list.remove(burger)
    bad_burger_list.remove(burger)
    canvas.delete(heartsLevel)
    hearts += 1
    hearts_image = PhotoImage(file=heartsImages[hearts])
    heartsLevel = canvas.create_image(650, 40, image=hearts_image)
    return hearts

    
def check_hits():
    global hearts, heartsLevel
    for burger in bad_burger_list:
        if collisions(mychar, burger, 30):
            update_hearts(burger)
            game_over = canvas.create_text(375,375, text="Game Over", fill="red", font=("Helvetica", 30))
            window.after(2000,end_game_over)
            return       

    for burger in burger_list:
        if collisions(mychar, burger, 40):
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
    if move_direction == "Right" and canvas.coords(mychar)[0] < 750:
        canvas.move(mychar, 10,0)
    if move_direction == "Left" and canvas.coords(mychar)[0] > 0:
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
