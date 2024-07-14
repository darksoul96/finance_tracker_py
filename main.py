import ttkbootstrap as ttk
import ttkbootstrap.constants as constants
import csv
import os


# Define the filename
filename = "data.csv"

# Define the headers and data to be written
headers = ["Name", "Value", "Category"]


def SaveExpense(name: str, value: int, category: str):
    if category == "":
        category = "Other"
    try:
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, value, category])
            output_string.set("Expense added succesfully!")
            output_label.configure(foreground="green")
    except any:
        output_string.set("Value could not be saved")


# Method called after submitting
def ValidateExpenseInput():
    try:
        expense_name_str = str(expense_name_entry.get())
        expense_value_int = int(expense_value_entry.get())
        expense_category_str = str(expense_category_combobox.get())
        SaveExpense(expense_name_str, expense_value_int, expense_category_str)
    except ValueError:
        output_string.set("Add a valid name and/or value")
        output_label.configure(foreground="red")
    finally:
        expense_name_entry.delete(0, constants.END)
        expense_value_entry.delete(0, constants.END)
        expense_name_entry.focus()


if __name__ == "__main__":
    file_exists = os.path.isfile(filename)

    if not file_exists:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

    # window
    window = ttk.Window(themename="darkly")

    window.title("Finance Tracker in Python")
    window.geometry("600x500")
    window.maxsize(600, 500)

    # title
    title_label = ttk.Label(
        master=window, text="Welcome to your finance tracker!", font="Calibri 24"
    )
    title_label.pack(pady=15)

    # Main input fram
    frame = ttk.Frame(master=window)

    expense_name_label = ttk.Label(master=frame, text="Enter expense name: ", padding=5)
    expense_name_entry = ttk.Entry(master=frame, width=50)

    expense_value_label = ttk.Label(
        master=frame, text="Enter expense value: ", padding=5
    )
    expense_value_entry = ttk.Entry(master=frame, width=50)

    expense_category_label = ttk.Label(
        master=frame, text="Select expense category", padding=5
    )
    expense_category_combobox = ttk.Combobox(
        master=frame, values=["Auto", "Alquiler", "Comida", "Gatos"]
    )

    save_button = ttk.Button(
        master=frame, text="Save", padding=10, command=ValidateExpenseInput
    )
    quit_button = ttk.Button(
        master=frame, text="Quit", command=window.destroy, padding=10
    )

    # Add labels, input and buttons to the window
    expense_name_label.pack()
    expense_name_entry.pack(pady=(20))

    expense_value_label.pack()
    expense_value_entry.pack(pady=(20))

    expense_category_label.pack()
    expense_category_combobox.pack(pady=15)
    save_button.pack(side=ttk.LEFT, padx=20)
    quit_button.pack(side=ttk.RIGHT, padx=20)
    frame.pack()

    # This label shows whether the input was correct or not
    output_string = ttk.StringVar()
    output_label = ttk.Label(master=window, textvariable=output_string, padding=15)
    output_label.pack()

    # This line makes sure that the cursor starts at the input
    expense_name_entry.focus()

    # run window
    window.mainloop()
