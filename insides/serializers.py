from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Books, Authors


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
class BooksSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Books
        fields = ['id','name', 'author', 'owner']


class AuthorsSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Authors
        fields = ['id','name', 'books'] 
        
               
