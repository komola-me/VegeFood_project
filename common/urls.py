from django.urls import path

# from .views import index

from .views import SponsorListAPIView, SponsorDetailAPIView, SponsorCreateAPIView, SponsorUpdateAPIView, SponsorDeleteAPIView

urlpatterns = [
    # path("", index, name="home"),
    path("sponsor/", SponsorListAPIView.as_view(), name='sponsor-list'),
    path("sponsor/create/", SponsorCreateAPIView.as_view(), name="sponsor-create"),
    path("sponsor/<int:id>/", SponsorDetailAPIView.as_view(), name="sponsor-detail"),
    path("sponsor/<int:id>/update", SponsorUpdateAPIView.as_view(), name="sponsor-update"),
    path("sponsor/<int:id>/delete/", SponsorDeleteAPIView.as_view(), name="sponsor-delete"),
]
