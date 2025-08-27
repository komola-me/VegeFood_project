from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from users.utils import generate_confirmation_token


@shared_task
def send_register_email(user_id, email):
    token = generate_confirmation_token(user_id)

    print(">>>> Email should be sent")
    send_mail(
        subject="Confirm your account",
        recipient_list=[email],
        message=f"Click here to confirm your account: http://127.0.0.1:8000/users/confirm/{token}",
        from_email=settings.EMAIL_HOST_USER,
    )