import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("moodifyy: mood tracker")
root.configure(bg="#FFFDDD")
root.minsize(400, 300)

icon = tk.PhotoImage(file="mylogo.png")
root.iconphoto(True, icon)

#HOMEPAGE
#logo
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
input_frame.pack(pady=10)

#input name
name_label = tk.Label(
    input_frame,
    text="enter your name here :)",
    font=("Arial Rounded MT Bold", 16),
    bg="#FFFDDD",
    fg="hot pink"
)
name_label.pack(pady=15)

name_entry = tk.Entry(
    input_frame, 
    font=("Kristen ITC", 18), 
    width=30
)
name_entry.pack(pady=3)

#input date
date_label = tk.Label(
    input_frame,
    text="enter the date today :)",
    font=("Arial Rounded MT Bold", 16),
    bg="#FFFDDD",
    fg="hot pink"
)
date_label.pack(pady=3)

date_entry = tk.Entry(
    input_frame, 
    font=("Kristen ITC", 18), 
    width=30
)
date_entry.pack(pady=2)

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
    relief="ridge"
)
start_button.pack(pady=13) 

root.mainloop()
