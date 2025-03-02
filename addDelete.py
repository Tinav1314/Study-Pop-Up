import tkinter as tk
from tkinter import ttk, messagebox
import json
import time
import os

# ✅ Load & Save questions in JSON
def load_questions():
    if os.path.exists("questions.json"):
        try:
            with open("questions.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_questions():
    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)

# ✅ Initialize question storage
questions = load_questions()

# ✅ Create the main window
root = tk.Tk()
root.title("🚀 FocusLock - Stay Focused")
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{800}x{600}")


# ✅ Open question management window
def open_question_editor():
    """Manage question storage in a new window"""
    editor = tk.Toplevel(root)
    editor.title("📋 Manage Questions")
    editor.geometry(f"{800}x{600}")
    editor.attributes("-topmost", True)

    frame = tk.Frame(editor)
    frame.pack(pady=5)

    tk.Label(frame, text="Question:").grid(row=0, column=0, padx=5)
    question_entry = ttk.Entry(frame, width=40)
    question_entry.grid(row=0, column=1, padx=5)

    tk.Label(frame, text="Answer:").grid(row=0, column=2, padx=5)
    answer_entry = ttk.Entry(frame, width=20)
    answer_entry.grid(row=0, column=3, padx=5)

    tk.Label(frame, text="Difficulty:").grid(row=1, column=0, padx=5)
    difficulty_entry = ttk.Combobox(frame, values=["Easy", "Medium", "Hard"])
    difficulty_entry.grid(row=1, column=1, padx=5)

    question_table = ttk.Treeview(editor, columns=("Question", "Answer", "Difficulty"), show="headings", height=5)
    question_table.heading("Question", text="Question")
    question_table.heading("Answer", text="Answer")
    question_table.heading("Difficulty", text="Difficulty")
    question_table.column("Question", width=200)
    question_table.column("Answer", width=100)
    question_table.column("Difficulty", width=80)
    question_table.pack(pady=5)

    for q in questions:
        question_table.insert("", "end", values=q)

    def add_question():
        question = question_entry.get().strip()
        answer = answer_entry.get().strip()
        difficulty = difficulty_entry.get().strip()

        if question and answer and difficulty:
            questions.append((question, answer, difficulty))
            question_table.insert("", "end", values=(question, answer, difficulty))
            save_questions()
            question_entry.delete(0, tk.END)
            answer_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields must be filled.")

    def delete_question():
        selected_item = question_table.selection()
        if selected_item:
            for item in selected_item:
                question_table.delete(item)
                values = question_table.item(item, "values")
                questions.remove(values)
            save_questions()
        else:
            messagebox.showerror("Error", "Please select a question to delete.")

    button_frame = tk.Frame(editor)
    button_frame.pack(pady=5)

    add_button = tk.Button(button_frame, text="Add", command=add_question)
    add_button.grid(row=0, column=0, padx=5)

    delete_button = tk.Button(button_frame, text="Delete", command=delete_question)
    delete_button.grid(row=0, column=1, padx=5)



style = ttk.Style()
style.configure("TButton", background="white", foreground="black", padding=10, font=("Arial", 15))

# ✅ Button to Open Question Editor
manage_button = ttk.Button(root, text="Manage Questions", style="TButton", command=open_question_editor)
manage_button.pack(pady=10)
manage_button.place(x=300,y=450)



# ✅ Run the main Tkinter loop
root.mainloop()