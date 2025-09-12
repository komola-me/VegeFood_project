from rest_framework import serializers
from .models import Order, OrderItem, Promocode

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product_variant.product.name", read_only=True)
    variant_name = serializers.CharField(source="product_variant.name", read_only=True)

    class Meta:
        fields = [
            "id", "product_variant", "product_name", "variant_name", "quantity", "price"
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    promocode = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields  = [
            "id", "user", "status", "items", "total_amount", "promocode", "ordered_at"
        ]

    def get_promocode(self, obj):
        usage = obj.promo_usages.all().first()
        return usage.promocode.code if usage else None


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ["code", "description", "type", "value", "valid_from", "valid_until"]