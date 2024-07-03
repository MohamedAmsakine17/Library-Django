from django.contrib import admin
from django.urls import path
from .views.home import index
from .views.library import library
from .views.login_view import login_view
from .views.logout_view import logout_view
from .views.register_view import register_view
from .views.profile import profile  
from django.conf import settings
from django.conf.urls.static import static
from .views.book_detail import book_detail
from .views.issue_book import issue_book
from .views.return_book import return_book
from .views.search import search
from .views.admin_dashboard import admin_dashboard, user_list, book_list, transaction_list, add_user,edit_user,delete_user,add_book,add_transaction,edit_book,edit_transaction,delete_book,delete_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', admin_dashboard, name='admin_dashboard'),
    path('dashboard/users', user_list, name='user_list'),
    path('dashboard/users/add/', add_user, name='add_user'),
    path('dashboard/users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('dashboard/users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('dashboard/books', book_list, name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/',delete_book, name='delete_book'),
    path('dashboard/transactions', transaction_list, name='transaction_list'),
     path('transactions/add/', add_transaction, name='add_transaction'),
    path('transactions/edit/<int:transaction_id>/', edit_transaction, name='edit_transaction'),
    path('transactions/delete/<int:transaction_id>/', delete_transaction, name='delete_transaction'),
    path('', index, name='index'), 
    path('library/', library, name='library'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'), 
    path('profile/', profile, name='profile'), 
    path('book/<int:book_id>/', book_detail, name='book_detail'), 
    path('book/<int:pk>/issue/', issue_book, name='issue_book'), 
    path('return_book/<int:transaction_id>/', return_book, name='return_book'),
    path('search/', search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)