import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

root.title("moodifyy: your personal mood tracker")
root.configure(bg="#FFFDDD")
root.minsize(400, 400)

icon = tk.PhotoImage(file="mylogo.png")
root.iconphoto(True, icon)

#HOMEPAGE
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
    text="- your personal mood tracker",
    font=("Kristen ITC", 20),
    justify="center",
    bg="#FFFDDD",
    fg="hot pink"
)
caption.pack(pady=5)

input_frame = tk.Frame(root, bg="#FFFDDD")
input_frame.pack(pady=10)

#input name
name_label = tk.Label(
    input_frame,
    text="enter your name here",
    font=("Arial Rounded MT Bold", 16),
    bg="#FFFDDD",
    fg="hot pink"
)
name_label.pack(pady=15)

name_entry = tk.Entry(
    input_frame, 
    font=("Kristen ITC", 14),  
    width=30,
    fg="hot pink",   
    bg="white",
    validate="key"
)
name_entry.pack(pady=3)

#input date
date_label = tk.Label(
    input_frame,
    text="enter the date today (mm-dd-yy)",
    font=("Arial Rounded MT Bold", 16),
    bg="#FFFDDD",
    fg="hot pink"
)
date_label.pack(pady=3)

date_entry = tk.Entry(
    input_frame, 
    font=("Kristen ITC", 14), 
    width=30,
    fg="hot pink",   
    bg="white",
    validate="key"
)
date_entry.pack(pady=2)

def validate_name(P):
    return P.isalpha() or P == ""

def validate_date(P):
    allowed = "0123456789-"
    return all(c in allowed for c in P) or P == ""

name_entry.config(validatecommand=(root.register(validate_name), "%P"))
date_entry.config(validatecommand=(root.register(validate_date), "%P"))

#check date format
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

# main menu
def start_action():
    name = name_entry.get().strip()
    date = date_entry.get().strip()
    if not name or not date:
        messagebox.showwarning("Incomplete Data", "Please enter both name and date!")
    elif not check_date_format(date):
        messagebox.showwarning("Invalid Date", "Please enter the date in mm-dd-yy format!")
    else:
        # greetings
        greeting_label.config(text=f"Hello {name}!")
        greeting_label.place(x=10, y=10)

        # hide
        input_frame.pack_forget()
        button_frame.pack_forget()
        label.pack_forget()
        caption.pack_forget()
        image_label.pack_forget()

        # date
        date_label_result.config(text=f"Today's date: {date}")
        date_label_result.place(x=10, y=50)

#start button
button_frame = tk.Frame(root, bg="#FFFDDD")
button_frame.pack(pady=13)

start_button = tk.Button(
    button_frame,
    text=" start ",
    font=("Arial Rounded MT Bold", 20),
    fg="black",
    bg="#F7C767",
    activebackground="#F7C767",
    activeforeground="hot pink",
    relief="ridge",
    command=start_action
)
start_button.pack(pady=16) 

# greetings
greeting_label = tk.Label(
    root, 
    font=("Kristen ITC", 20), 
    bg="#FFFDDD", fg="hot pink"
)
date_label_result = tk.Label(
    root, 
    font=("Kristen ITC", 16), 
    bg="#FFFDDD", 
    fg="hot pink"
)

root.mainloop()
