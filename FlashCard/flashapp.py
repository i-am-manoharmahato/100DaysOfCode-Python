from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
word_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/500_Spanish_to_English.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


# word_dict = data.to_dict(orient='records')


def populate_new_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(word_dict)
    spanish_word = current_word["Spanish"]
    canvas.itemconfigure(canvas_word_lang, text="Spanish", fill="black")
    canvas.itemconfigure(canvas_word, text=spanish_word, fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_word_lang, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)


def already_known():
    word_dict.remove(current_word)
    populate_new_word()
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Learn Spanish..")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card)
canvas_word_lang = canvas.create_text(400, 150, fill="black", text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, fill="black", text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Button

check_btn_img = PhotoImage(file="images/tick.png")
known_button = Button(image=check_btn_img, highlightthickness=0, command=already_known)
known_button.grid(column=1, row=1)

cross_btn_img = PhotoImage(file="images/cross.png")
unknown_btn = Button(image=cross_btn_img, highlightthickness=0, command=populate_new_word)
unknown_btn.grid(column=0, row=1)

populate_new_word()

window.mainloop()
