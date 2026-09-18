from rest_framework import serializers
from .models import Task, Category, SubTask
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "status", "deadline")
        read_only_fields = ("id",)


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = "__all__"
        read_only_fields = ("created_at",)


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        name = validated_data.get("name")

        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError({"name": "Категория с таким названием уже существует."})

        return super().create(validated_data)

    def update(self, instance: Category, validated_data):
        name = validated_data.get("name", instance.name)

        if Category.objects.filter(name=name).exclude(id=instance.id).exists():
            raise serializers.ValidationError({"name": "Категория с таким названием уже существует."})

        return super().update(instance, validated_data)


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = "__all__"


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        field = (
            "id",
            "title",
            "description",
            "status",
            "deadline",
            "subtask"
        )


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = (
            "id",
            "title",
            "description",
            "status",
            "deadline"
        )
        read_only_field = ("id",)

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Дедлайн не может быть в прошлом.")
        return value
