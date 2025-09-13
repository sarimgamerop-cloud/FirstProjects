import tkinter as tk
from tkinter import font

root = tk.Tk()
fonts = sorted(font.families())

for f in fonts:
    if "argent" in f.lower():   # filter for your font
        print(f)
