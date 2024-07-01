from django.shortcuts import render
from ..models import Book

def search(request):
    query = request.GET.get('query')
    results = Book.objects.filter(title__icontains=query) if query else None
    return render(request, 'myapp/search_results.html', {'results': results, 'query': query})
