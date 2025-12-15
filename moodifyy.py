import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random  # for random greetings

# ===== root window =====
root = tk.Tk()
root.title("moodifyy: your personal mood tracker")
root.configure(bg="#FFFDDD")
root.minsize(400, 400)

icon = tk.PhotoImage(file="mylogo.png")
root.iconphoto(True, icon)

# ===== homepage images and labels =====
top_image = tk.PhotoImage(file="mylogo.png")
small_image = top_image.subsample(2, 2)  # resize the image
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

# ===== input name =====
name_label = tk.Label(
    input_frame,
    text="Enter your name here",
    font=("Arial Rounded MT Bold", 16),
    bg="#FFFDDD",
    fg="hot pink"
)
name_label.pack(pady=7)

name_entry = tk.Entry(
    input_frame,
    font=("Kristen ITC", 12),
    width=40,
    fg="hot pink",
    bg="white",
    relief="groove",
    justify="center",
    validate="key"
)
name_entry.pack(pady=5)

# ===== input date =====
date_label = tk.Label(
    input_frame,
    text="Enter the date today (mm-dd-yy)",
    font=("Arial Rounded MT Bold", 16),
    bg="#FFFDDD",
    fg="hot pink"
)
date_label.pack(pady=3)

date_entry = tk.Entry(
    input_frame,
    font=("Kristen ITC", 12),
    width=40,
    fg="hot pink",
    bg="white",
    relief="groove",
    justify="center",
    validate="key"
)
date_entry.pack(pady=5)

# ===== validation functions =====
def validate_name(P):
    # only letters allowed in name, empty string also allowed
    return P.isalpha() or P == ""

def validate_date(P):
    # only numbers and - allowed in date
    allowed = "0123456789-"
    return all(c in allowed for c in P) or P == ""

name_entry.config(validatecommand=(root.register(validate_name), "%P"))
date_entry.config(validatecommand=(root.register(validate_date), "%P"))

def move_to_date(event):
    # when enter pressed on name entry, move focus to date
    date_entry.focus()

name_entry.bind("<Return>", move_to_date)

def check_date_format(date_text):
    # check if date is exactly mm-dd-yy format
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

# ===== greetings labels =====
greeting_label = tk.Label(
    root,
    font=("Arial Rounded MT Bold", 40),
    bg="#FFFDDD",
    fg="hot pink"
)

random_greeting_label = tk.Label(
    root,
    font=("Kristen ITC", 15),
    bg="#FFFDDD",
    fg="hot pink"
)

# ===== main menu label =====
main_menu_label = tk.Label(
    root,
    text="✿ MAIN MENU ✿",
    font=("Arial Rounded MT Bold", 63),
    bg="#FFFDDD",
    fg="hot pink"
)

# ===== second page menu =====
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

# ===== return home =====
def return_home():
    # hide all pages
    greeting_label.place_forget()
    random_greeting_label.place_forget()
    main_menu_label.place_forget()
    second_menu_frame.place_forget()
    how_are_you_label.place_forget()
    emoji_frame.place_forget()
    menu_button.place_forget()
    done_button.place_forget()
    edit_entries_label.place_forget()
    view_stats_label.place_forget()
    edit_entries_frame.place_forget()
    stats_frame.place_forget()
    blank_page_label.place_forget()

    # clear inputs
    name_entry.delete(0, END)
    date_entry.delete(0, END)

    # show homepage again
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

# ===== random greetings list =====
greetings_list = [
    "✿ hope u have a great day!!",
    "✿ keep smiling :)",
    "✿ make today amazing!!",
    "✿ slay your day!!",
    "✿ stay positive and happy ;)",
    "✿ let's track some moods!",
    "✿ how are you??",
    "✿ how's your day??"
]

# ===== third page (how are you) =====
how_are_you_label = tk.Label(
    root,
    text="✿ HOW ARE YOU? ✿",
    font=("Arial Rounded MT Bold", 55),
    bg="#FFFDDD",
    fg="hot pink"
)

emoji_frame = tk.Frame(root, bg="#FFFDDD")

emotions = ["😊", "😢", "😡", "😐", "😰"]
emotion_names = ["HAPPY", "SAD", "ANGRY", "NEUTRAL", "STRESSED"]

# ===== store moods =====
mood_entries = []  # global list to store moods

# ===== emoji buttons with functionality =====
def emoji_clicked(emoji, name):
    # check if date entered
    date_val = date_entry.get().strip()
    if not date_val:
        messagebox.showwarning("No date", "Please enter date first!")
        return
    # store mood in list as dictionary
    mood_entries.append({"date": date_val, "emotion": emoji, "emotion_name": name})
    messagebox.showinfo("Saved", f"{name} mood saved!")
    open_fourth_page()  # go to edit entries page

for emo, name in zip(emotions, emotion_names):
    container = tk.Frame(emoji_frame, bg="#FFFDDD")
    container.pack(side=LEFT, padx=15, pady=20)

    btn = tk.Button(
        container,
        text=emo,
        font=("Arial Rounded MT Bold", 40),
        width=6,
        height=3,
        bg="#F7C767",
        fg="black",
        activeforeground="#F7C767",
        relief="groove",
        command=lambda e=emo, n=name: emoji_clicked(e, n)  # bind emoji click
    )
    btn.pack()

    lbl = tk.Label(
        container,
        text=name,
        font=("Arial Rounded MT Bold", 20),
        bg="#FFFDDD",
        fg="hot pink"
    )
    lbl.pack()

# ===== menu and done buttons =====
menu_button = tk.Button(root, text="MENU", font=("Arial Rounded MT Bold", 20), bg="#F7C767", width=10, activeforeground="#F7C767", relief="groove", fg="black")
done_button = tk.Button(root, text="DONE", font=("Arial Rounded MT Bold", 20), bg="#F7C767", width=10, activeforeground="#F7C767", relief="groove", fg="black")

# ===== fourth page (edit entries) =====
edit_entries_label = tk.Label(
    root,
    text="✿ EDIT ENTRIES ✿",
    font=("Arial Rounded MT Bold", 55),
    bg="#FFFDDD",
    fg="hot pink"
)

edit_entries_frame = tk.Frame(root, bg="#FFFDDD")

def refresh_edit_entries():
    # clear all existing entry widgets
    for widget in edit_entries_frame.winfo_children():
        widget.destroy()

    for i, entry in enumerate(mood_entries):
        # create frame for each mood entry
        frame = tk.Frame(edit_entries_frame, bg="#FFFDDD", relief="groove", bd=2)
        frame.pack(pady=5, padx=10, fill="x")

        # display date and mood
        tk.Label(frame, text=f"Date: {entry['date']}", font=("Arial Rounded MT Bold", 14), bg="#FFFDDD", fg="hot pink").pack(anchor="w", padx=5)
        tk.Label(frame, text=f"{entry['emotion']}  {entry['emotion_name']}", font=("Arial Rounded MT Bold", 18), bg="#FFFDDD", fg="black").pack(anchor="w", padx=5)

        btn_frame = tk.Frame(frame, bg="#FFFDDD")
        btn_frame.pack(anchor="e", padx=5, pady=2)

        # ===== edit entry =====
        def edit_entry(idx=i):
            # confirm edit
            confirm = messagebox.askyesno("Edit Entry", "Are you sure you want to edit this entry?")
            if confirm:
                del mood_entries[idx]  # simple approach: delete and go back to add entry page
                open_third_page()

        # ===== delete entry =====
        def delete_entry(idx=i):
            # confirm delete
            confirm = messagebox.askyesno("Delete Entry", "Are you sure you want to delete this entry?")
            if confirm:
                del mood_entries[idx]
                refresh_edit_entries()  # refresh page after delete

        # buttons for edit/delete
        tk.Button(btn_frame, text="Edit", command=edit_entry, relief="groove").pack(side=LEFT, padx=2)
        tk.Button(btn_frame, text="Delete", command=delete_entry, relief="groove").pack(side=LEFT, padx=2)

def open_fourth_page():
    # hide other pages
    main_menu_label.place_forget()
    second_menu_frame.place_forget()
    how_are_you_label.place_forget()
    emoji_frame.place_forget()
    view_stats_label.place_forget()

    # show edit entries page
    edit_entries_label.place(relx=0.5, y=160, anchor="n")
    edit_entries_frame.place(relx=0.5, rely=0.35, anchor="n")
    menu_button.place(relx=0.02, rely=0.95, anchor="sw")
    done_button.place(relx=0.98, rely=0.95, anchor="se")
    refresh_edit_entries()  # show current saved moods

# ===== fifth page (view stats) =====
view_stats_label = tk.Label(
    root,
    text="✿ VIEW STATS ✿",
    font=("Arial Rounded MT Bold", 55),
    bg="#FFFDDD",
    fg="hot pink"
)

stats_frame = tk.Frame(root, bg="#FFFDDD")

def refresh_stats():
    # clear stats frame
    for widget in stats_frame.winfo_children():
        widget.destroy()
    counts = {"HAPPY":0,"SAD":0,"ANGRY":0,"NEUTRAL":0,"STRESSED":0}
    # count moods
    for entry in mood_entries:
        counts[entry["emotion_name"]] += 1
    # display counts
    for emo, count in counts.items():
        tk.Label(stats_frame, text=f"{emo}: {count}", font=("Arial Rounded MT Bold", 20), bg="#FFFDDD", fg="hot pink").pack()

def open_fifth_page():
    # hide other pages
    main_menu_label.place_forget()
    second_menu_frame.place_forget()
    how_are_you_label.place_forget()
    emoji_frame.place_forget()
    edit_entries_label.place_forget()
    edit_entries_frame.place_forget()

    # show stats page
    view_stats_label.place(relx=0.5, y=160, anchor="n")
    stats_frame.place(relx=0.5, rely=0.35, anchor="n")
    menu_button.place(relx=0.02, rely=0.95, anchor="sw")
    done_button.place_forget()
    refresh_stats()  # show updated stats

# ===== third page functions =====
def open_third_page():
    # hide other pages
    main_menu_label.place_forget()
    second_menu_frame.place_forget()
    edit_entries_label.place_forget()
    edit_entries_frame.place_forget()
    view_stats_label.place_forget()
    stats_frame.place_forget()

    # show add entry page
    how_are_you_label.place(relx=0.5, y=160, anchor="n")
    emoji_frame.place(relx=0.5, y=300, anchor="n")
    menu_button.place(relx=0.02, rely=0.95, anchor="sw")
    done_button.place(relx=0.98, rely=0.95, anchor="se")

# ===== main menu navigation =====
def back_to_main_menu():
    # hide all pages
    how_are_you_label.place_forget()
    emoji_frame.place_forget()
    edit_entries_label.place_forget()
    edit_entries_frame.place_forget()
    view_stats_label.place_forget()
    stats_frame.place_forget()
    menu_button.place_forget()
    done_button.place_forget()

    # show main menu
    main_menu_label.place(relx=0.5, y=150, anchor="n")
    second_menu_frame.place(relx=0.5, rely=0.65, anchor="center")
    greeting_label.place(x=10, y=10)
    random_greeting_label.place(x=30, y=75)

# ===== done button navigation =====
def done_button_action():
    # done button goes to next page depending on current page
    if how_are_you_label.winfo_ismapped():       # from add entry
        open_fourth_page()
    elif edit_entries_label.winfo_ismapped():    # from edit entries
        open_fifth_page()

done_button.config(command=done_button_action)
menu_button.config(command=back_to_main_menu)

# ===== main menu buttons =====
button1.config(command=open_third_page)
button2.config(command=open_fourth_page)
button3.config(command=open_fifth_page)

# ===== start button =====
button_frame = tk.Frame(root, bg="#FFFDDD")
button_frame.pack(pady=13)

def start_action():
    name = name_entry.get().strip()
    date = date_entry.get().strip()
    if not name or not date:
        messagebox.showwarning("Incomplete Data", "Please enter both name and date!")
    elif not check_date_format(date):
        messagebox.showwarning("Invalid Date", "Please enter the date in mm-dd-yy format!")
    else:
        # display greetings
        greeting_label.config(text=f"Hello, {name}!")
        greeting_label.place(x=10, y=10)
        random_greeting_label.config(text=random.choice(greetings_list), font=("Kristen ITC", 24))
        random_greeting_label.place(x=30, y=75)
        # show main menu
        main_menu_label.place(relx=0.5, y=150, anchor="n")
        second_menu_frame.place(relx=0.5, rely=0.65, anchor="center")
        # hide homepage
        input_frame.pack_forget()
        button_frame.pack_forget()
        label.pack_forget()
        caption.pack_forget()
        image_label.pack_forget()

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

# ===== blank page placeholder =====
blank_page_label = tk.Label(root, text="", bg="#FFFDDD")

root.mainloop()
