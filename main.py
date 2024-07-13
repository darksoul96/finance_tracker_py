import tkinter as tk
from tkinter import ttk


if __name__ == "__main__":
    # window
    window = tk.Tk()
    window.title("Finance Tracker in Python")
    window.geometry("600x300")
    window.maxsize(600, 300)

    # title
    title_label = ttk.Label(
        master=window, text="Welcome to your finance tracker!", font="Calibri 24"
    )
    title_label.pack()

    frame = ttk.Frame(master=window)
    expense_label = ttk.Label(master=frame, text="Enter expense: ", padding=10)
    expense_value = ttk.Entry(master=frame, width=50)

    save_button = ttk.Button(master=frame, text="Save", padding=5)
    quit_button = ttk.Button(
        master=frame, text="Quit", command=window.destroy, padding=5
    )

    expense_label.pack()
    expense_value.pack(pady=(20))
    save_button.pack(side=tk.LEFT, pady=20, padx=20)
    quit_button.pack(side=tk.RIGHT, padx=20)
    frame.pack()

    # run window
    window.mainloop()
