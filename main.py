import ttkbootstrap as ttk
import ttkbootstrap.constants as constants


# Method called after submitting
def SaveExpense():
    try:
        expense_int_value = int(expense_entry.get())
        output_string.set("Expense added succesfully!")
    except ValueError:
        output_string.set("Add a valid number")
    finally:
        expense_entry.delete(0, constants.END)
        expense_entry.focus()


if __name__ == "__main__":
    # window
    # window = tk.Tk()
    window = ttk.Window(themename="darkly")

    window.title("Finance Tracker in Python")
    window.geometry("600x300")
    window.maxsize(600, 300)

    # title
    title_label = ttk.Label(
        master=window, text="Welcome to your finance tracker!", font="Calibri 24"
    )
    title_label.pack(pady=15)

    # Main input fram
    frame = ttk.Frame(master=window)

    expense_label = ttk.Label(master=frame, text="Enter expense: ", padding=10)
    expense_entry = ttk.Entry(master=frame, width=50)

    save_button = ttk.Button(master=frame, text="Save", padding=5, command=SaveExpense)
    quit_button = ttk.Button(
        master=frame, text="Quit", command=window.destroy, padding=5
    )

    # Add labels, input and buttons to the window
    expense_label.pack()
    expense_entry.pack(pady=(20))
    save_button.pack(side=ttk.LEFT, pady=30, padx=30)
    quit_button.pack(side=ttk.RIGHT, padx=20)
    frame.pack()

    # This label shows whether the input was correct or not
    output_string = ttk.StringVar()
    output_label = ttk.Label(master=window, textvariable=output_string)
    output_label.pack()

    # This line makes sure that the cursor starts at the input
    expense_entry.focus()

    # run window
    window.mainloop()
