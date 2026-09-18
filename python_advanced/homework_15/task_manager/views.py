from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, TaskStatus, SubTask
from .serializers import (
    SubTaskCreateSerializer,
    TaskCreateSerializer,
    TaskDetailSerializer,
)


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    filterset_fields = ("status", "deadline")

    search_fields = ("title", "description")

    ordering_fields = ("created_at",)


class TaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


@api_view(["GET"])
def task_statistics(request):
    total_tasks = Task.objects.count()
    task_by_status = {
        status_value: Task.objects.filter(status=status_value).count()
        for status_value, _ in TaskStatus.choices
    }
    overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

    data = {
        "total_tasks": total_tasks,
        "tasks_by_status": task_by_status,
        "overdue_tasks": overdue_tasks
    }

    return Response(data, status=status.HTTP_200_OK)


class SubTaskPagination(PageNumberPagination):
    page_size = 5


class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
    pagination_class = SubTaskPagination

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    filterset_fields = ("status", "deadline")

    search_fields = ("title", "description")

    ordering_fields = ("created_at",)


class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
