from django.shortcuts import render
from .models import Books, Authors
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
# Create your views here.


def index (request):
    list = Books.objects.all()
    return render(request, 'index.html', {'list':list})


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
    