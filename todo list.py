import tkinter as tk
from tkinter import messagebox
import json
import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            self.save_tasks()
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            return True
        return False

    def get_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List Manager")
        self.root.geometry("400x400")
        self.task_manager = TaskManager()

        # UI Components
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(self.root, width=45, height=15)
        self.listbox.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Selected Task", width=20, command=self.delete_task)
        self.delete_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if self.task_manager.add_task(task):
            self.entry.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            if self.task_manager.delete_task(selected_index):
                self.load_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.listbox.insert(tk.END, task)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
