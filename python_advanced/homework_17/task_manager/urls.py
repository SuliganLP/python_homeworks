from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet
from .views import (
    task_statistics,
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView,
    TaskDetailUpdateDeleteView,
    TaskListCreateView
)

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
urlpatterns = [path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
               path("tasks/statistics/", task_statistics, name="task-statistics"),
               path("tasks/<int:pk>/", TaskDetailUpdateDeleteView.as_view(),
                    name="task-detail-update-delete"),
               path("subtasks/", SubTaskListCreateView.as_view(), name="subtask-list-create"),
               path("subtasks/<int:pk>/", SubTaskDetailUpdateDeleteView.as_view(),
                    name="subtask-detail-update-delete"),
               ] + router.urls
