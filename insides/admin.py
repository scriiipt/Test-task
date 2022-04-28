from attr import field
from django.contrib import admin
from .models import Books, Authors
from django.db.models import Count

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'id')
    list_filter = ['author']
admin.site.register(Books, BooksAdmin)

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
  list_display =['name', 'id', 'books_count']
  
  def books_count(self, obj):
          return obj.books_count

  def get_queryset(self, request):
          queryset = super().get_queryset(request)
          queryset = queryset.annotate(books_count=Count("books"))
          return queryset







