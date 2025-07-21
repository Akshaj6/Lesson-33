import tkinter as tk
from tkinter import ttk

# --- Main Logic Function ---
def calculate_product():
    """
    Gets two numbers from the entry widgets, calculates their product,
    and displays the result in the Text widget.
    """
    try:
        # Get the string values from the entry widgets
        num1_str = entry1.get()
        num2_str = entry2.get()

        # Convert the strings to floating-point numbers
        num1 = float(num1_str)
        num2 = float(num2_str)

        # Calculate the product
        product = num1 * num2

        # Create the result string
        result_string = f"The product of {num1} and {num2} is: {product:.2f}"

        # --- Update the Text widget ---
        # 1. Set the state to normal to allow editing
        result_textbox.config(state="normal")
        # 2. Delete any existing content (from '1.0' to 'end')
        result_textbox.delete("1.0", tk.END)
        # 3. Insert the new result string
        result_textbox.insert(tk.END, result_string)
        # 4. Set the state back to disabled to prevent user from typing in it
        result_textbox.config(state="disabled")

    except ValueError:
        # Handle cases where input is not a valid number
        result_textbox.config(state="normal")
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, "Error: Please enter valid numbers.")
        result_textbox.config(state="disabled")
    except Exception as e:
        # Handle other unexpected errors
        result_textbox.config(state="normal")
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, f"An error occurred: {e}")
        result_textbox.config(state="disabled")


# --- Main Window Setup ---
root = tk.Tk()
root.title("Getting Started With Widgets")
root.geometry("400x300") # width x height
root.resizable(False, False) # Prevent resizing

# Style for widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 11))
style.configure("TButton", font=("Helvetica", 11, "bold"))

# --- Widgets ---
# Frame to hold all content with padding
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# 1. Description Label
description_label = ttk.Label(
    main_frame,
    text="This application multiplies two numbers. Enter your numbers below.",
    wraplength=350,  # Wrap text if it gets too long
    justify="center" # Center the wrapped text
)
description_label.pack(pady=(0, 10)) # Add padding only at the bottom

# Frame to hold the input fields side-by-side
input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=5)

# 2. Labels and Entry widgets for numbers
label1 = ttk.Label(input_frame, text="Number 1:")
label1.pack(side="left", padx=(0, 5))

entry1 = ttk.Entry(input_frame, width=10)
entry1.pack(side="left")

label2 = ttk.Label(input_frame, text="Number 2:")
label2.pack(side="left", padx=(10, 5))

entry2 = ttk.Entry(input_frame, width=10)
entry2.pack(side="left")

# 3. Button to calculate
calculate_button = ttk.Button(main_frame, text="Calculate Product", command=calculate_product)
calculate_button.pack(pady=15)

# 4. Textbox to display the result
# The Text widget is more complex than a Label
result_textbox = tk.Text(
    main_frame,
    height=3, # Height in lines of text
    width=40, # Width in characters
    wrap="word", # Wrap lines at word boundaries
    font=("Helvetica", 12, "bold")
)
result_textbox.pack(pady=5)
# Disable the textbox initially so the user can't type in it
result_textbox.config(state="disabled")

# --- Start the main event loop ---
root.mainloop()