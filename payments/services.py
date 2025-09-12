from django.db import transaction
from django.utils import timezone
from payments.models import Order, OrderItem, ProductDiscount, PromocodeUsage

def create_order_from_cart(user, cart):
    """
    Creates an Order from the user's cart:
    - applies product-level discounts
    - applies promocode if valid
    - clears the cart
    """
    now = timezone.now()
    cart_items = cart.cart_items.select_related("product_variant")

    if not cart_items.exists():
        raise ValueError("Cart is empty")

    total_amount = 0
    order_items = []

    # --- Apply product discounts ---
    for item in cart_items:
        base_price = item.product_variant.price
        final_price = base_price

        product_discount = (
            ProductDiscount.objects.filter(
                product=item.product_variant,
                valid_from__lte=now,
                valid_until__gte=now,
                discount__is_active=True,
            )
            .select_related("discount")
            .first()
        )

        if product_discount:
            discount = product_discount.discount
            if discount.discount_type == "percent":
                final_price = base_price - (base_price * discount.value / 100)
            elif discount.discount_type == "fixed":
                final_price = max(0, base_price - discount.value)

        total_amount += final_price * item.quantity

        order_items.append(
            OrderItem(
                order=None,  # set later
                product_variant=item.product_variant,
                quantity=item.quantity,
                price=final_price,
            )
        )

    # --- Create order ---
    with transaction.atomic():
        order = Order.objects.create(
            user=user,
            total_amount=total_amount,
            status="pending",
        )

        for oi in order_items:
            oi.order = order
        OrderItem.objects.bulk_create(order_items)

        # --- Apply promocode if exists ---
        if getattr(cart, "promocode", None):
            promocode = cart.promocode
            if promocode.is_valid_for_user(user):
                order.total_amount = promocode.apply_discount(total_amount)
                order.promocode = promocode
                order.save()

                PromocodeUsage.objects.create(promocode=promocode, user=user, order=order)

        # --- Clear cart ---
        cart.cart_items.all().delete()

    return order
