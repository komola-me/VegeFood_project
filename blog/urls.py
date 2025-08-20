from django.urls import path

from blog.views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDeleteAPIView
)

urlpatterns = [
    #### category ##############
    path("category/", CategoryListAPIView.as_view(), name="category-list"),
    path("category/<int:id>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("category/create/", CategoryCreateAPIView.as_view(),  name="category-create"),
    path("category/<int:id>/update/", CategoryUpdateAPIView.as_view(), name="category-update"),
    path("category/<int:id>/delete/", CategoryDeleteAPIView.as_view(),  name="category-delete"),

    ######## tag #############


    ######## post ############
]
