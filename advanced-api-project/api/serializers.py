from rest_framework import serializers
from api.models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the book model including all fields"""
    class Meta:
        model = Book
        fields = '__all__'

    def validate_plublication_year(self,value):
        """
        Check that the publication is not in the future
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year {value} cannot be in the future, current year: {current_year}"
            )


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the author model including a custom validation and a nested BookSerializer
    """
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']
    



# The relationship between Author and Book is handled in this serializer by nesting the book 
# serializing creating declaring the bookserializer first and setting many = True to show 
# it is a many(books) to one author relationship
