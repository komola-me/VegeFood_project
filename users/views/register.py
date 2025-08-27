import jwt

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

from users.models import User
from users.serializers import UserRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    # def post(self, request, *args, **kwargs):
    #     user = self.create(request, *args, **kwargs)

    #     return Response({"status": {f"Confirmation email has been sent to {user.email}."}}, status=status.HTTP_201_CREATED)


class EmailConfirmAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        try:
            user = User.objects.get(id=decoded.get("user_id"))
        except User.DoesNotExist:
            return Response(data={"status": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        user.is_confirmed = True
        user.save()

        return Response(data={"status": "ok confirmed"}, status=status.HTTP_200_OK)