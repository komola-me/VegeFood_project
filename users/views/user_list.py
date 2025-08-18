from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.serializers import UserListSerializer

class UserListAPIView(APIView):
    serializer_class = UserListSerializer

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        return User.objects.all().order_by("id")
