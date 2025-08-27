from django.urls import path

from users.views import (
    UserListAPIView,
    UserDetailAPIView,
    UserProfileAPIView,
    ProfessionListAPIView,
    ProfessionDetailAPIView,
    ProfessionCreateAPIView,
    ProfessionUpdateAPIView,
    ProfessionDeleteAPIView,
    UserRegisterAPIView,
    EmailConfirmAPIView,)

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("profile/", UserProfileAPIView.as_view(), name="profile"),

    path("profession/", ProfessionListAPIView.as_view(), name="profession-list"),
    path("profession/<int:id>/", ProfessionDetailAPIView.as_view(), name="profession-detail"),
    path("profession/create/", ProfessionCreateAPIView.as_view(), name="profession-create"),
    path("profession/<int:id>/update/", ProfessionUpdateAPIView.as_view(), name="profession-update"),
    path("profession/<int:id>/delete/", ProfessionDeleteAPIView.as_view(), name="profession-delete"),

    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("register/confirm/<str:token>/", EmailConfirmAPIView.as_view(), name="register-confirm"),
]
