from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from myapp.models import Transaction

@login_required
def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    if transaction.status == 'borrowed':
        transaction.return_book()
    return redirect('profile')