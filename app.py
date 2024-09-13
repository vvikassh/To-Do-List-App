import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do")
        self.tasks = []

        # UI elements
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(master, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.done_button = tk.Button(master, text="Mark as Done", command=self.mark_as_done)
        self.done_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_as_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            task = self.tasks[task_index]
            task["done"] = not task["done"]
            self.refresh_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            confirm_delete = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirm_delete:
                del self.tasks[selected_index[0]]
                self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            task_text = f"{idx}. {task['task']}"
            if task['done']:
                task_text += " (Done)"
                self.task_listbox.insert(tk.END, task_text)
                self.task_listbox.itemconfig(tk.END, {'bg': '#90EE90'})  # Light green
            else:
                self.task_listbox.insert(tk.END, task_text)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
