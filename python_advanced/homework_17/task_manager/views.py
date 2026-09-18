from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, TaskStatus, SubTask, Category
from .serializers import (
    SubTaskCreateSerializer,
    TaskCreateSerializer,
    TaskDetailSerializer,
    CategoryCreateSerializer
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


class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    filterset_fields = ("status", "deadline")

    search_fields = ("title", "description")

    ordering_fields = ("created_at",)


class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

    @action(detail=True, methods=["get"])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        count = category.tasks.count()

        return Response({
            "category": category.name,
            "tasks_count": count
        })
