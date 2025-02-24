from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer
from .permissions import IsAuthenticatedOrReadOnly
from .filters import EventFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from django.core.mail import send_mail


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'date', 'location', 'organizer']
    filterset_class = EventFilter

    search_fields = ['title', 'description', 'location']

    ordering_fields = ['date', 'title']
    ordering = ['date']
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_QUERY, description="Filter by title", type=openapi.TYPE_STRING),
            openapi.Parameter('date_after', openapi.IN_QUERY, description="Filter by start date (YYYY-MM-DD)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('date_before', openapi.IN_QUERY, description="Filter by end date (YYYY-MM-DD)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('location', openapi.IN_QUERY, description="Filter by location", type=openapi.TYPE_STRING),
        ],
        operation_description="Retrieve all events with filters and JWT authentication."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class EventRegistrationViewSet(viewsets.ModelViewSet):

    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        registration = serializer.save(user=self.request.user)

        send_mail(
            subject=f"Event Registration: {registration.event.title}",
            message=f"Hi {registration.user.username},\n\nYou've successfully registered for '{registration.event.title}'",
            from_email=None,
            recipient_list=[registration.user.email],
            fail_silently=False,
        )

    def get_queryset(self):
        return EventRegistration.objects.filter(user=self.request.user)
