import tkinter as tk
from tkinter import messagebox
import random

def make_groups():
    students_text = text_area.get("1.0", tk.END).strip()
    group_size = entry_size.get()

    if not students_text:
        messagebox.showerror("Error", "Please enter student names/roll numbers!")
        return

    if not group_size.isdigit() or int(group_size) <= 0:
        messagebox.showerror("Error", "Please enter a valid group size (number)!")
        return

    students = students_text.split("\n")
    random.shuffle(students)
    size = int(group_size)

    groups = [students[i:i+size] for i in range(0, len(students), size)]

    result_box.delete("1.0", tk.END)
    for idx, group in enumerate(groups, start=1):
        result_box.insert(tk.END, f"Group {idx}: {', '.join(group)}\n")

# GUI setup
root = tk.Tk()
root.title("Random Group Maker")
root.geometry("500x500")
root.config(bg="#f4f4f4")

lbl = tk.Label(root, text="Enter student names/roll numbers (one per line):", bg="#f4f4f4")
lbl.pack(pady=5)

text_area = tk.Text(root, height=10, width=50)
text_area.pack(pady=5)

lbl2 = tk.Label(root, text="Enter group size:", bg="#f4f4f4")
lbl2.pack(pady=5)

entry_size = tk.Entry(root, width=10)
entry_size.pack(pady=5)

btn = tk.Button(root, text="Make Groups 🎲", command=make_groups, bg="#4CAF50", fg="white", padx=10, pady=5)
btn.pack(pady=10)

result_box = tk.Text(root, height=10, width=50)
result_box.pack(pady=5)

root.mainloop()
