from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Task


@receiver(pre_save, sender=Task)
def remember_old_status(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_task = Task.objects.get(pk=instance.pk)
        instance._old_status = old_task.status
    except Task.DoesNotExist:
        instance._old_status = None


@receiver(post_save, sender=Task)
def notify_owner_about_status_change(sender, instance, created, **kwargs):
    if created:
        return

    old_status = getattr(instance, "_old_status", None)

    if old_status == instance.status:
        return

    if not instance.owner:
        return

    if not instance.owner.email:
        return

    send_mail(
        subject="Task status changed",
        message=(
            f'Task "{instance.title}" changed status '
            f'from "{old_status}" to "{instance.status}".'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.owner.email],
    )
