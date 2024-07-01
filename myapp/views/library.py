# myapp/views/library.py
from django.shortcuts import render
from ..models import Book


def library(request):
    books = Book.objects.all()
    return render(request, 'myapp/library.html', {'books': books})