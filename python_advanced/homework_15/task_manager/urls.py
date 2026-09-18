from django.urls import path

from .views import (
    task_statistics,
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView,
    TaskDetailUpdateDeleteView,
    TaskListCreateView
)

urlpatterns = [path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
               path("tasks/statistics/", task_statistics, name="task-statistics"),
               path("tasks/<int:pk>/", TaskDetailUpdateDeleteView.as_view(),
                    name="task-detail-update-delete"),
               path("subtasks/", SubTaskListCreateView.as_view(), name="subtask-list-create"),
               path("subtasks/<int:pk>/", SubTaskDetailUpdateDeleteView.as_view(),
                    name="subtask-detail-update-delete"),
               ]
