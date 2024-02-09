import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")

        self.tasks = []

        # Entry widget for adding tasks
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)

        # Button to add tasks
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Frame to display tasks
        self.tasks_frame = tk.Frame(master)
        self.tasks_frame.pack(pady=10)

        # Display initial tasks
        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self, task):
        confirmation = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{task}'?")
        if confirmation:
            self.tasks.remove(task)
            self.display_tasks()

    def edit_task(self, task):
        new_task = simpledialog.askstring("Edit Task", "Enter new task:", parent=self.master)
        if new_task:
            index = self.tasks.index(task)
            self.tasks[index] = new_task
            self.display_tasks()

    def display_tasks(self):
        # Clear previous tasks
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        # Display current tasks
        for task in self.tasks:
            task_label = tk.Label(self.tasks_frame, text=task, padx=10, pady=5)
            task_label.pack(side=tk.LEFT)

            remove_button = tk.Button(self.tasks_frame, text="Delete", bg="red", fg="white",
                                      command=lambda t=task: self.remove_task(t))
            remove_button.pack(side=tk.LEFT, padx=(0, 5))

            edit_button = tk.Button(self.tasks_frame, text="Edit", bg="green", fg="white",
                                    command=lambda t=task: self.edit_task(t))
            edit_button.pack(side=tk.LEFT)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
