from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import (
    task_statistics,
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView,
    TaskDetailUpdateDeleteView,
    TaskListCreateView,
    CategoryViewSet,
    MyTaskView
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
               path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
               path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
               path("tasks/my/", MyTaskView.as_view(), name="my-tasks")] + router.urls
