
from django.db import models
import uuid

   
class Authors (models.Model):
    """ Авторы """
    name = models.CharField(("Имя"), max_length=50)
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   # contest = models.ForeignKey(Books)
   
    class Meta:
        verbose_name = ("Автор")
        verbose_name_plural = ("Авторы")

    def __str__(self):
        return self.name


class Books (models.Model):
    """ Книги """
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=50)
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return '%s %s' %(self.name, self.author)
    
    class Meta: 
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        
class Authr (models.Model):
    auth = Authors()
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    

        
