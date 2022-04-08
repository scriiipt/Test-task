from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path( "",views.index  , name = 'list'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('books/', views.BooksList.as_view()),
    path('books/<int:pk>/', views.BooksDetail.as_view()),
    path('author/', views.AuthorsList.as_view()),
    path('author/<int:pk>/', views.AuthorsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)