from django.shortcuts import render
from ..models import Book  # Import the Book model

def index(request):
    # Get the first 8 books (or fewer if there aren't that many)
    books = Book.objects.all()[:8]
    return render(request, 'myapp/index.html', {'books': books})
