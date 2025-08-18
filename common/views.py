from django.shortcuts import render

from common.models import Sponsor

# Create your views here.
def index(request):
    return render(request, "index.html")
