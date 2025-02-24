from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventRegistrationViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'events-registration', EventRegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]