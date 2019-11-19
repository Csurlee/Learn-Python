import tkinter as tk

root = tk.Tk()

root.geometry("800x500")


tk.Label(root, text="Product").grid(row=0)
tk.Label(root, text="Size").grid(row=1)
tk.Label(root, text="Price").grid(row=2)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
root.mainloop()