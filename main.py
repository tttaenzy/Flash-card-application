BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

# --------------------UI interface------------
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ----- image upload
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# -----Label----------
title = Label(text="French", font=("Ariel", 40, "italic"), bg="white")
title.place(x=300, y=150)

word = Label(text="trouve", font=("Ariel", 60, "bold"), bg="white")
word.place(x=300, y=263)

# ------Button------------
right = PhotoImage(file="images/right.png")
rightButton = Button(image=right, highlightthickness=0)
rightButton.grid(row=1, column=0)

wrong = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrong, highlightthickness=0)
wrongButton.grid(row=1, column=1)

window.mainloop()
