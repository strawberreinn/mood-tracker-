import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random  # for random greetings

root = tk.Tk()

root.title("moodifyy: your personal mood tracker")
root.configure(bg="#FFFDDD")
root.minsize(400, 400)

icon = tk.PhotoImage(file="mylogo.png")
root.iconphoto(True, icon)

# ===== HOMEPAGE =====
top_image = tk.PhotoImage(file="mylogo.png")
small_image = top_image.subsample(2, 2)
image_label = tk.Label(root, image=small_image, bg="#FFFDDD")
image_label.pack(pady=0)

label = tk.Label(
    root, 
    text="✿ moodifyy ✿",
    font=("Arial Rounded MT Bold", 85),
    justify="center",
    bg="#FFFDDD",
    fg="hot pink"
)
label.pack(pady=0)

caption = tk.Label(
    root, 
    text="your personal mood tracker",
    font=("Kristen ITC", 20),
    justify="center",
    bg="#FFFDDD",
    fg="hot pink"
)
caption.pack(pady=5)

input_frame = tk.Frame(root, bg="#FFFDDD")
input_frame.pack(pady=18)

# ===== INPUT NAME =====
name_label = tk.Label(
    input_frame,
    text="Enter your name here",
    font=("Arial Rounded MT Bold", 16),
    bg="#FFFDDD",
    fg="hot pink"
)
name_label.pack(pady=7)  # equalized spacing

name_entry = tk.Entry(
    input_frame, 
    font=("Kristen ITC", 12),  
    width=40,
    fg="hot pink",   
    bg="white",
    relief="groove",
    justify="center",  # center the text
    validate="key"
)
name_entry.pack(pady=5)  # equalized spacing

# ===== INPUT DATE =====
date_label = tk.Label(
    input_frame,
    text="Enter the date today (mm-dd-yy)",
    font=("Arial Rounded MT Bold", 16),
    bg="#FFFDDD",
    fg="hot pink"
)
date_label.pack(pady=3)  # equalized spacing

date_entry = tk.Entry(
    input_frame, 
    font=("Kristen ITC", 12), 
    width=40,
    fg="hot pink",   
    bg="white",
    relief="groove",
    justify="center",  # center the text
    validate="key"
)
date_entry.pack(pady=5)  # equalized spacing

# ===== VALIDATION =====
def validate_name(P):
    return P.isalpha() or P == ""

def validate_date(P):
    allowed = "0123456789-"
    return all(c in allowed for c in P) or P == ""

name_entry.config(validatecommand=(root.register(validate_name), "%P"))
date_entry.config(validatecommand=(root.register(validate_date), "%P"))

def move_to_date(event):
    date_entry.focus()

name_entry.bind("<Return>", move_to_date)

def check_date_format(date_text):
    if len(date_text) != 8:
        return False
    if date_text[2] != '-' or date_text[5] != '-':
        return False
    mm, dd, yy = date_text.split('-')
    if not (mm.isdigit() and dd.isdigit() and yy.isdigit()):
        return False
    if not (1 <= int(mm) <= 12):
        return False
    if not (1 <= int(dd) <= 31):
        return False
    return True

# ===== GREETINGS LABELS =====
greeting_label = tk.Label(
    root,
    font=("Arial Rounded MT Bold", 45),
    bg="#FFFDDD",
    fg="hot pink"
)

random_greeting_label = tk.Label(
    root,
    font=("Kristen ITC", 20),
    bg="#FFFDDD",
    fg="hot pink"
)

# ===== SECOND PAGE MENU =====
second_menu_frame = tk.Frame(root, bg="#FFFDDD")

button1 = tk.Button(
    second_menu_frame,
    text="Add Entry",
    font=("Arial Rounded MT Bold", 20),
    fg="black",
    bg="#F7C767",
    activeforeground="#F7C767",
    relief="groove",
    width=20,
    pady=8
)
button1.pack(pady=20)

button2 = tk.Button(
    second_menu_frame,
    text="Edit Entries",
    font=("Arial Rounded MT Bold", 20),
    fg="black",
    bg="#F7C767",
    relief="groove",
    width=20,
    pady=8
)
button2.pack(pady=20)

button3 = tk.Button(
    second_menu_frame,
    text="View Stats",
    font=("Arial Rounded MT Bold", 20),
    fg="black",
    bg="#F7C767",
    activeforeground="#F7C767",
    relief="groove",
    width=20,
    pady=8
)
button3.pack(pady=20)

# ===== RETURN TO HOMEPAGE =====
def return_home():
    greeting_label.place_forget()
    random_greeting_label.place_forget()
    second_menu_frame.place_forget()

    name_entry.delete(0, END)
    date_entry.delete(0, END)

    image_label.pack(pady=0)
    label.pack(pady=0)
    caption.pack(pady=5)
    input_frame.pack(pady=10)
    button_frame.pack(pady=13)

button4 = tk.Button(
    second_menu_frame,
    text="Exit",
    font=("Arial Rounded MT Bold", 20),
    fg="black",
    bg="#F7C767",
    activeforeground="#F7C767",
    relief="groove",
    width=20,
    pady=8,
    command=return_home
)
button4.pack(pady=20)

# ===== RANDOM GREETINGS LIST =====
greetings_list = [
    "✿ hope u have a great day!!",
    "✿ keep smiling :)",
    "✿ make today amazing!!",
    "✿ slay your day!!",
    "✿ stay positive and happy!",
    "✿ let's track some moods!"
]

# ===== START BUTTON LOGIC =====
def start_action():
    name = name_entry.get().strip()
    date = date_entry.get().strip()

    if not name or not date:
        messagebox.showwarning("Incomplete Data", "Please enter both name and date!")
    elif not check_date_format(date):
        messagebox.showwarning("Invalid Date", "Please enter the date in mm-dd-yy format!")
    else:
        greeting_label.config(text=f"Hello, {name}!")
        greeting_label.place(x=10, y=10)

        # Random greeting (slightly bigger and moved slightly right)
        random_greeting = random.choice(greetings_list)
        random_greeting_label.config(text=random_greeting, font=("Kristen ITC", 24))
        random_greeting_label.place(x=30, y=85)

        # Hide homepage
        input_frame.pack_forget()
        button_frame.pack_forget()
        label.pack_forget()
        caption.pack_forget()
        image_label.pack_forget()

        # Show second page menu buttons
        second_menu_frame.place(relx=0.5, rely=0.55, anchor="center")

# ===== START BUTTON =====
button_frame = tk.Frame(root, bg="#FFFDDD")
button_frame.pack(pady=13)

start_button = tk.Button(
    button_frame,
    text=" START ",
    font=("Arial Rounded MT Bold", 20),
    fg="black",
    bg="#F7C767",
    activeforeground="#F7C767",
    relief="groove",
    command=start_action
)
start_button.pack(pady=16)

root.mainloop()
