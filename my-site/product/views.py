from django.shortcuts import render
from .models import SlidBar

def index(request):
    sliders = SlidBar.objects.filter(is_active = True)
    contex = {
        'sliders' : sliders
    }
    return render(request, 'main/index.html', contex)

