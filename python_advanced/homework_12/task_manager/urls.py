from django.urls import path

from .views import (
    create_task,
    task_list,
    task_detail,
    task_statistics
)

urlpatterns = [path("tasks/create/", create_task, name="create-task"),
               path("tasks/", task_list, name="task-list"),
               path("tasks/statistics/", task_statistics, name="task-statistics"),
               path("tasks/<int:task_id>/", task_detail, name="task-detail")]
