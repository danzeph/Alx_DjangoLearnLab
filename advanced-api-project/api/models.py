from django.db import models

class Author(models.Model):
    """Author model which acts as a foreign key(one to many books) for the book model)"""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """ String representation of the author model(name) """
        return self.name

class Book(models.Model):
    """
    Book model with fields title, publication_year and author(a foreign key to author)
    """
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')

    
    def __str__(self):
        """ String represenation of the book model using books title """
        return self.title
