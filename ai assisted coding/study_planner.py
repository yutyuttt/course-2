import json
import tkinter as tk
from datetime import date, datetime
from pathlib import Path
from tkinter import messagebox, ttk


DATA_FILE = Path.home() / ".study_planner.json"


class StudyPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Planner")
        self.root.geometry("980x620")
        self.root.minsize(820, 540)

        self.tasks = self.load_tasks()
        self.selected_filter = tk.StringVar(value="All")

        self.configure_styles()
        self.build_ui()
        self.refresh_tasks()

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"), foreground="#1f2937")
        style.configure("Heading.TLabel", font=("Segoe UI", 11, "bold"), foreground="#374151")
        style.configure("Card.TFrame", background="#ffffff", relief="flat")
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), foreground="#ffffff", background="#2563eb")
        style.map("Accent.TButton", background=[("active", "#1d4ed8")])
        style.configure("Danger.TButton", foreground="#b91c1c")
        style.configure("Treeview", rowheight=34, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), foreground="#374151")

        self.root.configure(bg="#f3f4f6")

    def build_ui(self):
        main = ttk.Frame(self.root, padding=24)
        main.pack(fill="both", expand=True)

        header = ttk.Frame(main)
        header.pack(fill="x", pady=(0, 16))

        ttk.Label(header, text="Study Planner", style="Title.TLabel").pack(side="left")
        ttk.Label(
            header,
            text=datetime.now().strftime("%A, %d %B"),
            foreground="#6b7280",
            font=("Segoe UI", 10),
        ).pack(side="right", pady=(8, 0))

        form = ttk.Frame(main, style="Card.TFrame", padding=18)
        form.pack(fill="x", pady=(0, 16))

        ttk.Label(form, text="Add a study session", style="Heading.TLabel").grid(
            row=0, column=0, columnspan=6, sticky="w", pady=(0, 12)
        )

        fields = [
            ("Subject", 0, 1),
            ("Task", 1, 2),
            ("Date (YYYY-MM-DD)", 2, 1),
            ("Time (HH:MM)", 3, 1),
            ("Duration (min)", 4, 1),
        ]

        self.subject_var = tk.StringVar()
        self.task_var = tk.StringVar()
        self.date_var = tk.StringVar(value=date.today().isoformat())
        self.time_var = tk.StringVar(value="16:00")
        self.duration_var = tk.StringVar(value="60")

        widgets = [
            ttk.Entry(form, textvariable=self.subject_var, width=18),
            ttk.Entry(form, textvariable=self.task_var, width=28),
            ttk.Entry(form, textvariable=self.date_var, width=14),
            ttk.Entry(form, textvariable=self.time_var, width=10),
            ttk.Entry(form, textvariable=self.duration_var, width=10),
        ]

        for (label, column, span), widget in zip(fields, widgets):
            ttk.Label(form, text=label).grid(row=1, column=column, sticky="w", padx=(0, 10))
            widget.grid(row=2, column=column, sticky="ew", padx=(0, 10), pady=(4, 0))

        form.columnconfigure(1, weight=1)
        ttk.Button(form, text="Add task", style="Accent.TButton", command=self.add_task).grid(
            row=2, column=5, padx=(8, 0), sticky="e"
        )

        toolbar = ttk.Frame(main)
        toolbar.pack(fill="x", pady=(0, 8))

        ttk.Label(toolbar, text="Show:").pack(side="left", padx=(0, 8))
        for filter_name in ("All", "Upcoming", "Completed"):
            ttk.Radiobutton(
                toolbar,
                text=filter_name,
                value=filter_name,
                variable=self.selected_filter,
                command=self.refresh_tasks,
            ).pack(side="left", padx=(0, 12))

        ttk.Button(toolbar, text="Complete", command=self.complete_task).pack(side="right", padx=(6, 0))
        ttk.Button(toolbar, text="Delete", style="Danger.TButton", command=self.delete_task).pack(side="right")

        table_frame = ttk.Frame(main)
        table_frame.pack(fill="both", expand=True)

        columns = ("subject", "task", "date", "time", "duration", "status")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        headings = ("Subject", "Task", "Date", "Time", "Duration", "Status")
        widths = (140, 320, 110, 90, 110, 100)

        for column, heading, width in zip(columns, headings, widths):
            self.table.heading(column, text=heading)
            self.table.column(column, width=width, anchor="w")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.status_label = ttk.Label(main, text="0 tasks", foreground="#6b7280")
        self.status_label.pack(anchor="w", pady=(8, 0))

    def load_tasks(self):
        if not DATA_FILE.exists():
            return []
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def save_tasks(self):
        try:
            with DATA_FILE.open("w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=2)
        except OSError as error:
            messagebox.showerror("Save error", f"Could not save tasks: {error}")

    def add_task(self):
        subject = self.subject_var.get().strip()
        task = self.task_var.get().strip()
        task_date = self.date_var.get().strip()
        task_time = self.time_var.get().strip()

        try:
            datetime.strptime(task_date, "%Y-%m-%d")
            datetime.strptime(task_time, "%H:%M")
            duration = int(self.duration_var.get().strip())
            if duration <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Invalid input",
                "Enter a valid date, time, and duration greater than zero.",
            )
            return

        if not subject or not task:
            messagebox.showwarning("Missing details", "Enter both a subject and task.")
            return

        self.tasks.append(
            {
                "subject": subject,
                "task": task,
                "date": task_date,
                "time": task_time,
                "duration": duration,
                "completed": False,
            }
        )
        self.save_tasks()
        self.task_var.set("")
        self.subject_var.set("")
        self.refresh_tasks()

    def refresh_tasks(self):
        for row in self.table.get_children():
            self.table.delete(row)

        today = date.today().isoformat()
        visible_tasks = []
        for index, task in enumerate(self.tasks):
            completed = task.get("completed", False)
            filter_name = self.selected_filter.get()
            if filter_name == "Completed" and not completed:
                continue
            if filter_name == "Upcoming" and (completed or task["date"] < today):
                continue
            visible_tasks.append((index, task))

        visible_tasks.sort(key=lambda item: (item[1]["date"], item[1]["time"]))
        for index, task in visible_tasks:
            status = "Completed" if task.get("completed", False) else "Upcoming"
            values = (
                task["subject"],
                task["task"],
                task["date"],
                task["time"],
                f'{task["duration"]} min',
                status,
            )
            row_id = self.table.insert("", "end", iid=str(index), values=values)
            if task.get("completed", False):
                self.table.set(row_id, "status", "Completed")

        count = len(visible_tasks)
        self.status_label.configure(text=f"{count} task{'s' if count != 1 else ''} shown")

    def get_selected_index(self):
        selection = self.table.selection()
        if not selection:
            messagebox.showinfo("No selection", "Select a task from the list first.")
            return None
        return int(selection[0])

    def complete_task(self):
        index = self.get_selected_index()
        if index is None:
            return
        self.tasks[index]["completed"] = not self.tasks[index].get("completed", False)
        self.save_tasks()
        self.refresh_tasks()

    def delete_task(self):
        index = self.get_selected_index()
        if index is None:
            return
        task = self.tasks[index]
        if not messagebox.askyesno("Delete task", f'Delete "{task["task"]}"?'):
            return
        del self.tasks[index]
        self.save_tasks()
        self.refresh_tasks()


if __name__ == "__main__":
    window = tk.Tk()
    app = StudyPlanner(window)
    window.mainloop()
