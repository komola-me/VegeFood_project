from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Order, Promocode
from users.models import Cart
from .serializers import OrderSerializer, PromocodeSerializer
from users.serializers import CartSerializer
from .services import create_order_from_cart

# Create your views here.
class ApplyPromocodeView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        code = request.data.get("code")
        cart, _ = Cart.objects.get_or_create(user=request.user)

        try:
            promocode = Promocode.objects.get(code=code)
        except Promocode.DoesNotExist:
            return Response({"detail": "Invalid promocode"}, status=status.HTTP_400_BAD_REQUEST)

        if not promocode.is_valid_for_user(request.user):
            return Response({"detail": "Promocode not valid"}, status=status.HTTP_400_BAD_REQUEST)

        cart.applied_promo = promocode
        cart.save()
        return Response(CartSerializer(cart).data)


class PromocodeValidateView(generics.GenericAPIView):
    serializer_class = PromocodeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        code = request.data.get("code")
        try:
            promo = Promocode.objects.get(code=code)
        except Promocode.DoesNotExist:
            return Response({"detail": "Invalid promocode"}, status=400)

        if not promo.is_valid_for_user(request.user):
            return Response({"detail": "Promocode not valid"}, status=400)

        return Response(self.get_serializer(promo).data)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-ordered_at")


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-orderet_at")


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            order = create_order_from_cart(user, cart)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
