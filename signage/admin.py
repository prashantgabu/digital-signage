from django.contrib import admin

from signage.models import Doctor, RoomStatus, OperatingRoom, ConsultRoom, DataTracker


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]

    def save_model(self, request, obj, form, change):
        data_tracker, _ = DataTracker.objects.update_or_create(
            defaults={"has_consulting_rooms_changed": True, "has_operating_rooms_changed": True})
        super().save_model(request, obj, form, change)


@admin.register(RoomStatus)
class RoomStatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]

    def save_model(self, request, obj, form, change):
        data_tracker, _ = DataTracker.objects.update_or_create(
            defaults={"has_consulting_rooms_changed": True, "has_operating_rooms_changed": True})
        super().save_model(request, obj, form, change)


@admin.register(ConsultRoom)
class ConsultRoomAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'room_status', 'name']
    search_fields = ['doctor__name', 'room_status', 'name']

    def save_model(self, request, obj, form, change):
        data_tracker, _ = DataTracker.objects.update_or_create(
            defaults={"has_consulting_rooms_changed": True})
        super().save_model(request, obj, form, change)


@admin.register(OperatingRoom)
class OperatingRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'text_input_1', 'text_input_2', 'text_input_3']
    search_fields = ['name', 'text_input_1', 'text_input_2', 'text_input_3']

    def save_model(self, request, obj, form, change):
        data_tracker, _ = DataTracker.objects.update_or_create(
            defaults={"has_operating_rooms_changed": True})
        super().save_model(request, obj, form, change)
