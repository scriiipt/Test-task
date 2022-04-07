from django.shortcuts import render
from .models import Books, Authors
# Create your views here.


def index (request):
    list = Books.objects.all()
    return render(request, 'index.html', {'list':list})