from django.shortcuts import render

from rest_framework import viewsets
from .models import Book 
from serializers import BookSerializers 

class BookViewSets(viewsets.ModelViewSets):
    queryset = Book.objects.all()
    serializers_class = BookSerializers 