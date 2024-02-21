from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
french_word = ""
english_word = ""
num = 0
my_dict = []

#------------------------------------PUTTING WORDS ON THE CARD----------------------#
def next_card():
    global french_word, english_word, flip_timer, num, my_dict
    window.after_cancel(flip_timer)
    try:
        df = pd.read_csv(r"C:\Users\koush\PycharmProjects\days100code\DAY-31\data\words_to_learn.csv")
    except:
        df = pd.read_csv(r"C:\Users\koush\PycharmProjects\days100code\DAY-31\data\french_words.csv")
    my_dict = df.to_dict(orient="records")
    num = random.randint(0, len(my_dict)-1)
    french_word = my_dict[num]["French"]
    english_word = my_dict[num]["English"]
    flash_frame.itemconfig(canvas_img, image=old_img)
    flash_frame.itemconfig(card_title, text="French")
    flash_frame.itemconfig(card_word, text=french_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    flash_frame.itemconfig(canvas_img, image=new_img)
    flash_frame.itemconfig(card_title, text="English")
    flash_frame.itemconfig(card_word, text=english_word, fill="white")

def is_known():
    my_dict.pop(num)
    new_df = pd.DataFrame(my_dict)
    new_df.to_csv(r"C:\Users\koush\PycharmProjects\days100code\DAY-31\data\words_to_learn.csv", index=False)
    next_card()


#-------------------------------------UI INTERFACE----------------------------------
window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
flash_frame = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
flash_frame.grid(row=0, column=0, columnspan=2)
flash_frame.config(highlightthickness=0)
old_img = PhotoImage(file = r"C:\Users\koush\PycharmProjects\days100code\DAY-31\images\card_front.png")
new_img = PhotoImage(file = r"C:\Users\koush\PycharmProjects\days100code\DAY-31\images\card_back.png")
canvas_img = flash_frame.create_image(400, 263, image=old_img)
card_title = flash_frame.create_text(400,150, text="French", font=("Ariel", 40, "italic"))
card_word = flash_frame.create_text(400, 263, text="french word", font=("Ariel", 40, "bold"))
right_img = PhotoImage(file=r"C:\Users\koush\PycharmProjects\days100code\DAY-31\images\right.png")
left_img = PhotoImage(file=r"C:\Users\koush\PycharmProjects\days100code\DAY-31\images\wrong.png")
right_button = Button(image=right_img, width=70, height=70, bg="green",command =is_known)
flash_frame.create_window(600, 400, window=right_button)
left_button = Button(image=left_img, width=70, height=70, bg="red", command=next_card)
flash_frame.create_window(200, 400, window=left_button)
next_card()

window.mainloop()

