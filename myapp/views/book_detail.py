from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from ..models import Book, Transaction
from django.contrib.auth.decorators import login_required

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_transactions = Transaction.objects.filter(user=request.user, book=book, status='borrowed')
    already_issued = user_transactions.exists()

    if request.method == 'POST' and 'issue_book' in request.POST:
        if not already_issued and book.available_copies > 0:
            transaction = Transaction(user=request.user, book=book)
            transaction.issue_book()
            return redirect('profile')

    other_books = Book.objects.exclude(id=book_id)[:4]
    context = {
        'book': book,
        'already_issued': already_issued,
        'other_books': other_books,
    }
    return render(request, 'myapp/book_detail.html', context)
