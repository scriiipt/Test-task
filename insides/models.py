from asyncio.windows_events import NULL
from django.db import models

   
class Authors (models.Model):
    """ Авторы """
    name = models.CharField("Имя", max_length=50, null=True)
    id = models.AutoField(primary_key=True)

    
    class Meta:
        verbose_name = ("Автор")
        verbose_name_plural = ("Авторы")
        
    def __str__(self):
        return self.name


class Books (models.Model):
    """ Книги """
    
    author = models.ForeignKey(Authors, verbose_name='Автор', on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=50,null=True)
   # book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    
   
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        
    

        
