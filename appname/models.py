from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Books(models.Model):
 id = models.IntegerField(primary_key=True)
 title = models.CharField(max_length=100)
 author = models.CharField(max_length=500)
 ratings = models.FloatField()
 rating_nb = models.CharField(max_length=500)
 genre = models.CharField(max_length=500)
 description = models.CharField(max_length=500)
 book_url = models.CharField(max_length=500)
 image = models.CharField(max_length=500)
 book_id = models.FloatField()
 pages = models.IntegerField()
 meta = {
     'collection': 'book-database.Books'  # Specify the MongoDB collection name
 }

 @classmethod
 def filter_by_genre(cls, genre):
     return cls.objects.filter(genre__iexact=genre)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=300)






    # class Book(models.Model):
    #     title = models.CharField(max_length=100)
    #     # author = models.CharField(max_length=500)
    #     # ratings = models.FloatField()
    #     # rating_nb = models.CharField(max_length=500)
    #     # genre = models.CharField(max_length=500)
    #     # description = models.CharField(max_length=500)
    #     # book_url = models.CharField(max_length=500)
    #     # image = models.CharField(max_length=500)
    #     # book_id = models.FloatField()
    #     # pages = models.IntegerField()

    from mongoengine import Document, fields

