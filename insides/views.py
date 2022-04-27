from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from . import serializers
from .models import Authors, Books

# Create your views here.


def index (request):
    list = Authors.objects.all()
    return render(request, 'index.html', {'list': list})

    # Количество запросов
    

#   Пользователи
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
#  книги
class BooksList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer

"""   def perform_create(self, serializer):
        serializer.save(owner=self.request.user) """


class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer
    
#   АВТОРЫ
class AuthorsList (generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = serializers.AuthorsSerializer
   
    
class AuthorsDetail(generics.RetrieveAPIView):
    queryset = Authors.objects.all()
    serializer_class = serializers.AuthorsSerializer
    
    