#CODE CLAUSE INTERNSHIP 

#Position- Python Development Intern
# Allocated Project

#Task 2
#Calculator in Python


import tkinter as tk

cal = ""

def add_to_cal(symbol):
    global cal
    cal += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, cal)

def evaluate_cal():
    global cal
    try:
        cal = str(eval(cal))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, cal)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global cal
    cal = ""
    text_result.delete(1.0, "end")

# Create the main application window
root = tk.Tk()
root.geometry("300x300")

# Create a text field to display the calculator input and result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Button colors
button_colors = {
    "digits": "#00CCFF",   # Light Blue
    "operators": "#F0F0F0",   # Light Gray
    "equal": "#FFCC00",   # Orange
    "brackets": "#C0C0C0",   # Gray
    "clear": "#FF0000"   # Red
}

# Button border properties
button_border_relief = "groove"  # Options: "flat", "raised", "sunken", "solid", "ridge", "groove"
button_border_width = 1  # Set to 0 for rounded borders

# Create buttons for digits 1-9
for i in range(1, 10):
    btn = tk.Button(root, text=str(i), command=lambda i=i: add_to_cal(i), width=5, font=("Arial", 14),
                    bg=button_colors["digits"], relief=button_border_relief, borderwidth=button_border_width)
    btn.grid(row=(i-1)//3 + 2, column=(i-1)%3 + 1)

# Create a button for digit 0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_cal(0), width=5, font=("Arial", 14),
                  bg=button_colors["digits"], relief=button_border_relief, borderwidth=button_border_width)
btn_0.grid(row=5, column=2)

# Create buttons for arithmetic operators ("+", "-", "*", "/")
operators = ["+", "-", "*", "/"]
for i, operator in enumerate(operators):
    btn_operator = tk.Button(root, text=operator, command=lambda operator=operator: add_to_cal(operator), width=5, font=("Arial", 14),
                             bg=button_colors["operators"], relief=button_border_relief, borderwidth=button_border_width)
    btn_operator.grid(row=i+2, column=4)

# Create additional buttons ("=", "C", "(", ")")
btn_equal = tk.Button(root, text="              =", command=evaluate_cal, width=11, font=("Arial", 14),
                      bg=button_colors["equal"], relief=button_border_relief, borderwidth=button_border_width)
btn_equal.grid(row=5, column=3, columnspan=2)

btn_open_bracket = tk.Button(root, text="(", command=lambda: add_to_cal('('), width=5, font=("Arial", 14),
                             bg=button_colors["brackets"], relief=button_border_relief, borderwidth=button_border_width)
btn_open_bracket.grid(row=5, column=1)

btn_close_bracket = tk.Button(root, text=")", command=lambda: add_to_cal(')'), width=5, font=("Arial", 14),
                              bg=button_colors["brackets"], relief=button_border_relief, borderwidth=button_border_width)
btn_close_bracket.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14),
                      bg=button_colors["clear"], relief=button_border_relief, borderwidth=button_border_width)
btn_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
