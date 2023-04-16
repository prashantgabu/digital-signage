from django.views import View
from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ConsultRoom, OperatingRoom, Doctor, RoomStatus, DataTracker


class ConsultationRoomBaseView(View):
    model = ConsultRoom


class ConsultationRoomListView(ConsultationRoomBaseView, ListView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(ConsultationRoomListView, self).get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        context['room_statuses'] = RoomStatus.objects.all()
        context['operating_rooms'] = OperatingRoom.objects.all()
        return context


class OperatingRoomBaseView(View):
    model = OperatingRoom


class OperatingRoomListView(OperatingRoomBaseView, ListView):
    template_name = "SurgicalSuite.html"


class SaveDataAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        response = {
            "data_changed": False
        }
        key = request.query_params.get('key')
        data_tracker = DataTracker.objects.filter().first()
        if data_tracker:
            value = getattr(data_tracker, key)
            response['data_changed'] = value
            setattr(data_tracker, key, False)
            data_tracker.save()
        return Response(response,
                        status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        for key, value in data.items():
            room_data = data[key]
            room = ConsultRoom.objects.filter(id=key).first()
            if room:
                doctor_id = room_data.get('doctor')
                room_status_id = room_data.get('room_status')
                room_text = room_data.get('room_text', None)
                if room_text:
                    room_text = room_text.strip()
                    room.room_text = room_text
                if doctor_id:
                    doctor = Doctor.objects.filter(id=doctor_id).first()
                    room.doctor = doctor
                if room_status_id:
                    room_status = RoomStatus.objects.filter(id=room_status_id).first()
                    room.room_status = room_status
                room.save()
        return Response({}, status=status.HTTP_200_OK)
