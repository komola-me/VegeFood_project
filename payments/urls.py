from django.urls import path

from .views import OrderListView, OrderDetailView, OrderCreateAPIView

urlpatterns = [
    path("order/create/", OrderCreateAPIView.as_view(), name="oder-create"),
    path("orders/list/", OrderListView.as_view(), name="orders-list"),
    path("orders/<id:int>/", OrderDetailView.as_view(), name="orders-detail"),
]
