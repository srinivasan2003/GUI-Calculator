import tkinter as tk
from math import sqrt

def on_click(button_value):
    current_text = entry.get()
    if button_value == 'C':
        clear_entry()
    elif button_value == '⌫':
        entry.delete(len(current_text) - 1)
    elif button_value == '√':
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(sqrt(float(current_text))))
    elif button_value == '=':
        calculate()
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + str(button_value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Calculator by Srinivasan")


bg_color = '#F0F0F0'
button_color = '#D3D3D3'


entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=2, relief="solid", bg=bg_color)
entry.grid(row=0, column=0, columnspan=5, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('√', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('⌫', 5, 1)
]


for button_text, row_val, col_val in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 14),
              command=lambda button_text=button_text: on_click(button_text),
              bg=button_color).grid(row=row_val, column=col_val)


root.mainloop()
