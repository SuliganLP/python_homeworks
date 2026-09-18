from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task, TaskStatus, SubTask, Category
from .serializers import (
    SubTaskCreateSerializer,
    TaskCreateSerializer,
    TaskDetailSerializer,
    CategoryCreateSerializer,
    RegisterSerializer,
    LoginSerializer
)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

        except TokenError:
            return Response({"detail": "Invalid or expired refresh token."}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    filterset_fields = ("status", "deadline")

    search_fields = ("title", "description")

    ordering_fields = ("created_at",)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


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


class MyTaskView(generics.ListCreateAPIView):
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
