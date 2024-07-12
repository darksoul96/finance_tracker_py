from tkinter import *
from tkinter import ttk


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x300")
    root.maxsize(600, 300)
    frame = ttk.Frame(root, padding=50, width=600, height=300, borderwidth=5)
    frame.grid(row=50, column=10)

    ttk.Label(frame, text="Welcome to your finance tracker!").grid(
        column=0, row=0, padx=10, pady=10
    )
    ttk.Label(frame, text="Enter expense: ").grid(column=0, row=2, padx=10, pady=10)
    ttk.Entry(frame, validate="key").grid(column=1, row=2, padx=10, pady=10)

    ttk.Button(frame, text="Save").grid(column=0, row=50, padx=10, pady=10)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(
        column=5, row=50, padx=10, pady=10
    )
    root.mainloop()
