import random
from tkinter import *
import json
from tkinter import messagebox
import sys
import os

# Get the path to the user's documents directory
documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')

# Create a directory for your program's data if it doesn't exist
data_dir = os.path.join(documents_dir, 'MyProgramData')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
images_dir = os.path.join(data_dir, 'images')
if not os.path.exists(images_dir):
    os.makedirs(images_dir)
image_files = ['card_front.png', 'card_back.png', 'right.png', 'wrong.png', 'flip.png']
for image_file in image_files:
    image_path = os.path.join(images_dir, image_file)
    if not os.path.exists(image_path):
        print(f"Error: {image_file} not found in {images_dir}")


jp_base_data = os.path.join(os.path.dirname(__file__), 'data', 'japanese_data.json')


BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91C2AF"
WD_HEIGHT = 750
WD_WIDTH = 800

front_text = ""
back_text = ""
flipped = False
new_cards = {}
repeat_cards_saved = {}
long_term_saved = {}
jp_current_data = {}
in_lt_deck = False
in_repeat_deck = False
is_empty_lt = True
is_empty_rp = True


# Window Items -------------------------------------------------------------------------------#
window = Tk()
window.configure(width=WD_HEIGHT,height=WD_WIDTH,highlightthickness=0, bg=BACKGROUND_COLOR)
window.resizable(False, False)
selected_deck = StringVar()
selected_deck.set("Decks")

# Canvas Items -------------------------------------------------------------------------------#
card_front = PhotoImage(file=os.path.join(sys._MEIPASS, 'images', 'card_front.png'))
card_back = PhotoImage(file=os.path.join(sys._MEIPASS, 'images', 'card_back.png'))
right_img = PhotoImage(file=os.path.join(sys._MEIPASS, 'images', 'right.png'))
wrong_img = PhotoImage(file=os.path.join(sys._MEIPASS, 'images', 'wrong.png'))
flip_img = PhotoImage(file=os.path.join(sys._MEIPASS, 'images', 'flip.png'))
canvas = Canvas(bg=BACKGROUND_COLOR,height=WD_HEIGHT,width=WD_WIDTH,highlightthickness=0)
image_id =canvas.create_image(WD_WIDTH/2, WD_HEIGHT/2.7, image=card_front)
canvas.grid(column=0,row=0,columnspan=2,padx=50,pady=50)
# read/write data ------------------------------------------------------------------------------#

def read_data(new_card_deck, repeat_deck, long_term_deck):
    global data_dir, documents_dir,is_empty_rp,is_empty_lt
    if new_card_deck:
        try:
            with open(jp_base_data, mode="r", encoding="utf-8") as read_file:
                data = json.load(read_file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(title="Oops", message="Sorry you do not have a Deck made yet.")
    elif repeat_deck:
        print(data_dir)
        try:
            with open(os.path.join(data_dir, 'repeat_cards_saved.json'), mode="r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            is_empty_rp = False
            messagebox.showinfo(title="Oops", message="Sorry you do not have a Deck made yet.")
        is_empty_rp = True

    elif long_term_deck:
        try:
            with open(os.path.join(data_dir, 'long_term_saved.json'), mode="r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            is_empty_lt = False
            messagebox.showinfo(title="Oops", message="Sorry you do not have a Deck made yet.")
        is_empty_lt = True

def write_data(long_term_saved_cards, repeat_saved_cards, save_front, save_back):
    """When saving you need to turn on the section with a True and reset the others to False
        long_term_saved_cards,    repeat_saved_cards
            slot 1                      slot 2      """
    global data_dir, documents_dir,is_empty_rp,is_empty_lt
    if repeat_saved_cards:
        try:
            with open(os.path.join(data_dir, 'repeat_cards_saved.json'), mode="r", encoding="utf-8") as read_file:
                to_update = json.load(read_file)
        except (FileNotFoundError, json.JSONDecodeError):
            to_update = {}
        save_this = {front_text: back_text}
        to_update.update(save_this)

        with open(os.path.join(data_dir, 'repeat_cards_saved.json'), mode="w", encoding="utf-8") as write_file:
            if save_front and save_back:
                json.dump(to_update, write_file, indent=4, ensure_ascii=False)
        is_empty_rp = True
    if long_term_saved_cards:
        try:
            with open(os.path.join(data_dir, 'long_term_saved.json'), mode="r", encoding="utf-8") as read_file:
                to_update = json.load(read_file)
        except (FileNotFoundError, json.JSONDecodeError):
            to_update = {}
        save_this = {front_text: back_text}
        to_update.update(save_this)
        with open(os.path.join(data_dir, 'long_term_saved.json'), mode="w", encoding="utf-8") as write_file:
            if save_front and save_back:
                json.dump(to_update, write_file, indent=4, ensure_ascii=False)
        is_empty_lt = True

def lt_save():
    global front_text,back_text
    if front_text and back_text:
        write_data(True,False,front_text,back_text)
        messagebox.showinfo(title="Data Saved",message=f"You saved {front_text} \nto your long term deck")

def repeat_save():
    global front_text,back_text
    if front_text and back_text:
        write_data(False,True,front_text,back_text)
        messagebox.showinfo(title="Data Saved", message=f"You saved {front_text} \nto your repeat deck")

# Function Items -------------------------------------------------------------------------------#

def next_card():
    global jp_current_data,front_text,back_text
    if in_lt_deck:
        if is_empty_lt:
            jp_data = read_data(False,False,True)
            while True:
                jp_current_data = random.choice(list(jp_data.keys()))
                if check_for_repeat:
                    break
            front_text = jp_current_data
            back_text = jp_data[jp_current_data]
            bottom_label.config(text=front_text, bg="white")
            canvas.itemconfig(image_id, image=card_front)
            top_label.config(text="Japanese", bg="white")
            flip_button.config(bg="white", activebackground="white")
        else:
            messagebox.showinfo(title="Oops",message="the Deck is empty.\nPick a new card or select a deck.")
    if in_repeat_deck:
        if is_empty_rp:
            jp_data = read_data(False,True,False)
            while True:
                jp_current_data = random.choice(list(jp_data.keys()))
                if check_for_repeat:
                    break
            front_text = jp_current_data
            back_text = jp_data[jp_current_data]
            bottom_label.config(text=front_text, bg="white")
            canvas.itemconfig(image_id, image=card_front)
            top_label.config(text="Japanese", bg="white")
            flip_button.config(bg="white", activebackground="white")
        else:
            messagebox.showinfo(title="Oops",message="the Deck is empty.\nPick a new card or select a deck.")
    elif not in_lt_deck and not in_repeat_deck:
        messagebox.showinfo(title="Oops",message="Your not currently in a deck.\nPick a new card or select a deck.")


def new_card():
    global front_text, back_text, jp_current_data, flipped
    flipped = False
    jp_data = read_data(True, False, False)
    while True:
        jp_current_data = random.choice(list(jp_data.keys()))
        if check_for_repeat:
            break
    front_text = jp_current_data
    back_text = jp_data[jp_current_data]
    bottom_label.config(text=front_text, bg="white")
    canvas.itemconfig(image_id, image=card_front)
    top_label.config(text="Japanese", bg="white")
    flip_button.config(bg="white", activebackground="white")


def flip_card():
    global front_text,card_back,card_front,flipped,back_text,jp_current_data
    if flipped:
        flip_button.config(bg="white",activebackground="white")
        top_label.config(text="Japanese",bg="white")
        bottom_label.config(text=front_text,bg="white")
        canvas.itemconfig(image_id,image=card_front)
        new_text = "aww im back"
        flipped = False
        return
    flip_button.config(bg=CARD_BACK_COLOR,activebackground=CARD_BACK_COLOR)
    top_label.config(text="English",bg=CARD_BACK_COLOR)
    bottom_label.config(text=back_text,bg=CARD_BACK_COLOR)
    canvas.itemconfig(image_id,image=card_back)
    flipped = True


def check_for_repeat():
    if jp_current_data == front_text:
        return False
    else:
        return True
def select_deck(value):
    print(f"Selected deck: {value}")
    global in_lt_deck, in_repeat_deck
    if value == "Decks":
        in_repeat_deck = False
        in_lt_deck = False
    if value == "Repeat Deck":
        in_repeat_deck = True
        in_lt_deck = False
    elif value == "Long Term Deck":
        in_repeat_deck = False
        in_lt_deck = True

#--------------------------------------------------------------------------------------------#
#                                      UI Items                                              #
# Label Items -------------------------------------------------------------------------------#
bottom_label = Label(text="Waiting on users input",bg="white", font=("Arial", 32, "bold"),wraplength=500)
bottom_label.place(relx=0.5, rely=0.38, anchor="center")
top_label = Label(text="Japanese",bg="white", font=("Arial", 40, "italic"))
top_label.place(relx=0.5, rely=0.2, anchor="center")

# Button Items -------------------------------------------------------------------------------#

check_mark_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card, borderwidth=0)
check_mark_button.grid(column=0, row=0,sticky="s",pady=100)
cross_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card, borderwidth=0)
cross_button.grid(column=1, row=0,sticky="s",pady=100)

flip_button = Button(image=flip_img,activebackground="white", highlightthickness=0, bg="white", command=flip_card, borderwidth=0)
flip_button.place(relx=0.82, rely=0.18, anchor="center")

new_word_button = Button(text="New Word", highlightthickness=0, bg=BACKGROUND_COLOR, command=new_card, borderwidth=0
                         ,font=("Arial", 12, "bold"),activebackground=CARD_BACK_COLOR)
new_word_button.place(relx=0.5, rely=0.8, anchor="center")

save_card_lt = Button(text="Save Card to long term deck", highlightthickness=0, bg=BACKGROUND_COLOR, command=lt_save,
                      borderwidth=0,font=("Arial", 12, "bold"),activebackground=CARD_BACK_COLOR)
save_card_lt.place(relx=0.5, rely=0.95, anchor="center")

save_card_repeat = Button(text="Save Card for repeat", highlightthickness=0, bg=BACKGROUND_COLOR, command=repeat_save,
                          borderwidth=0,font=("Arial", 12, "bold"),activebackground=CARD_BACK_COLOR)
save_card_repeat.place(relx=0.5, rely=0.9, anchor="center")

deck_selection = OptionMenu(window, selected_deck,"Decks", "Repeat Deck", "Long Term Deck", command=select_deck)
deck_selection.config(highlightthickness=1,borderwidth=0,bg=CARD_BACK_COLOR,highlightbackground=CARD_BACK_COLOR,
                      font=("Arial", 12, "bold"),activebackground=BACKGROUND_COLOR)
deck_selection.place(relx=0.5, rely=0.85, anchor="center")

# Main Loop -------------------------------------------------------------------------------#

window.mainloop()
