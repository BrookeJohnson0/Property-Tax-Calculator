import tkinter as tk
from tkinter import messagebox

# First list variables

def calculate_tax():
    try:
        # Get the property value from entry
        property_value = float(entry_value.get())

        # Calculate assessment and tax
        assessment_value = property_value * 0.60
        property_tax = assessment_value * 0.0072  # 72 cents per $100

        # Display results
        label_assessment.config(text=f"Assessment Value: ${assessment_value:,.2f}")
        label_tax.config(text=f"Property Tax: ${property_tax:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")


# Create the main window
root = tk.Tk()
root.title("Property Tax Calculator")
root.geometry("350x200")

# Add widgets
tk.Label(root, text="Enter Actual Property Value ($):").pack(pady=5)
entry_value = tk.Entry(root, width=30)
entry_value.pack(pady=5)

tk.Button(root, text="Calculate Tax", command=calculate_tax).pack(pady=10)

label_assessment = tk.Label(root, text="Assessment Value:")
label_assessment.pack(pady=5)

label_tax = tk.Label(root, text="Property Tax:")
label_tax.pack(pady=5)

# Run the application
root.mainloop()
