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