from django.contrib import admin
from .models import Task, SubTask, Category, TaskStatus


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("short_title", "status", "deadline", "created_at")
    search_fields = ("title", "description")
    list_filter = ("status", "created_at", "deadline")
    inlines = [SubTaskInline]

    @admin.display(description="Название задачи", ordering="title")
    def short_title(self, obj):
        if len(obj.title) > 10:
            return obj.title[:10] + "..."
        return obj.title


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "created_at")
    search_fields = ("title", "description")
    list_filter = ("status", "created_at", "deadline")
    actions = ["mark_as_done"]

    @admin.action(description="Перевести выбранные подзадачи в Done")
    def mark_as_done(self, _request, queryset):
        queryset.update(status=TaskStatus.DONE)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
