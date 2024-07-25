import tkinter as tk
from tkinter import ttk
import math

# ---------------------------------------------------- (BACKEND) ----------------------------------------------------

def calculate_polygon_area(n, side_lengths):
    if len(side_lengths) < n:
        return "Not enough side lengths provided!"
    
    total_area = 0
    for i in range(n):
        s = side_lengths[i]
        area = (n * s**2) / (4 * math.tan(math.pi / n))
        total_area += area
    
    return total_area

def calculate_area():
    num_sides = int(entry_sides.get())
    side_lengths_str = entry_lengths.get()
    
    # Convert side lengths input to a list of floats
    side_lengths = [float(length.strip()) for length in side_lengths_str.split(",")]
    
    if num_sides < 3:
        result_label.config(text="Polygon must have at least 3 sides!")
    elif len(side_lengths) != num_sides:
        result_label.config(text=f"Enter {num_sides} side lengths separated by commas!")
    else:
        area = calculate_polygon_area(num_sides, side_lengths)
        result_label.config(text=f"Area of {num_sides} - sided polygon: {area:.2f} square units")


root = tk.Tk()
root.title("Polygon Area Calculator")
root.geometry("700x400+350+170")
root.resizable(False, False)

label_sides = tk.Label(root, text="Number of Sides:", font=("Arial", 15, 'bold'), fg="blue")
label_sides.grid(row=0, column=0, padx=0, pady=30)

entry_sides = tk.Entry(root, width=25, bg="sky blue", borderwidth=5, font=("arial", 15, 'bold'))
entry_sides.grid(row=0, column=1, padx=0, pady=0,)

label_lengths = tk.Label(root, text="Side Lengths (Comma-Separated):", font=("Arial", 15, 'bold'), fg="blue")
label_lengths.grid(row=1, column=0, padx=15, pady=0)

entry_lengths = tk.Entry(root, width=25, bg="sky blue", borderwidth=5, font=("arial", 15, 'bold'))
entry_lengths.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area, width=15, bd=5, bg="black", fg="White", font=("arial", 12, 'bold'))
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

result_label = tk.Label(root, text="", font=("arial", 20, 'bold'), fg="red")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()