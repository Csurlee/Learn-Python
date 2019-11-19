# !/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
header_label = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam
"""

root.title("Kinder Kleider Markt")
root.geometry("1000x500")

label = tk.Label(root, text = header_label)
label.pack(padx=20, pady=20)


def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")


## BUTTONS
add = tk.Button(root, text = "Add", command = helloCallBack)
add.place(x = 500,y = 50)

## ENTRY

product = tk.Entry(root, bd=5)
product.place(x = 100 ,y = 50)
product.get()

p_size = tk.Entry(root, bd=5)
p_size.place(x = 300 ,y = 50)
p_size.get()


root.mainloop()