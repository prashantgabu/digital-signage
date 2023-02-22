from django.urls import path

from . import views

app_name = 'films'

urlpatterns = [
    path('', views.ConsultationRoomListView.as_view(), name='consultation-room-list'),
    path('operating_rooms', views.OperatingRoomListView.as_view(), name='operating-room-list'),
    path('save-data/', views.SaveDataAPIView.as_view(), name='save-data'),
]
