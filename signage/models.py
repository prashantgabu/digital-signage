from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Doctor(BaseModel):
    name = models.CharField(_("Doctor's Name"), max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = _("Doctors")


class RoomStatus(BaseModel):
    name = models.CharField(_("Status"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = _("Room Statuses")


class ConsultRoom(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    room_status = models.ForeignKey(RoomStatus, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(_("Room Name"), max_length=50)
    room_text = models.TextField(_("Room Text"), default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Consultation Room")
        verbose_name_plural = _("Consultation Rooms")


class OperatingRoom(BaseModel):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    room_status = models.ForeignKey(RoomStatus, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(_("Room Name"), max_length=50)
    text_input_1 = models.CharField(_("Room Name"), max_length=50)
    text_input_2 = models.CharField(_("Room Name"), max_length=50)
    text_input_3 = models.CharField(_("Room Name"), max_length=50)
    room_text = models.TextField(_("Room Text"), default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Operating Room")
        verbose_name_plural = _("Operating Rooms")


class DataTracker(BaseModel):
    has_consulting_rooms_changed = models.BooleanField(default=False)
    has_operating_rooms_changed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = verbose_name_plural = _("DataTracker")

