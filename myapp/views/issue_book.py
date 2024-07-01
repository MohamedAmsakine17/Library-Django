# myapp/views.py

from django.shortcuts import redirect
from ..models import Book, Transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def issue_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.available_copies > 0:
        book.available_copies -= 1
        book.save()
        transaction = Transaction.objects.create(
            user=request.user,
            book=book,
            issue_date=timezone.now(),
            status='borrowed'
        )
        transaction.save()
        return redirect('book_detail', pk=pk)
    else:
        return render(request, 'myapp/book_detail.html', {'book': book, 'error': 'No copies available.'})