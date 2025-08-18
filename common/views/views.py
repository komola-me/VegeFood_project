from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from common.models import Sponsor
from common.serializers.serializer import SponsorSerializer, SponsorListSerializer


class SponsorCreateAPIView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorListSerializer


class SponsorDetailAPIView(RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorListSerializer
    lookup_field = "id"


class SponsorUpdateAPIView(UpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorDeleteAPIView(DestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    lookup_field = "id"
