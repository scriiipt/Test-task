from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def firstpage (request):
    return render(request, 'insides\\newfile.html')


def testing (request):
    return HttpResponse( "<h4>HEllo World!!</h4>")