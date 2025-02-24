from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status


from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_mail(
                subject=f"Registration: {user.username}",
                message=f"Hi {user.username},\n\nYou've successfully registered",
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
            )
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User registered successfully."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)