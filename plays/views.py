from django.shortcuts import render
from .models import Performance


def performances_list(request):
    performances = Performance.objects.all()
    context = {
        'performances': performances
    }
    return render(request, 'play/afisha.html', context)
