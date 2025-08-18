from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RegisterUserView(TemplateView):
    template_name = "auth/register.html"


class LoginView():
    pass