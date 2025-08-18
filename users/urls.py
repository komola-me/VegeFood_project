from django.urls import path

from users.views import (
    UserListAPIView,
    UserDetailAPIView,
    UserProfileAPIView)

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),
]
