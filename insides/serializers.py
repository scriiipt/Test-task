from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Books, Authors


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
class BooksSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    #author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Books
        fields = ['id','name', 'author']


class AuthorsSerializer(serializers.ModelSerializer):
    #tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Authors
        fields = ['name','id'] 
        
        
               
