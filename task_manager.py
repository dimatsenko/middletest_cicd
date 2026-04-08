import json
import os
from task import Task


class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in self.tasks], f, ensure_ascii=False, indent=4)

            def add_task(self, description, priority):
                new_id = max([t.task_id for t in self.tasks], default=0) + 1
                new_task = Task(new_id, description, priority)
                self.tasks.append(new_task)
                self.save_tasks()
                return new_id

            def delete_task(self, task_id):
                initial_count = len(self.tasks)
                self.tasks = [t for t in self.tasks if t.task_id != task_id]
                if len(self.tasks) < initial_count:
                    self.save_tasks()
                    return True
                return False