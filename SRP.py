from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True
        print(f"Task '{self.title}' completed.")

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added.")

    def list_tasks(self):
        for task in self.tasks:
            status = "✔" if task.completed else "✘"
            print(f"[{status}] {task.title} - Due {task.due_date}")

class Notifier:
    def send_reminder(self, task):
        if datetime.now() > task.due_date:
            print(f"⚠ Reminder: Task '{task.title}' is overdue.")
        else:
            print(f"🔔 Reminder: Don't forget to complete '{task.title}'.")

# Usage
task1 = Task("Submit report", "Send the monthly report to the manager", datetime(2025, 4, 15))
task2 = Task("Pay bills", "Pay electricity and internet bills", datetime(2025, 4, 10))

task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)

task_manager.list_tasks()

notifier = Notifier()
notifier.send_reminder(task1)
