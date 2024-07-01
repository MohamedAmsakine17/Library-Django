# myapp/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField()
    available_copies = models.IntegerField(default=0)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title  # Display book title in admin

    def update_book(self, title, author, summary, available_copies):
        self.title = title
        self.author = author
        self.summary = summary
        self.available_copies = available_copies
        self.save()

    def delete_book(self):
        self.delete()

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')

    def issue_book(self):
        if self.book.available_copies > 0:
            self.status = 'borrowed'
            self.issue_date = timezone.now()
            self.book.available_copies -= 1
            self.book.save()
            self.save()
        else:
            raise ValueError("No available copies to issue")

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'returned'
            self.return_date = timezone.now()
            self.book.available_copies += 1
            self.book.save()
            self.save()

    def check_status(self):
        return self.status