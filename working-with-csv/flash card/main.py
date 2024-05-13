from tkinter import *
import pandas as pd
import random as r
import time


BACKGROUND_COLOR = "#B1DDC6"
FRONT_SIDE_IMAGE = "images\card_front.png"
BACK_SIDE_IMAGE = "images\card_back.png"
CORRECT_BUTTON_IMAGE = "images\right.png"
INCORRECT_BUTTON_IMAGE = "images\wrong.png"
DATA_FILE_PATH = "data\french_words.csv"
USER_DATA_PATH = "data\user_progress.csv"

# ------------------------------------- IMPORTING DATA ---------------------------------------------- #

try:
    data_file = pd.read_csv(USER_DATA_PATH)
except FileNotFoundError:
    data_file = pd.read_csv(DATA_FILE_PATH)

finally:
    progress_data = {row.French: row.English for (
        index, row) in data_file.iterrows()}

# ----------------------------------- DISPLAY ANSWER ------------------------------------------------ #


def show_answer():
    fr_word = bg_canvas.itemcget(card_word, "text")
    en_word = progress_data[fr_word]

    bg_canvas.itemconfigure(language, text="English", fill="white")
    bg_canvas.itemconfigure(card_word, text=en_word, fill="white")
    bg_canvas.itemconfigure(card_img, image=back_img)
    correct_button.config(command=remove_word)


# --------------------------------- REMOVE ANSWERED WORDS ------------------------------------------- #


def remove_word():
    en_word = bg_canvas.itemcget(card_word, "text")
    fr_word = list(
        filter(lambda x: progress_data[x] == en_word, progress_data))[0]

    del progress_data[fr_word]

    unanswered = pd.DataFrame([progress_data]).T
# -----------------
    unanswered.columns = ['French']
    unanswered.columns = unanswered.columns.astype(str).str.strip()
    unanswered['English'] = unanswered['French'].apply(
        lambda x: progress_data.get(x, ""))

    print(unanswered)
    unanswered.to_csv(USER_DATA_PATH)

    next_card()


# ---------------------------------- GENERATE FRENCH WORD ------------------------------------------- #


def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    front_img = PhotoImage(file=FRONT_SIDE_IMAGE)
    fr_word = r.choice(list(progress_data.keys()))
    bg_canvas.itemconfigure(language, text="French", fill="black")
    bg_canvas.itemconfigure(card_word, text=fr_word, fill="black")
    bg_canvas.itemconfigure(card_img, image=front_img)
    correct_button.config(command=next_card)

    flip_timer = window.after(3000, show_answer)


# ----------------------------------------- UI ------------------------------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, show_answer)

# card background image
bg_canvas = Canvas(width=800, height=526,
                   bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file=FRONT_SIDE_IMAGE)
back_img = PhotoImage(file=BACK_SIDE_IMAGE)
card_img = bg_canvas.create_image(400, 263, image=front_img)
language = bg_canvas.create_text(
    400, 150, text="French", font=("Arial", 40, "italic"))
card_word = bg_canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"))
bg_canvas.grid(row=0, column=0, columnspan=2)

# correct button
correct_img = PhotoImage(file=CORRECT_BUTTON_IMAGE)
correct_button = Button(image=correct_img, command=next_card)
correct_button.grid(row=1, column=1)

# incorrect button
incorrect_img = PhotoImage(file=INCORRECT_BUTTON_IMAGE)
incorrect_button = Button(image=incorrect_img, command=next_card)
incorrect_button.grid(row=1, column=0)

next_card()

window.mainloop()
