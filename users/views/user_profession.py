from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import Profession
from users.serializers import ProfessionListSerializer

class ProfessionListAPIView(ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionListSerializer
    permission_classes = [IsAuthenticated]