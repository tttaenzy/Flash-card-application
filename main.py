BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

current_card={}
to_learn={}
#-------Create new flash card
try:
    data=pd.read_csv("data/known_word.csv")
except FileNotFoundError:
    original=pd.read_csv("data/french_words.csv")
    to_learn=original.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(french,text="French",fill="black")
    canvas.itemconfig(meaning,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer=window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(french,text="English",fill="white")
    canvas.itemconfig(meaning,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back)

def right_button():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("data/known_word.csv",index=False)
    next_card()
# --------------------UI interface------------
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)
# ----- image upload
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_background=canvas.create_image(400, 263, image=card_front)
card_back=PhotoImage(file="images/card_back.png")
french=canvas.create_text(400,150,text="French", font=("Ariel", 40, "italic"))
meaning=canvas.create_text(400,263,text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0,columnspan=2)


# ------Button------------
right = PhotoImage(file="images/right.png")
rightButton = Button(image=right, highlightthickness=0, command=right_button)
rightButton.grid(row=1, column=0)

wrong = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrong, highlightthickness=0, command=next_card)
wrongButton.grid(row=1, column=1)

next_card()






window.mainloop()


