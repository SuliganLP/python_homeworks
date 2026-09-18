from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, TaskStatus, SubTask

from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from .serializers import (
    SubTaskCreateSerializer,
    TaskCreateSerializer,
    TaskDetailSerializer,
    TaskSerializer)


@api_view(["POST"])
def create_task(request):
    serializer = TaskCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    serializer = TaskDetailSerializer(task)

    return Response(serializer.data, status=status.HTTP_200_OK)


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


class SubTaskListCreateView(APIView):
    def get(self, request):
        subtasks = SubTask.objects.all()

        serializer = SubTaskCreateSerializer(subtasks, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = SubTaskCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SubTaskDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        subtask = get_object_or_404(SubTask, pk=pk)

        serializer = SubTaskCreateSerializer(subtask)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        subtask = get_object_or_404(SubTask, pk=pk)

        serializer = SubTaskCreateSerializer(subtask, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        subtask = get_object_or_404(SubTask, pk=pk)

        serializer = SubTaskCreateSerializer(subtask, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subtask = get_object_or_404(SubTask, pk=pk)
        subtask.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)






























