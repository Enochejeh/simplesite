from rest_framework import serializers
from .models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields =['id', 'tile', 'author', 'published_date', 'isbn_number']