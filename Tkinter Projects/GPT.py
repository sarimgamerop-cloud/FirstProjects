import tkinter as tk

root = tk.Tk()
root.title("Scrollable Canvas with Entries")
root.geometry("400x300")

# Create a frame that will hold the canvas and scrollbars
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create canvas and scrollbars
canvas = tk.Canvas(frame, bg="lightblue")
v_scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
h_scrollbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)

# Configure the canvas to use the scrollbars
canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

# Grid them inside the frame
canvas.grid(row=0, column=0, sticky="nsew")
v_scrollbar.grid(row=0, column=1, sticky="ns")
h_scrollbar.grid(row=1, column=0, sticky="ew")

# Make the frame's grid expandable
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Create a FRAME INSIDE the canvas to hold all your widgets.
# This is a critical best-practice step.
inner_frame = tk.Frame(canvas)
# Then, create a window on the canvas to hold that inner frame
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Now, create a bunch of Entry widgets and place them
# using .grid() on the INNER_FRAME, NOT on the canvas directly.
entries = []
for i in range(20):
    label = tk.Label(inner_frame, text=f"Field {i+1}:")
    label.grid(row=i, column=0, padx=5, pady=2, sticky="e")
    
    entry = tk.Entry(inner_frame, width=25)
    entry.grid(row=i, column=1, padx=5, pady=2)
    entries.append(entry)

# Update the inner frame's size and the canvas's scrollable region
# AFTER all widgets are added.
inner_frame.update_idletasks()  # Calculate the size needed
canvas.config(scrollregion=canvas.bbox("all")) # bbox("all") = bounding box of every item

root.mainloop()