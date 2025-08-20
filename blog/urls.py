from django.urls import path

from blog.views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDeleteAPIView,

    TagListAPIView,
    TagDetailAPIView,
    TagCreateAPIView,
    TagUpdateAPIView,
    TagDeleteAPIView,
)

urlpatterns = [
    #### category ##############
    path("category/", CategoryListAPIView.as_view(), name="category-list"),
    path("category/<int:id>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("category/create/", CategoryCreateAPIView.as_view(),  name="category-create"),
    path("category/<int:id>/update/", CategoryUpdateAPIView.as_view(), name="category-update"),
    path("category/<int:id>/delete/", CategoryDeleteAPIView.as_view(),  name="category-delete"),

    ######## tag #############
    path("tag/", TagListAPIView.as_view(), name="tag-list"),
    path("tag/<int:id>/", TagDetailAPIView.as_view(), name="tag-detail"),
    path("tag/create/", TagCreateAPIView.as_view(), name="tag-create"),
    path("tag/<int:id>/update/", TagUpdateAPIView.as_view(), name="tag-update"),
    path("tag/<int:id>/delete/", TagDeleteAPIView.as_view(), name="tag-delete"),

    ######## post ############
]
