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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('library/', library, name='library'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'), 
    path('profile/', profile, name='profile'), 
    path('book/<int:book_id>/', book_detail, name='book_detail'), 
    path('book/<int:pk>/issue/', issue_book, name='issue_book'), 
    path('return_book/<int:transaction_id>/', return_book, name='return_book'),
    path('search/', search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)