from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task, Category, SubTask
from django.utils import timezone
from django.contrib.auth import get_user_model, aauthenticate
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = aauthenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Неверный логин или пароль.")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        read_only_fields = ("id",)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Пользователь с таким username уже существует.")

        return value

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")

        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "status", "deadline")
        read_only_fields = ("id",)


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = "__all__"
        read_only_fields = ("created_at", "owner")


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
        fields = (
            "id",
            "title",
            "description",
            "status",
            "deadline",
            "subtasks",
            "owner"
        )

        read_only_fields = ("owner",)


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "status",
            "deadline",
            "owner"
        )
        read_only_fields = ("id", "owner")

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Дедлайн не может быть в прошлом.")
        return value
