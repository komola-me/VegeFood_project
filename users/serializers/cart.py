from rest_framework import serializers
from users.models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product_variant.product.name", read_only=True)
    variant_name = serializers.CharField(source="product_variant.name", read_only=True)
    unit_price = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["id", "product_variant", "product_name", "variant_name", "quantity", "unit_price", "discounted_price", "total_price"]

    def get_unit_price(self, obj):
        return obj.product_variant.price

    def get_discounted_price(self, obj):
        return obj.get_discounted_price()

    def get_total_price(self, obj):
        return obj.get_total_price()


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    subtotal = serializers.SerializerMethodField()
    discount_total = serializers.SerializerMethodField()
    promocode = serializers.SerializerMethodField()
    final_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "id", "items", "subtotal", "discount_total", "promocode", "final_total"
        ]

    def get_subtotal(self, obj):
        return obj.get_subtotal()

    def get_discount_total(self, obj):
        return obj.get_discount_total()

    def get_promocode(self, obj):
        return obj.applied_promo.code if obj.applied_promo else None

    def get_final_total(self, obj):
        return obj.get_total_price()