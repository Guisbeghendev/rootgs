# home/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')  # Renderiza o template da página inicial





