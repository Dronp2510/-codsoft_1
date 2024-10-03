import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("300x400")
        self.root.configure(bg="#00FFFF") 

        self.tasks = []

        self.entry_frame = tk.Frame(root, bg="#00FFFF")
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=20, bg="#FFFACD", fg="#000000")
        self.task_entry.grid(row=0, column=0, padx=10)

        self.add_button = tk.Button(self.entry_frame, text="+ Add Task", bg="#D3D3D3", fg="black", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        self.tasks_frame = tk.Frame(root, bg="#00FFFF")
        self.tasks_frame.pack(pady=20)

        self.tasks_canvas = tk.Canvas(self.tasks_frame, bg="#00FFFF", bd=0, highlightthickness=0)
        self.tasks_scrollbar = tk.Scrollbar(self.tasks_frame, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_scrollbar.pack(side="right", fill="y")
        self.tasks_canvas.pack(side="left", fill="both", expand=True)

        self.tasks_frame_content = tk.Frame(self.tasks_canvas, bg="#00FFFF")
        self.tasks_canvas.create_window((0, 0), window=self.tasks_frame_content, anchor="nw")
        self.tasks_canvas.configure(yscrollcommand=self.tasks_scrollbar.set)

        self.update_task_display()

        self.remove_button = tk.Button(root, text="Remove Task", bg="#FF6347", fg="white", command=self.remove_completed_tasks)
        self.remove_button.pack(pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text != "":
            self.tasks.append({"task": task_text, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_task_display()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task_display(self):

        for widget in self.tasks_frame_content.winfo_children():
            widget.destroy()


        for index, task in enumerate(self.tasks):
            var = tk.BooleanVar(value=task["completed"])
            task_text = task["task"]
            if task["completed"]:
                task_text = f"✔ {task_text}"  

            checkbox = tk.Checkbutton(self.tasks_frame_content, text=task_text, variable=var, onvalue=True, offvalue=False, 
                                      command=lambda i=index, v=var: self.toggle_task(i, v),
                                      bg="#00FFFF", fg="#228B22" if task["completed"] else "#000000",
                                      selectcolor="#7CFC00", activebackground="#00FFFF")
            checkbox.pack(anchor="w", pady=5)

            task["variable"] = var 


        self.tasks_frame_content.update_idletasks()
        self.tasks_canvas.config(scrollregion=self.tasks_canvas.bbox("all"))

    def toggle_task(self, index, var):
        self.tasks[index]["completed"] = var.get()
        self.update_task_display()

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self.update_task_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
