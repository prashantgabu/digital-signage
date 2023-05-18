from django.db.models.signals import post_delete
from django.dispatch import receiver

from signage.models import ConsultRoom, DataTracker, Doctor, OperatingRoom, RoomStatus


@receiver(post_delete, sender=ConsultRoom)
def after_delete_consult_room(sender, **kwargs):
    data_tracker, _ = DataTracker.objects.update_or_create(
        defaults={"has_consulting_rooms_changed": True})


@receiver(post_delete, sender=Doctor)
def after_delete_doctor(sender, **kwargs):
    data_tracker, _ = DataTracker.objects.update_or_create(
        defaults={"has_consulting_rooms_changed": True})


@receiver(post_delete, sender=OperatingRoom)
def after_delete_operating_room(sender, **kwargs):
    data_tracker, _ = DataTracker.objects.update_or_create(
        defaults={"has_consulting_rooms_changed": True})


@receiver(post_delete, sender=RoomStatus)
def after_delete_room_status(sender, **kwargs):
    data_tracker, _ = DataTracker.objects.update_or_create(
        defaults={"has_consulting_rooms_changed": True})
