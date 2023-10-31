import tkinter as tk
from tkinter import ttk

store = []

active_input = 'a'  # Variable to keep track of the active input field

def enternum():
    a = float(entry_a.get())
    b = float(entry_b.get())
    return a, b

def history():
    if len(store) == 0:
        result_display.config(text="No past calculations to show")
    else:
        result_display.config(text="\n".join(store))

def reset():
    if len(store) > 0:
        store.clear()
        result_display.config(text="Reset all calculations.")
    else:
        result_display.config(text="Already reset.")

def calculate(choice):
    a, b = enternum()
    if choice == '+':
        result = a + b
    elif choice == '-':
        result = a - b
    elif choice == '*':
        result = a * b
    elif choice == '/':
        if b == 0:
            result_display.config(text="Float division by zero")
            return
        result = a / b
    elif choice == '^':
        result = a ** b
    elif choice == '%':
        result = a % b
    else:
        result_display.config(text="Unrecognized operation")
        return

    result_display.config(text=f"{a} {choice} {b} = {result}")
    store.append(f"{a} {choice} {b} = {result}")

def on_button_click(event):
    global active_input
    button_text = event.widget.cget("text")

    if button_text in ['+', '-', '*', '/']:
        calculate(button_text)
    elif button_text == '=':
        calculate(operation.get())
    elif button_text == '#':
        root.destroy()
    elif button_text == '$':
        reset()
    elif button_text == '?':
        history()
    elif button_text.isdigit() or (button_text == '.' and active_input == 'a'):
        current_text = entry_a.get()
        entry_a.delete(0, tk.END)
        entry_a.insert(tk.END, current_text + button_text)
    elif button_text.isdigit() or (button_text == '.' and active_input == 'b'):
        current_text = entry_b.get()
        entry_b.delete(0, tk.END)
        entry_b.insert(tk.END, current_text + button_text)
    else:
        operation.set(button_text)

        # Set the active input field based on the operation
        if button_text in ['+', '-', '*', '/']:
            active_input = 'b'
        else:
            active_input = 'a'

root = tk.Tk()
root.title("Simple Calculator")

# Create a style for buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 16))

entry_a_label = tk.Label(root, text="Enter first number:")
entry_a_label.pack()
entry_a = tk.Entry(root)
entry_a.pack()

entry_b_label = tk.Label(root, text="Enter second number:")
entry_b_label.pack()
entry_b = tk.Entry(root)
entry_b.pack()

operation_label = tk.Label(root, text="Select operation:")
operation_label.pack()

operation = tk.StringVar()
operation.set('+')
operation_option = ttk.OptionMenu(root, operation, '+', '-', '*', '/', '^', '%')
operation_option.pack()

result_display = tk.Label(root, text="")
result_display.pack()

calculate_button = ttk.Button(root, text="Calculate", command=lambda: calculate(operation.get()))
calculate_button.pack()

history_button = ttk.Button(root, text="History", command=history)
history_button.pack()

reset_button = ttk.Button(root, text="Reset", command=reset)
reset_button.pack()

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

# Create the number pad
number_pad = tk.Frame(root)
number_pad.pack()

buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

row, col = 0, 0
for button_text in buttons:
    button = ttk.Button(number_pad, text=button_text)
    button.grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1
    button.bind("<Button-1>", on_button_click)

root.mainloop()
