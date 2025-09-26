class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, urgency, importance):
        """Add a task with name, urgency, and importance."""
        if not (1 <= urgency <= 10 and 1 <= importance <= 10):
            raise ValueError("Urgency and importance must be between 1 and 10.")
        task = {
            "name": name,
            "urgency": urgency,
            "importance": importance,
            "score": self._calculate_score(urgency, importance)
        }
        self.tasks.append(task)

    def _calculate_score(self, urgency, importance):
        """Calculate a priority score based on urgency and importance."""
        # Simple weighted formula: 60% urgency, 40% importance
        return (0.6 * urgency + 0.4 * importance)

    def prioritize_tasks(self):
        """Return tasks sorted by priority score (descending)."""
        return sorted(self.tasks, key=lambda x: x["score"], reverse=True)