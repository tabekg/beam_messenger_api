from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'rooms', views.RoomViewSet)
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('', views.home_page),
    path('api/', include(router.urls)),
]
