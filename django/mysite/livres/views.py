from django.shortcuts import render
from .models import Livre

def livres(request):
    livres = Livre.objects.all()
    return render(request, 'livres/livres.html', {'livres': livres})
