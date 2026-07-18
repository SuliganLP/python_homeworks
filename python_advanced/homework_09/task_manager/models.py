from django.db import models


class TaskStatus(models.TextChoices):
    NEW = "new", "New"
    IN_PROGRESS = "in_progress", "In progress"
    PENDING = "pending", "Pending"
    BLOCKED = "blocked", "Blocked"
    DONE = "done", "Done"


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "task_manager_category"
        verbose_name = "Category"
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_category_name"
            )
        ]


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название задачи", unique_for_date="deadline")
    description = models.TextField(verbose_name="Описание задачи")
    categories = models.ManyToManyField(Category, related_name="tasks", verbose_name="Категории задачи")
    status = models.CharField(max_length=20, choices=TaskStatus, default=TaskStatus.NEW, verbose_name="Статус")
    deadline = models.DateTimeField(verbose_name="Дата и время дедлайна")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время создания")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_task"
        ordering = ["-created_at"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        constraints = [
            models.UniqueConstraint(
                fields=["title"],
                name="unique_task_title"
            )
        ]


class SubTask(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название подзадачи")
    description = models.TextField(verbose_name="Описание подзадачи")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks", verbose_name="Основная задача")
    status = models.CharField(max_length=20, choices=TaskStatus, default=TaskStatus.NEW, verbose_name="Статус")
    deadline = models.DateTimeField(verbose_name="Дата и время дедлайна")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время создания")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_subtask"
        ordering = ["-created_at"]
        verbose_name = "SubTask"
        constraints = [
            models.UniqueConstraint(
                fields=["title"],
                name="unique_subtask_title"
            )
        ]
