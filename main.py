import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap.constants as constants


def SaveExpense():
    try:
        # expense_int_value = int(expense_entry.get())
        output_string.set("Expense added succesfully!")
    except ValueError:
        output_string.set("Add a valid number")
    finally:
        expense_entry.delete(0, constants.END)
        expense_entry.focus()


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
    title_label.pack(pady=15)

    frame = ttk.Frame(master=window)
    expense_label = ttk.Label(master=frame, text="Enter expense: ", padding=10)
    # expense_int_value = tk.IntVar()
    expense_entry = ttk.Entry(master=frame, width=50)

    save_button = ttk.Button(master=frame, text="Save", padding=5, command=SaveExpense)
    quit_button = ttk.Button(
        master=frame, text="Quit", command=window.destroy, padding=5
    )

    expense_label.pack()
    expense_entry.pack(pady=(20))
    save_button.pack(side=tk.LEFT, pady=30, padx=30)
    quit_button.pack(side=tk.RIGHT, padx=20)
    frame.pack()

    output_string = tk.StringVar()
    output_label = ttk.Label(master=window, textvariable=output_string)
    output_label.pack()

    expense_entry.focus()
    # run window
    window.mainloop()
