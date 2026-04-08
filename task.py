from datetime import datetime

class Task:
    def __init__(self, task_id, description, priority, created_at=None, is_done=False):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_done = is_done

    def to_dict(self):
        return {
            "id": self.task_id,
            "description": self.description,
            "priority": self.priority,
            "created_at": self.created_at,
            "is_done": self.is_done
        }

    @staticmethod
    def from_dict(data):
        return Task(data['id'], data['description'], data['priority'], data['created_at'], data['is_done'])

    def __str__(self):
        status = "[V]" if self.is_done else "[ ]"
        return f"ID: {self.task_id} | {status} Пріоритет: {self.priority} | Створено: {self.created_at} | Опис: {self.description}"